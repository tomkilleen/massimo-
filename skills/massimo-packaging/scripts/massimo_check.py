#!/usr/bin/env python3
"""
massimo_check: measure a page, poster, diagram or dieline against the Vignelli canon.

Usage:
  python3 massimo_check.py <file.html|file.svg|http://localhost:3000> [--mode ui|poster|infographic|packaging] [--json]

Renders the target in headless Chromium (Playwright) and reads computed styles,
so it works on any framework's output. Without Playwright it falls back to a
rougher scan of the CSS text in the file.

Exit code 0 when there are no failures, 1 when the canon is broken.
Install Playwright once:  pip install playwright && python3 -m playwright install chromium
"""
import json, re, sys, pathlib

PALETTE = {
    "ink": (17, 17, 17), "paper": (255, 255, 255), "grey": (94, 94, 94),
    "hairline": (212, 212, 212), "wash": (242, 242, 240), "red": (226, 35, 26),
    "blue": (0, 57, 166), "yellow": (255, 204, 0), "black": (0, 0, 0),
}
SCALE = {12, 16, 32, 64, 128}
BANNED_FONTS = {"inter", "space grotesk", "poppins", "montserrat", "roboto", "open sans", "lato", "nunito", "dm sans", "manrope", "plus jakarta sans", "outfit", "sora"}
SIZE_LIMIT = {"ui": 3, "poster": 3, "infographic": 3, "packaging": 4}  # per view; poster: 2 + one legal/small line

JS = r"""
() => {
  const out = [];
  const els = document.querySelectorAll('body *, svg *');
  for (const el of els) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    let hasText = false;
    for (const n of el.childNodes) if (n.nodeType === 3 && n.textContent.trim()) { hasText = true; break; }
    out.push({
      tag: el.tagName.toLowerCase(), hasText, w: r.width, h: r.height,
      font: cs.fontFamily, size: parseFloat(cs.fontSize), weight: cs.fontWeight, style: cs.fontStyle,
      align: cs.textAlign, color: cs.color, bg: cs.backgroundColor, bgImg: cs.backgroundImage,
      fill: cs.fill, stroke: cs.stroke,
      radius: [cs.borderTopLeftRadius, cs.borderTopRightRadius, cs.borderBottomLeftRadius, cs.borderBottomRightRadius],
      shadow: cs.boxShadow, tshadow: cs.textShadow, anim: cs.animationName,
      borders: ['Top','Right','Bottom','Left'].map(s => [cs['border'+s+'Style'], parseFloat(cs['border'+s+'Width']), cs['border'+s+'Color']]),
      spacing: [cs.marginTop, cs.marginRight, cs.marginBottom, cs.marginLeft, cs.paddingTop, cs.paddingRight, cs.paddingBottom, cs.paddingLeft, cs.rowGap, cs.columnGap],
      cls: (el.getAttribute('class') || '').toString().slice(0, 60)
    });
  }
  return out;
}
"""

def rgb(s):
    m = re.match(r"rgba?\(([\d.]+)[, ]+([\d.]+)[, ]+([\d.]+)(?:[, /]+([\d.]+))?", s or "")
    if not m: return None
    a = float(m.group(4)) if m.group(4) else 1.0
    if a == 0: return None
    return tuple(int(float(m.group(i))) for i in (1, 2, 3))

def near_palette(c, tol=18):
    return any(sum(abs(a - b) for a, b in zip(c, p)) <= tol for p in PALETTE.values())

def is_red(c):
    return c and sum(abs(a - b) for a, b in zip(c, PALETTE["red"])) <= 30

def first_family(f):
    return (f or "").split(",")[0].strip().strip('"\'').lower()

