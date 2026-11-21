---
name: massimo-poster
description: Design posters, flyers, announcements and covers in the style of Massimo and Lella Vignelli (The Vignelli Canon): strict grid, Helvetica or Bodoni, two sizes, black band, type as image, primary colour. Use for a Vignelli, Swiss, modernist or International Typographic Style poster or print piece.
---

# Massimo Poster

Posters the way the Vignellis made them for Knoll and the Institute for Architecture and Urban Studies: the name or idea set so large it becomes the image, a strict grid, a heavy band, two sizes, flush left, a lot of empty space.

## Read first
- `references/canon.md`: rules, slop test, intentional test.
- `references/reference-works.md`: Knoll International Graphics, Institute for Architecture and Urban Studies, Stendig Calendar, NPS Unigrid.
- `references/DESIGN.md`: colours and typefaces (sizes on a poster follow this skill, not the screen scale).

## Brief (write it before designing)
- Subject and the single message.
- Audience and where it hangs (distance it is read from).
- Size: default A2 (420 × 594 mm). Alternatives: A1 (594 × 841), A3 (297 × 420), 50 × 70 cm, 70 × 100 cm.
- Grid: choose columns × modules and state it, e.g. 4 × 8, 6 × 6, 3 × 6. Margins: narrow (tension) by default, 10–15 mm on A2.
- Typefaces: Helvetica alone, or Bodoni alone, or Helvetica with Bodoni. Never more.
- Colour: black and white, plus at most one of red, blue or yellow, and say what it signifies.

## Composition rules
1. **Two sizes.** One display size and one text size. A third, small size only for unavoidable fine print (credits, legal), at the text size or smaller.
2. **Type as image.** The display element is the picture: the name, a number, a word, set at a scale that fills one or more full grid modules. Overlap, crop or bleed it off the edge if the meaning survives; Vignelli did this for Knoll because the name was already known.
3. **The band.** A black band across the top or bottom carrying the issuer and the date is the default structure, as on the IAUS posters. Information rows can sit under it, divided by 2pt and ½pt rules.
4. **Flush left, ragged right.** Nothing centred.
5. **Empty space.** At least a third of the poster stays empty, and the emptiness is shaped by the grid.
6. **Every element sits on the grid.** Text tops hang from module lines; columns start on column lines.
7. **No images unless the brief requires one.** If it does, crop it to whole grid modules, full bleed or square-cut, no rounded corners, no frames.

## Build
- Build as one HTML file with a fixed page size using CSS `@page { size: 420mm 594mm; margin: 0 }`, a container sized in mm and the grid as CSS grid in mm. Or as SVG with a `viewBox` in mm.
- Include 3 mm bleed when the design bleeds: make the artboard 426 × 600 mm and mark the trim in a separate, hidden layer.
- Export a PDF with Playwright: `page.pdf(path=..., width='420mm', height='594mm', print_background=True)`. Export a PNG preview at 1600 px tall.
- Fonts: embed or link; check the PDF has the real face, not a fallback.
- Note in the handover: colours are RGB for screen proof; the printer converts to CMYK or matches spot colours (suggest Pantone Warm Red or 485 for the red).

## Check
1. `python3 scripts/massimo_check.py poster.html --mode poster`. Fix every FAIL.
2. Look at the PNG at thumbnail size. From across a room, is there one clear idea? If two things compete, make one smaller.
3. Answer the slop test and intentional test in `references/canon.md`.
4. Put it beside the Knoll poster and the IAUS posters in your mind. Is it as forceful and as empty?
5. If it looks like a template event poster (centred title, photo behind, badge for the date), start again.

Deliver: the HTML or SVG source, the PDF, the PNG preview, and three lines naming the grid, the sizes and what the colour means.
