# YouTube Channel Slide Deck Brand Spec

Extracted from `channel_slide_brand.pptx` (21 slides, Aug 2026).

## Slide Dimensions
- **13.33 × 7.50 inches** (standard 16:9 widescreen)
- All measurements in EMU (914400 EMU = 1 inch)

## Color Palette

| Token | Hex | Usage |
|---|---|---|
| `brand` | `#6D5DF6` | Primary purple — accents, bars, icons, active states, kickers, links |
| `brand-light` | `#8B7DF9` | Lighter purple — arrows, connecting elements |
| `ink` | `#19172E` | Near-black — titles, primary text, bold labels |
| `body` | `#5C5A75` | Muted purple-gray — subtitles, descriptions, body text |
| `meta` | `#A3A0BC` | Light purple-gray — footers, captions, slide numbers |
| `tint-1` | `#EFEBFF` | Very light purple — pill backgrounds, icon backgrounds, inactive number circles |
| `tint-2` | `#F4F1FF` | Light purple — panel backgrounds |
| `tint-3` | `#DCD5FF` | Very light lavender — watermark numbers |
| `tint-4` | `#E4E0FF` | Light purple — white-on-purple subtext |
| `white` | `#FFFFFF` | Cards, chip backgrounds, text on purple |

## Typography

| Font | Role | Sizes |
|---|---|---|
| **MiSans** | Structural — kickers, labels, number badges, panel titles, pills, captions, banner text, goal-pills | 9.5pt, 10pt, 10.5pt, 11pt, 11.5pt, 12pt, 12.5pt, 13pt, 15pt, 15.5pt, 17pt, 56pt, 100pt (watermark) |
| **Inter** | Content — slide titles, subtitles, body paragraphs, footers | 11pt, 13.5pt, 15pt, 33pt |

### Font Rules
- **Slide titles**: Inter 33pt bold, `#19172E`
- **Slide subtitles/body**: Inter 15pt, `#5C5A75` (inline bold spans in `#19172E`)
- **Kickers/section labels**: MiSans 12pt bold, `#6D5DF6` (e.g., "INTRO", "01", "THE PLAN")
- **Number badges**: MiSans 13pt bold, white on `#6D5DF6` (active) or `#6D5DF6` on `#EFEBFF` (inactive)
- **Panel titles**: MiSans 17pt bold, `#19172E`
- **Panel subtitles**: MiSans 11.5pt, `#5C5A75`
- **Footer**: Inter 11pt, `#A3A0BC`
- **Watermark numbers**: MiSans 100pt bold, `#DCD5FF`

## Layout Templates

### Layout 1: Title Slide
```
┌──────────────────────────────────────────┐
│ [pill: brand badge]                      │
│                                          │
│ LARGE TITLE (56pt)                       │  ← right panel with
│ second line in brand purple              │     3 chips (icon + text)
│                                          │
│ Subtitle (15pt, body gray)               │
│                                          │
│ footnote (11pt, meta)                    │
└──────────────────────────────────────────┘
```
- Left content area: x=0.89", width=~7.2"
- Right panel: x=8.33", bg=#F4F1FF, with white chip cards

### Layout 2: Content Slide (Kicker + Title + Body)
```
┌──────────────────────────────────────────┐
│ │KICKER                                   │
│ │Slide Title (33pt bold)                  │  ← right panel with
│ │                                         │     watermark number (100pt)
│ │Subtitle/body text (15pt)                │     + icon + caption
│ │                                         │
│ │[optional goal-pill]                     │
│ │                                         │
│ footer                          XX / XX  │
└──────────────────────────────────────────┘
```
- Vertical accent bar: x=0.89", width=0.097", bg=#6D5DF6
- Content starts at x=1.28"
- Right panel: x=8.88", bg=#F4F1FF

### Layout 3: Grid/Plan Slide
```
┌──────────────────────────────────────────┐
│ KICKER                                    │
│ Slide Title (33pt bold)                   │
│ Subtitle (13.5pt)                         │
│                                           │
│ [card1] [card2] [card3] [card4]           │
│ [card5] [card6] [card7] [card8]           │
│                                           │
│ note line (11pt, meta)                    │
│ ┌─────── full-width banner ──────────┐   │
│ │ icon  Banner text (15.5pt white)   │   │
│ └────────────────────────────────────┘   │
│ footer                          XX / XX  │
└──────────────────────────────────────────┘
```
- Grid cards: white bg, numbered badges (active=purple fill, inactive=tint-1 fill)
- 4 cards per row, each ~2.64" wide × 0.92" tall
- Banner: full width, #6D5DF6 bg, white text, optional tag pill on right

## Recurring Elements

### Footer (every slide except title)
- Bottom-left: series name (e.g., "8 /learn Superpowers"), Inter 11pt, `#A3A0BC`
- Bottom-right: slide number "XX / XX", Inter 11pt, `#A3A0BC`
- Position: y=7.02" (6426200 EMU)

### Vertical Accent Bar
- Width: 88900 EMU (~0.097")
- Color: `#6D5DF6`
- Used on content slides to anchor the left margin

### Number Badges
- Size: 381000 × 381000 EMU (0.42" × 0.42")
- Active: `#6D5DF6` fill, white MiSans 13pt bold
- Inactive: `#EFEBFF` fill, `#6D5DF6` MiSans 13pt bold

### Goal Pill
- Rounded rectangle, `#EFEBFF` fill, `#6D5DF6` MiSans 11pt bold text
- Pattern: "→ continues with /goal"

### Chips (title slide right panel)
- White rounded rectangles
- Icon (28-30px) on left, two-line text on right (bold title + muted subtitle)
- Active chip: `#6D5DF6` fill, white text
- Arrow between chips: `#8B7DF9`

### Panel (content slide right side)
- `#F4F1FF` background
- Oversized watermark number: MiSans 100pt bold, `#DCD5FF`
- Centered icon: `#6D5DF6`
- Bottom caption: MiSans 11pt, `#5C5A75`