def analyse(items, mode):
    fails, warns, facts = [], [], {}
    text = [i for i in items if i["hasText"]]
    fams = sorted({first_family(i["font"]) for i in text})
    sizes = sorted({round(i["size"]) for i in text})
    facts["typefaces"] = fams
    facts["type_sizes_px"] = sizes
    if len(fams) > 2: fails.append(f"{len(fams)} typefaces in use ({', '.join(fams)}). The canon allows two at most.")
    bad = [f for f in fams if f in BANNED_FONTS]
    if bad: fails.append(f"Generic 'modern' typeface in use: {', '.join(bad)}. Use Helvetica, or a Canon serif.")
    limit = SIZE_LIMIT.get(mode, 3)
    if len(sizes) > limit: fails.append(f"{len(sizes)} type sizes in one view ({sizes}). Limit for {mode}: {limit}.")
    if mode == "ui":
        off = [s for s in sizes if s not in SCALE]
        if off: warns.append(f"Sizes outside the scale 12/16/32/64/128: {off}.")
    centred = [i for i in text if i["align"] in ("center", "justify") and i["tag"] not in ("button", "th", "td")]
    if centred: fails.append(f"{len(centred)} text blocks centred or justified (e.g. <{centred[0]['tag']} class='{centred[0]['cls']}'>). Set flush left.")
    italic_display = [i for i in text if i["style"] == "italic" and i["size"] >= 32]
    if italic_display: fails.append("Italic display type found. Display type is roman.")
    rounded = [i for i in items if any(float(re.sub(r'[^\d.]', '', r) or 0) > 0 for r in i["radius"]) and not (abs(i["w"] - i["h"]) < 1 and i["w"] <= 48)]
    if rounded: fails.append(f"{len(rounded)} elements with rounded corners (e.g. <{rounded[0]['tag']} class='{rounded[0]['cls']}'>). Radius is 0.")
    shadows = [i for i in items if (i["shadow"] and i["shadow"] != "none") or (i["tshadow"] and i["tshadow"] != "none")]
    if shadows: fails.append(f"{len(shadows)} elements with shadows. No elevation in this system.")
    grads = [i for i in items if "gradient" in (i["bgImg"] or "")]
    if grads: fails.append(f"{len(grads)} gradients. Flat colour only.")
    widths = set()
    for i in items:
        for style, w, col in i["borders"]:
            if style not in ("none", "hidden") and w > 0: widths.add(round(w, 1))
    facts["rule_weights_px"] = sorted(widths)
    extra = [w for w in widths if w not in (1, 2)]
    if mode in ("ui", "poster", "infographic") and extra: fails.append(f"Rule weights outside 1px/2px: {extra}.")
    if len([w for w in widths if w in (1, 2)]) and len(widths) > 2: warns.append("More than two rule weights.")
    offgrid = set()
    if mode == "ui":
        for i in items:
            for v in i["spacing"]:
                try: n = float(str(v).replace("px", ""))
                except ValueError: continue
                if n > 2 and round(n) % 6 != 0: offgrid.add(round(n))
    facts["off_module_spacing_px"] = sorted(offgrid)
    if len(offgrid) > 3: fails.append(f"Spacing off the 6/12/24px module: {sorted(offgrid)[:10]}.")
    elif offgrid: warns.append(f"A few spacing values off the module: {sorted(offgrid)}.")
    colours, reds = set(), 0
    for i in items:
        for key in ("color", "bg", "fill", "stroke"):
            c = rgb(i[key])
            if not c: continue
            if key == "color" and not i["hasText"]: continue
            colours.add(c)
            if is_red(c) and key in ("bg", "fill") and i["w"] * i["h"] > 0: reds += 1
            elif is_red(c) and key == "color" and i["hasText"]: reds += 1
    offp = sorted(c for c in colours if not near_palette(c))
    facts["colours_off_palette"] = ["#%02x%02x%02x" % c for c in offp]
    facts["red_elements"] = reds
    if mode in ("ui",) and len(offp) > 2: fails.append(f"{len(offp)} colours outside the palette: {facts['colours_off_palette'][:6]}.")
    elif offp and mode == "ui": warns.append(f"Colours outside the palette: {facts['colours_off_palette']}.")
    if mode == "ui" and reds > 6: warns.append(f"Red appears on {reds} elements. Red should mark the one thing that needs attention.")
    anims = [i for i in items if i["anim"] and i["anim"] != "none"]
    if anims: warns.append(f"{len(anims)} animated elements. Motion should be instant colour change only.")
    return fails, warns, facts

