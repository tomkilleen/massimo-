---
name: massimo-packaging
description: Design packaging graphics, labels, bags and box artwork with dielines in the style of Massimo and Lella Vignelli (Bloomingdale's bags, Knoll, The Vignelli Canon): one typeface, literal naming, material colour as identity, strict panel grid. Use for Vignelli, Swiss or modernist packaging, labels, carton artwork and dielines.
---

# Massimo Packaging

Packaging graphics after the Vignellis' Bloomingdale's bags and their identity work: plain material, literal names, one typeface, the grid carried across every panel.

## Read first
- `references/canon.md`: rules, slop test, intentional test.
- `references/reference-works.md`: Bloomingdale's Brown Bags, Knoll International Graphics, NPS Unigrid (a family of formats from one system).
- `references/DESIGN.md`: colours and type.

## Be clear about the limits
- This skill produces **graphic artwork laid out on a dieline**, as a design proposal. A structural dieline must be confirmed by the printer or a packaging engineer for the actual board, caliper and machine before print.
- Legal text (ingredients, allergens, net quantity, barcodes, recycling marks, regulatory symbols) must come from the client. Never invent it. Leave clearly marked placeholders with the required minimum sizes for the market if the content is missing.

## Brief (write it first)
- Product, range and the one thing the pack must say.
- Format: tuck-end carton, sleeve, label, bag or pouch, with dimensions in mm (L × W × D).
- Material and finish: kraft, white board, uncoated. The material can be the identity, as kraft brown was for Bloomingdale's.
- Range: how many variants, and what changes between them (one colour? one word?).
- Typeface: one family. Helvetica unless the brand dictates otherwise.

## Rules
1. **Literal naming.** Say what it is: "Earl Grey. 20 bags." Plain words carry the identity, as "Big Brown Bag" did.
2. **One typeface, two sizes** for the brand content, plus the legally required sizes.
3. **One panel grid.** Choose a module and apply it to every panel so text and edges line up across folds. The front panel holds the name, set large and flush left; one panel holds all legal content in a tidy table.
4. **Colour as identifier across the range.** One constant (black type, kraft) plus one variable per variant (a single colour band, a single word). Identity and diversity: the system stays fixed; one element changes.
5. **Flush left. No illustrations, no badges, no starbursts, no "NEW", no script faces.**
6. **Bands and rules.** A band can wrap round the pack across panels. Rules: 2pt and ½pt.

## Build
- Draw the flat net as SVG in millimetres (`viewBox` in mm, `width="…mm"`). Layers as groups with ids:
  - `cut`: solid lines, 0.25 pt, magenta (#FF00FF), not printed.
  - `fold`: dashed lines, 0.25 pt, cyan (#00AEEF), not printed.
  - `bleed`: 3 mm outside cut lines, artwork extends to it.
  - `safe`: 3 mm inside cut and fold lines; keep type inside.
  - `art`: the printed design.
- Label each panel (front, back, sides, top, bottom, glue flap) outside the artwork in the dieline colour.
- Make a flat preview (art only, trimmed) and the dieline view (art plus cut and fold layers) as PNGs.
- Note colours: RGB for proof; specify Pantone or CMYK with the printer.

## Check
1. `python3 scripts/massimo_check.py dieline.html --mode packaging`. Fix every FAIL.
2. Check every panel's type is inside the safe area and every front-panel element lines up with the panel grid.
3. Range test: mock two variants side by side. Is the family obvious, and the difference instant?
4. Answer the slop and intentional tests in `references/canon.md`.
5. Compare with the Bloomingdale's bags: is it that plain, and that confident?

Deliver: the SVG dieline with layers, the PNG previews, a short spec (format, dimensions, material, colours, typeface), and a list of content still needed from the client.
