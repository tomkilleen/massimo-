# Massimo

**Design skills after The Vignelli Canon.**

A design system and four skills that make AI agents design the way Lella and Massimo Vignelli designed: one grid, few typefaces, few sizes, colour that means something, structure from rules and bands. One canon, four media.

| Skill | Makes |
|---|---|
| `massimo-ui` | Websites, apps and dashboards. Audits and converts existing UIs. |
| `massimo-poster` | Posters, flyers, covers. HTML or SVG to PDF at A-series sizes. |
| `massimo-infographic` | Diagrams, route maps, charts. SVG. |
| `massimo-packaging` | Carton and label artwork on a layered SVG dieline. |

All four share one core:

- `DESIGN.md`: the system in the open DESIGN.md format (Google Stitch spec). Tokens for colour, type, spacing and components, plus the canon as Do's and Don'ts. Passes `npx @google/design.md lint` with no errors or warnings.
- `canon.md`: the canon's rules as a print-to-screen table, the twelve intangibles as review questions, a slop test and an intentional test.
- `reference-works.md`: ten printed works as benchmarks, each broken into graphic elements.
- `tokens.css`: the tokens as CSS variables and a few base classes.
- `massimo_check.py`: renders a page in headless Chromium and measures it against the canon (typefaces, sizes, rules, radius, shadows, gradients, alignment, palette, spacing module, and the font the machine actually rendered).

## Install

**Fastest, any agent:** copy `DESIGN.md` to your project root. Any agent that reads DESIGN.md (Impeccable, Stitch, or a plain coding agent told to follow it) will design to the canon.

**Claude Code plugin:** download this folder, then in Claude Code:

```
/plugin marketplace add tomkilleen/massimo-
/plugin install massimo@massimo
```

**Skills only:** copy the folders in `skills/` into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project).

**With Impeccable** (recommended for UI): `npx impeccable install`, then put `DESIGN.md` in the project root. Impeccable's audit, polish and craft commands follow it automatically.

The checker needs Playwright once: `pip install playwright && python3 -m playwright install chromium`.

## Use

- "Audit this app against the Vignelli canon."
- "Convert the dashboard to the Vignelli system, one screen at a time."
- "Make an A2 poster for our lecture series in the Vignelli style."
- "Draw our onboarding flow as a Vignelli route diagram."
- "Design a carton for our coffee range, Vignelli style, 80 × 80 × 160 mm."

## Fonts

Helvetica is used where installed. Elsewhere the open stand-in is Arimo; Libre Bodoni stands in for Bodoni. `core/fonts.css` declares a "Massimo Sans" face that prefers local Helvetica and falls back to Arimo, so machines cannot silently swap in another face. The checker reports the face actually rendered.

## Examples

`examples/` holds one piece made with each skill, all passing the checker: a building energy dashboard, an A2 poster, a system diagram and a tea carton dieline with range.

## Develop

Edit files in `core/`, then run `python3 build.py` to copy them into every skill.

## Credits

After The Vignelli Canon by Massimo Vignelli (Lars Müller Publishers, 2010; free PDF from RIT's Vignelli Center) and the work of Lella and Massimo Vignelli. This project is an independent interpretation and is not affiliated with or endorsed by the Vignelli estate or the Vignelli Center. Arimo and Libre Bodoni are licensed under the SIL Open Font License.