def static_scan(path, mode):
    t = pathlib.Path(path).read_text(errors="ignore")
    fails, warns, facts = [], [], {"note": "static scan (Playwright not available): approximate"}
    fams = sorted({first_family(m) for m in re.findall(r"font-family\s*:\s*([^;}{]+)", t)})
    sizes = sorted({round(float(m)) for m in re.findall(r"font-size\s*:\s*([\d.]+)px", t)})
    facts.update(typefaces=fams, type_sizes_px=sizes)
    if len(fams) > 2: fails.append(f"{len(fams)} font-family declarations: {fams}.")
    if re.search(r"border-radius\s*:\s*(?!0[;\s}]|0px)", t): fails.append("border-radius other than 0 declared.")
    if re.search(r"box-shadow\s*:\s*(?!none)", t): fails.append("box-shadow declared.")
    if "gradient(" in t: fails.append("Gradient declared.")
    if re.search(r"text-align\s*:\s*(center|justify)", t): fails.append("Centred or justified text declared.")
    return fails, warns, facts

def rendered_fonts(pg, limit=300):
    """Ask Chromium which font files actually drew the text (catches silent fallbacks)."""
    try:
        cdp = pg.context.new_cdp_session(pg)
        cdp.send("DOM.enable"); cdp.send("CSS.enable")
        doc = cdp.send("DOM.getDocument", {"depth": -1, "pierce": True})
        ids = cdp.send("DOM.querySelectorAll", {"nodeId": doc["root"]["nodeId"], "selector": "body *, svg text"})["nodeIds"][:limit]
        names = set()
        for nid in ids:
            try:
                for f in cdp.send("CSS.getPlatformFontsForNode", {"nodeId": nid}).get("fonts", []):
                    names.add(f["familyName"])
            except Exception:
                pass
        return names
    except Exception:
        return set()

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args: print(__doc__); sys.exit(2)
    target = args[0]
    mode = "ui"
    if "--mode" in sys.argv:
        mode = sys.argv[sys.argv.index("--mode") + 1]
        args = [a for a in args if a != mode]
    as_json = "--json" in sys.argv
    url = target if re.match(r"https?://", target) else pathlib.Path(target).resolve().as_uri()
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={"width": 1440, "height": 1000})
            pg.goto(url, wait_until="networkidle")
            pg.wait_for_timeout(400)
            items = pg.evaluate(JS)
            rendered = rendered_fonts(pg)
            b.close()
        fails, warns, facts = analyse(items, mode)
        facts["rendered_fonts"] = sorted(rendered)
        bad = [f for f in rendered if f.lower() in BANNED_FONTS or f.lower().startswith("inter")]
        if bad: fails.append(f"The page asks for one face but the machine renders {bad}: a silent fallback. Load the font (or an open stand-in such as Arimo) explicitly.")
        if len(rendered) > 2: warns.append(f"{len(rendered)} faces actually rendered: {sorted(rendered)}.")
    except ImportError:
        fails, warns, facts = static_scan(target, mode)
    if as_json:
        print(json.dumps({"target": target, "mode": mode, "pass": not fails, "failures": fails, "warnings": warns, "facts": facts}, indent=2))
    else:
        print(f"MASSIMO CHECK  {target}  ({mode})")
        print("-" * 60)
        for k, v in facts.items(): print(f"{k:24} {v}")
        print("-" * 60)
        for f in fails: print("FAIL  " + f)
        for w in warns: print("WARN  " + w)
        print("-" * 60)
        print("PASS: on canon." if not fails else f"{len(fails)} failure(s). Fix and run again.")
    sys.exit(0 if not fails else 1)

if __name__ == "__main__":
    main()
