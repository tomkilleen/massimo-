---
name: massimo-ui
description: Design, audit or convert websites, apps and dashboards in the raw modernist style of Massimo and Lella Vignelli (The Vignelli Canon). Use when asked for a Vignelli, Swiss, modernist or International Typographic Style interface, to apply the Vignelli DESIGN.md, or to audit or convert an existing UI to the canon.
---

# Massimo UI

Interfaces built the way the Vignellis built printed matter: one grid, a black identification band, two typefaces at most, three sizes per screen, colour as signifier, structure from rules. Raw look over interface convention.

## Read first

1. `references/DESIGN.md`: the system. Tokens are normative. Every value you use comes from here.
2. `references/canon.md`: the rules, the slop test and the intentional test.
3. `references/reference-works.md`: the benchmarks. Read the entries for the Unigrid, The Herald and the NYCTA manual before any layout work.

## Setup in a project

1. Copy `references/DESIGN.md` to the project root as `DESIGN.md`. If the project already has one, ask before replacing it; if unattended, write `DESIGN.massimo.md` and say so.
2. Copy `references/tokens.css` into the styles folder and import it once, globally. For Tailwind, map the tokens into `theme.extend` (colours, fontSize, spacing) and set `borderRadius` to `{ none: '0' }` only.
3. If Impeccable is installed (`.impeccable/` or `/impeccable` available), its commands read DESIGN.md automatically. Use `/impeccable audit`, `/impeccable polish` and `/impeccable typeset` as normal. Its anti-pattern detector may flag deliberate Vignelli choices (a Bodoni display face, numbered sequence labels, a heavy black band). Where DESIGN.md calls a choice intended, keep it and add it to Impeccable's ignores rather than removing it.

## Modes

### New screen or product
1. **Semantics first.** Write three lines: who uses this, what the screen is for, what the one most important thing on it is.
2. **Choose the system.** Typefaces (default Helvetica only), the grid (12 × 24px), which three sizes this screen uses, what red marks.
3. **Compose.** Band at top. Content in horizontal bands on the grid. One dominant element (a figure, a headline or a table). Leave columns empty.
4. **Build** with tokens only. No new values.
5. **Check** (below).

### Audit an existing UI
1. Run `python3 scripts/massimo_check.py <url-or-file> --mode ui` against the running app or a built page. Install Playwright if missing: `pip install playwright && python3 -m playwright install chromium`.
2. Read the code too: count font-family declarations, font sizes, radius, shadows, colours, spacing values off the 6/12/24px module.
3. Report as a list grouped by canon rule, each with the file and line, what breaks the rule, and the reference work that shows the right way. Lead with a one-line verdict: how far the product is from the canon.

### Convert an existing UI
Work in this order, committing after each step so it can be reviewed:
1. **Tokens.** Add tokens.css (or the Tailwind mapping). Replace every colour, size, spacing, radius and shadow value with a token. Delete what has no token: shadows, radii, gradients.
2. **Shell.** Replace the header with the black identification band. Put the layout on the 12-column grid with 24px margins and gutters.
3. **Type.** Collapse to two families and the five-size scale. Map each old size to the nearest token. On each screen, cut to three sizes.
4. **Components.** Convert cards to rule-separated bands. Convert pill buttons to square blocks or underlined words. Convert inputs to label + underline. Convert status colours to quiet text plus one red block. Remove decorative icons.
5. **Screens.** Go screen by screen. For each, name the one dominant element and remove anything competing with it.
6. Run the checker after every screen.

## Raw mode: what to give up

This system chooses the Vignelli look over common interface conventions. Unless the user says otherwise:
- No cards, panels with shadows or rounded containers. Group with rules and white space.
- No icons except arrows (→ ←) set in the text face. Labels are words.
- Buttons are words: an ink block with an uppercase label, or underlined text.
- No hover animations; colour changes instantly.
- Navigation is words in the band.
- Status is text; only the one urgent state is red.
- Dense tables over chart widgets where a table answers the question.
Keep: visible focus (red outline), readable contrast, real labels on inputs, keyboard access. These are part of the discipline, not convention.

## Check before delivering

1. Run `scripts/massimo_check.py`. Fix every FAIL.
2. Take a screenshot and look at it. Answer the intentional test and the slop test in `references/canon.md`, honestly, in a short list.
3. Compare with the closest reference work. Would it sit beside the Unigrid or The Herald without embarrassment?
4. If it looks like a template, a generic SaaS dashboard, or any product with the name swapped, it is not done. Push scale contrast harder, remove more, and use the band and rules more forcefully.

Report: what was built or changed, the checker result, and the three biggest remaining departures from the canon, if any.
