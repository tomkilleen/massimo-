---
name: massimo-infographic
description: Design infographics, diagrams, maps, charts and data graphics in the style of Massimo Vignelli's 1972 New York subway diagram and his information design: lines at 45° and 90°, one colour per category, direct labels, Helvetica, strict grid. Use for Vignelli, Swiss or modernist information graphics, process diagrams, route maps and explanatory charts.
---

# Massimo Infographic

Information design after the 1972 New York subway diagram and the NYCTA manual: abstraction in service of understanding, colour that identifies, one geometry, no decoration.

## Read first
- `references/canon.md`: rules, slop test, intentional test.
- `references/reference-works.md`: New York City Subway Diagram, NYCTA Graphics Standards Manual, The Herald.
- `references/DESIGN.md`: colours (identifier blue and yellow are for categories here) and type.

## Accuracy comes first
- Use only data the user gave you or a source you cite. Never invent figures. If an example needs placeholder data, label it "Sample data" on the graphic.
- Every graphic carries a source line and a date in the text size.
- Keep proportions honest: bar lengths and areas are proportional to values; axes start at zero for bars.
- Abstraction must not mislead. Vignelli's diagram was criticised because it broke riders' sense of geography and shipped without its companion map. When abstracting something people also know literally, say so, or pair it with a literal view.

## Rules
1. **One geometry.** Lines run at 0°, 45° and 90° only. Corners are tight radii only where a line turns, or sharp. Nodes are circles (stops) or squares (data points), all one size.
2. **Colour identifies.** One colour per category, used everywhere that category appears. Black is the default; red marks the one thing that matters most; blue and yellow, and if needed more category colours chosen from the subway palette, identify the rest. No colour without a meaning. No more than six category colours.
3. **Label directly.** Put labels at the end of a line or next to the mark. Avoid legends; if one is unavoidable, it is a simple list aligned to the grid.
4. **Two sizes, one face.** Helvetica; a label size and one heading size; tabular figures.
5. **Grid.** Plot area and labels sit on one grid; label columns align. Every node is on a grid intersection.
6. **No chart junk.** No 3D, shadows, gradients, pictograms as decoration, donut charts, dense gridlines or borders around the plot. Axes are hairlines or are omitted where direct labels do the work.
7. **Title says the finding,** not the topic: "Night-time load is a third of daytime", not "Energy use".

## Build
- SVG, with a `viewBox` on a grid unit (e.g. 24 units). Lines `stroke-linecap="butt"`, `stroke-linejoin="miter"` (or round only for route lines), stroke widths from a fixed set (e.g. 2, 6, 12).
- Text in SVG uses the same font stack as DESIGN.md. Embed it in an HTML page for preview.
- For charts from real data, compute positions in code from the data; never hand-place bars.
- Export: the SVG, a PNG at 2×, and a PDF if it is for print.

## Check
1. `python3 scripts/massimo_check.py diagram.html --mode infographic`. Fix every FAIL.
2. Check every number and label against the source.
3. Can a newcomer read it without explanation (pragmatics)? Ask: what does a reader learn in five seconds?
4. Answer the slop and intentional tests in `references/canon.md`.
5. Compare with the 1972 diagram. Is it as calm, as consistent in angle, as disciplined in colour?

Deliver the files, the source line, and three lines naming the geometry, the colour key and the main finding.
