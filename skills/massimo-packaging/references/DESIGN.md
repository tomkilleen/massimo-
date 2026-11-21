---
version: alpha
name: Massimo
description: Massimo, a modernist design system after The Vignelli Canon. Derived from The Vignelli Canon and the printed work of Lella and Massimo Vignelli. One grid, few typefaces, few sizes, colour as identifier, structure from rules and bands. Raw and intentional; no decoration.
colors:
  primary: "#111111"
  on-primary: "#FFFFFF"
  neutral: "#FFFFFF"
  on-surface: "#111111"
  secondary: "#5E5E5E"
  hairline: "#D4D4D4"
  wash: "#F2F2F0"
  tertiary: "#E2231A"
  identifier-blue: "#0039A6"
  identifier-yellow: "#FFCC00"
  error: "#E2231A"
typography:
  display:
    fontFamily: Helvetica Neue
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -0.02em
  headline:
    fontFamily: Helvetica Neue
    fontSize: 32px
    fontWeight: 700
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-serif:
    fontFamily: Libre Bodoni
    fontSize: 32px
    fontWeight: 400
    lineHeight: 36px
  body-md:
    fontFamily: Helvetica Neue
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-strong:
    fontFamily: Helvetica Neue
    fontSize: 16px
    fontWeight: 700
    lineHeight: 24px
  label-sm:
    fontFamily: Helvetica Neue
    fontSize: 12px
    fontWeight: 700
    lineHeight: 16px
    letterSpacing: 0.06em
  figure:
    fontFamily: Helvetica Neue
    fontSize: 128px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -0.03em
    fontFeature: '"tnum" 1'
rounded:
  none: 0px
spacing:
  line: 24px
  half: 12px
  quarter: 6px
  double: 48px
  quad: 96px
  gutter: 24px
  margin: 24px
  band: 48px
  rule-heavy: 2px
  rule-light: 1px
  columns: 12
  max-width: 1440px
components:
  band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    height: 48px
    padding: 12px
    rounded: "{rounded.none}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    padding: 12px
    height: 48px
    rounded: "{rounded.none}"
  button-primary-hover:
    backgroundColor: "{colors.tertiary}"
  button-text:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-sm}"
    padding: 0px
    rounded: "{rounded.none}"
  button-text-hover:
    textColor: "{colors.tertiary}"
  input:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    height: 48px
    padding: 0px
    rounded: "{rounded.none}"
  table-header:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-sm}"
    height: 48px
  table-row:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    height: 48px
  status-attention:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    padding: 6px
    rounded: "{rounded.none}"
  note:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    padding: 12px
    rounded: "{rounded.none}"
  rule-light:
    backgroundColor: "{colors.hairline}"
    height: 1px
  chart-series-key:
    backgroundColor: "{colors.tertiary}"
  chart-series-a:
    backgroundColor: "{colors.identifier-blue}"
  chart-series-b:
    backgroundColor: "{colors.identifier-yellow}"
  input-error:
    textColor: "{colors.error}"
  status-quiet:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.secondary}"
    typography: "{typography.label-sm}"
    padding: 0px
---

# Massimo

## Overview

A system built from the method of Lella and Massimo Vignelli as set out in The Vignelli Canon (2010) and shown in their printed work: the NYCTA Graphics Standards Manual, the National Park Service Unigrid, Knoll International, the Stendig Calendar and The Herald newspaper.

The character is **disciplined, forceful and timeless**. Screens should look like a well-made printed page: one grid, a black identification band, few typefaces, few sizes, generous white space and colour that means something. The layout should almost disappear; if the layout is what you notice, it is weak.

This system deliberately favours the raw Vignelli look over common interface conventions. No cards, no rounded corners, no shadows, no gradients, no icons as decoration, no illustration. Structure comes from the grid, from rules (dividing lines) and from bands. Hierarchy comes from scale contrast and weight, never from colour or ornament.

Every element must have a reason. Before adding anything, ask what it means. If it means nothing, remove it.

**Intangibles to apply on every task:**
- **Semantics:** understand the subject before designing. Every detail has a purpose.
- **Syntactics:** consistency comes from the relationships between grid, type, images and sizes.
- **Pragmatics:** if it needs explaining, it has failed.
- **Discipline:** self-imposed rules, applied to every detail. There is no unimportant detail.
- **Appropriateness:** choose the media, scale and expression the subject needs.
- **Ambiguity:** double meanings are allowed only when controlled.
- **Design is one:** the same discipline for a screen, a poster, a package or a diagram.
- **Visual power:** strength comes from a clear concept, not from loudness.
- **Intellectual elegance:** the opposite of vulgarity. No trends, no tricks.
- **Timelessness:** primary shapes, primary colours, economy.
- **Responsibility:** to the work, the client and the user.
- **Equity:** refresh an existing identity before replacing it.

## Colors

The palette is black, white and one red. Blue and yellow exist only as identifiers for categories.

- **Ink (#111111):** text, rules, the identification band, primary buttons. The dominant colour after white.
- **Paper (#FFFFFF):** the page. Pure white, never cream or beige.
- **Grey (#5E5E5E):** secondary text and metadata only. Never for primary content.
- **Hairline (#D4D4D4):** light rules between rows. Never for text.
- **Wash (#F2F2F0):** a rare flat area to set off one block (a note, a code sample). Use at most once per screen.
- **Vignelli Red (#E2231A):** the single signifier. It marks the one thing that needs attention: the current selection, an alert, an error, the active state, a key figure. On any screen, red should appear in no more than one or two places. Red is never decoration.
- **Identifier Blue (#0039A6) and Identifier Yellow (#FFCC00):** only to tell categories apart, as the subway diagram gives each route a colour: chart series, route lines, category markers. Never for buttons, backgrounds or branding. Yellow is never used for text on white.

Colour is a signifier, never decoration. If you cannot say what a colour means, make it black.

## Typography

Vignelli worked with a handful of typefaces and no more. This system uses **two families at most per project**.

- **Default:** Helvetica only. Use the system stack `"Helvetica Neue", Helvetica, Arial, sans-serif`. Where an open web font is required, use Arimo as a stand-in and say so.
- **Optional serif:** Libre Bodoni (Bodoni) for headlines in editorial or cultural contexts. Set it roman, never italic for display.
- **Other permitted faces (from the Canon):** Garamond (EB Garamond), Century Expanded (no faithful open version; use the system face if present), Futura (Jost), Times Roman (system Times), Caslon (Libre Caslon Text), Baskerville (Libre Baskerville), Univers and Optima (system only). Choose one only if the subject asks for it, and state why.
- **Never:** Inter, Space Grotesk, rounded geometric faces, display novelty faces, monospace as decoration, or any face chosen to look current.

**Sizes.** Use as few as possible. On one screen, use **no more than three sizes** (typically label, body and one headline). Across a whole product, the scale is fixed at five: 12px label, 16px body, 32px headline, 64px display and 128px figure. Each step above body is double the one below, the Canon's contrast of display at about twice the text size. Never introduce a size outside this scale.

**Weights.** 400 and 700 only. A subhead can be body size in bold, with one line of space above and none below.

**Labels.** 12px, bold, uppercase, letter-spaced 0.06em. Used for section names, table headers, buttons and metadata.

**Alignment.** Flush left, ragged right, always. Never justify. Centre nothing on screens. Do not hyphenate.

**Numbers.** Tabular figures wherever numbers align in columns. Large figures (`figure`) are allowed once per screen, for the single most important number.

## Layout

**One grid.** 12 columns, 24px gutters, 24px outer margins, maximum width 1440px. Narrow margins create tension between content and edge; that is intended.

**One module.** The 24px line is the unit. Every margin, padding, gap and height is a multiple of 6px, and preferably of 12px or 24px. Text baselines and blocks align to the 24px line.

**Gutters are tight:** about one line of type (24px).

**Composition:**
- Build screens from horizontal bands of content, as The Herald built pages from bands.
- Use asymmetry: content in columns 1–8 with metadata in 10–12, or a narrow label column (1–3) beside content (4–12), as on a Vignelli letterhead.
- Leave columns empty on purpose. White space is structure, more important than the type.
- Repeat the same structure on every screen. Content provides the variety; the system does not change.

**Density.** Dense information is acceptable and often right; clutter is not. Density with alignment reads as order.

## Elevation & Depth

There is no elevation. No shadows, no blur, no glass, no layered cards, no z-depth illusions.

Hierarchy comes from four things only:
1. **Scale:** a large size against a small one.
2. **Weight:** bold against regular.
3. **Rules:** a 2px ink rule separates major parts; a 1px rule (ink or hairline) separates items within a part. Only these two weights exist. Type hangs from the rule above it.
4. **Bands:** a solid black identification band carries the product or section name at the top of every screen, as on the Unigrid and the subway signs. Band height is 48px (two lines) or a multiple of 24px.

Overlays (menus, dialogs) are flat panels with a 2px ink rule at the top and no shadow. Use a full-screen panel rather than a floating modal where possible.

## Shapes

Everything is rectangular. Corner radius is 0px everywhere: buttons, inputs, images, panels, tags. Circles are allowed only where they carry meaning, such as a stop on a route diagram or a data point.

No pills, no rounded avatars, no rounded cards, no blobs.

## Components

Components are minimal and typographic. Raw over conventional.

- **Identification band:** full width, ink background, white label-sm text, 48px tall. Left: product or section name. Right: navigation as words, separated by space, not dividers. The current item is red.
- **Buttons:** words, not shapes. Primary: ink block, white uppercase label, square corners, turns red on hover. Secondary: label text with a 2px underline rule; turns red on hover. No icons in buttons. No ghost outlines with rounded corners.
- **Inputs:** no box. A label above (label-sm), the value in body-md, a 1px ink rule below. Focus turns the rule red and 2px. Error: red rule plus a red label stating the problem in words.
- **Tables:** the primary pattern for data. Header row in label-sm with a 2px ink rule below; rows separated by 1px hairlines; text flush left, numbers flush right with tabular figures. No zebra striping, no row shading, no boxed cells.
- **Status:** state is text. Normal states are quiet grey labels. The one state needing attention is a red block with white uppercase label. Never use green/amber/red traffic lights; use words and the single red.
- **Navigation:** words in the band, or a list in a narrow left column. No icon rails, no hamburger menus on desktop.
- **Figures:** one large number, label above it, unit beside it in label-sm. No tile backgrounds.
- **Charts:** lines and bars in ink; categories in identifier colours; red only for the series or point that matters. Label directly at the end of lines rather than in a legend. Axes as hairlines. No gridline clutter, no 3D, no gradients, no donut charts.
- **Focus:** a 2px red outline, offset 2px. Keep it; it is part of the system.

## Do's and Don'ts

- Do start every screen with the black identification band and one 12-column grid.
- Do use at most two typefaces in a project and at most three sizes on a screen.
- Do keep every spacing value on the 6px/12px/24px module.
- Do use exactly two rule weights: 2px between parts, 1px within.
- Do set all text flush left, ragged right.
- Do use red only for the one thing that needs attention.
- Do let scale contrast carry hierarchy: one very large element against small labels.
- Do leave columns empty on purpose.
- Do name things literally: "Little, Medium, Big", not clever labels.
- Don't use rounded corners, shadows, gradients, blur, glass or transparency effects.
- Don't use cards. Group content with rules, bands and white space.
- Don't use icons as decoration, icon tiles, emoji or illustrations.
- Don't centre text, hero sections or layouts.
- Don't use cream, beige, pastel or purple palettes, or any colour without a meaning.
- Don't use Inter, Space Grotesk or any typeface chosen to look modern.
- Don't add eyebrow chips, badges, pills, "new" tags, sparkles or pulsing dots.
- Don't justify text or use italic serif display type.
- Don't add motion beyond instant colour changes on hover and focus.
- Don't invent sizes, colours or spacing outside these tokens.
- Don't make it look like a template. If it could be any product, it is wrong.
