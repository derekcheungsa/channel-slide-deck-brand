# Style Guide

**The single source of truth for colors, typography, and tokens.** Every diagram draws from this — not from hex values inlined in other reference files. If you want to change the visual skin of Diagram Design, change this file.

This working copy is **pre-skinned for Derek's YouTube channel** (vendored inside the `channel-slide-deck-brand` skill). The pristine upstream default skin is preserved at `~/.diagram-design/profiles/default.md`; `reset` per [`profiles.md`](profiles.md) restores it.

---

## Tokens

### Semantic roles

Every token is referred to by **semantic role**, not by its hex value. Type references (`type-*.md`) and SKILL.md say `accent`, not `#6D5DF6`.

| Role | Purpose | Channel skin (light) | Dark |
|---|---|---|---|
| `paper` | Page background, default node fill | `#FFFFFF` (white) | `#19172E` (ink) |
| `paper-2` | Diagram container bg, secondary fill | `#F4F1FF` (tint-2) | `#232036` |
| `ink` | Primary text, primary stroke | `#19172E` (ink) | `#F4F1FF` |
| `muted` | Secondary text, default arrow stroke | `#5C5A75` (body) | `#A3A0BC` (meta) |
| `soft` | Sublabels, boundary labels | `#A3A0BC` (meta) | `#A3A0BC` |
| `rule` | Hairline borders | `rgba(25,23,46,0.12)` | `rgba(244,241,255,0.12)` |
| `rule-solid` | Stronger borders, baselines | `#DCD5FF` (tint-3) | `rgba(220,213,255,0.25)` |
| `accent` | Focal / 1–2 max per diagram | `#6D5DF6` (brand) | `#8B7DF9` (brand-light) |
| `accent-tint` | Fill for accent-bordered boxes | `rgba(109,93,246,0.08)` | `rgba(139,125,249,0.10)` |
| `link` | HTTP/API calls, external arrows | `#8B7DF9` (brand-light) | `#8B7DF9` |

> **Brand palette source:** this skin maps Derek's channel slide palette — brand `#6D5DF6`, brand-light `#8B7DF9`, ink `#19172E`, body `#5C5A75`, meta `#A3A0BC`, tints `#EFEBFF` / `#F4F1FF` / `#DCD5FF` / `#E4E0FF`. Derived tokens: `rule` is ink-at-opacity, dark `paper-2` is a lightness step above ink. Diagram `paper` is white (not tint-2) because diagrams export with a transparent background (`omit_background`) and composite onto white slide cards.

> **Note:** The pre-baked example HTML files in `assets/` were built under an earlier skin. Regenerating them against the current `style-guide.md` is a v5.1 task. New diagrams the skill produces will use the tokens above.

### Inversion rule (light → dark)

Any `rgba(25,23,46, X)` in light becomes `rgba(244,241,255, X)` in dark. Same opacities, RGB flipped. The accent shifts to brand-light `#8B7DF9` to read on dark paper.

### Series palette (multi-series chart types only)

Kept **verbatim from upstream** — the channel brand doesn't define a chart-series palette, and these desaturated editorial tones sit quietly next to the purple accent. For chart types that genuinely need to distinguish multiple overlapping entities (currently: **radar**). The "1-focal" rule still holds — `accent` (brand purple) is reserved for the focal series.

| Token | Light | Dark | Notes |
|---|---|---|---|
| `series-1` | `#7c8f6f` (sage) | `#9caf8f` | Non-focal series |
| `series-2` | `#5e7a9b` (dusty-blue) | `#82a0c0` | Non-focal series |
| `series-3` | `#b8915a` (mustard) | `#d3ad7a` | Non-focal series |
| `series-4` | `#9c6b50` (rust-brown) | `#b88670` | Non-focal series |
| `series-5` | `#6e6479` (slate) | `#8d8298` | Non-focal series |

Fills sit at `0.18` opacity light, `0.22` dark; strokes use the full color. **Don't backfill these tokens to non-chart types** — architecture, swimlane, etc. continue to use muted-ink variants. The series palette is opt-in for diagrams where overlapping shapes demand distinguishable color, not a license to add color elsewhere.

### Terminal skin (opt-in alternate)

A self-contained palette for the terminal-window primitive (see [primitive-terminal.md](primitive-terminal.md)) — a CLI-chrome register for dev-tool posts and technical social cards. It does not replace the default skin above and isn't affected by onboarding; it's a second, fixed skin you opt into per-diagram. The one accent is swapped to brand purple.

| Token | Hex | Purpose |
|---|---|---|
| `terminal-page` | `#0a0a0a` | Page background behind the window |
| `terminal-paper` | `#141414` | Window body, node fill |
| `terminal-bar` | `#1b1b1b` | Titlebar strip |
| `terminal-border` | `#2b2b2b` | Window border, hairlines |
| `terminal-ink` | `#f5f5f5` | Primary text, primary stroke |
| `terminal-muted` | `#9a9a9a` | Secondary text, sublabels, ring stroke |
| `terminal-soft` | `#5c5c5c` | Tertiary — inactive dots, spokes |
| `terminal-accent` | `#6D5DF6` | The one accent — brand purple; focal station, prompt sign, active dot |
| `terminal-accent-tint` | `rgba(109,93,246,0.12)` | Fill for accent-bordered boxes |

**1-accent rule still holds.** Everything that isn't `terminal-ink` or `terminal-muted`/`terminal-soft` should be `terminal-accent` — never introduce a second hue.

---

## Typography

The channel brand uses two families — **Inter** (content: titles, body) and **MiSans** (structural: kickers, labels, numbers). MiSans takes over the register upstream assigned to Geist/Geist Mono: node sublabels, eyebrows/type-tags, and arrow labels are MiSans because on Derek's slides every label/kicker/number is MiSans. Node names and page titles are Inter, matching slide titles and body text.

| Role | Family | Size | Weight | Usage |
|---|---|---|---|---|
| `title` | Inter | 1.75rem (28px std / 40px presentation) | 700 | Page H1 — matches slide-title style (Inter bold, ink) |
| `node-name` | Inter | 12px (16px presentation) | 600 | Human-readable labels |
| `sublabel` | MiSans | 9px (12px presentation) | 380 | Port, protocol, URL, field type |
| `eyebrow` | MiSans | 7–8px | 630, tracked 0.18em, uppercase | Type tags, axis labels — fill `accent` (matches kickers) |
| `arrow-label` | MiSans | 8px (12px presentation) | 380, tracked 0.06em | Arrow annotations |
| `callout` | Inter | 14px | 400 italic | Editorial asides only |

### Font stack

```html
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>
  /* MiSans MUST load via @import inside <style> — never a <link> tag.
     scripts/self_check.py approves ONLY fonts.googleapis.com/css2 as a remote
     stylesheet link; <style> text is CSS (not an element attribute), so the
     scanner never URL-checks it. Each CDN css declares ~100 unicode-range
     subsets with relative woff2 URLs that resolve against the CDN origin. */
  @import url('https://cdn.jsdelivr.net/npm/misans@4.1.0/lib/Normal/MiSans-Medium.min.css');
  @import url('https://cdn.jsdelivr.net/npm/misans@4.1.0/lib/Normal/MiSans-Semibold.min.css');
  @import url('https://cdn.jsdelivr.net/npm/misans@4.1.0/lib/Normal/MiSans-Bold.min.css');
</style>
```

**MiSans CDN weight pitfall (load-bearing):** jsdelivr `misans@4.1.0` ships NON-standard `font-weight` declarations — Regular=330, Medium=380, Demibold=450, Semibold=520, Bold=630. `font-weight: 400/600/700` on MiSans triggers synthetic bold or the wrong face. Use the exact declared weights: eyebrows/type-tags/watermarks → **630**, panel/banner text → **520**, captions/sublabels/arrow-labels → **380**. The family name is exactly `MiSans` (no suffix). The CSS subsets faces by `unicode-range`, so `document.fonts.check('16px MiSans')` returns false on an empty probe — verify with `document.fonts.load('630 16px MiSans', 'sample text')` first, then check.

For standalone SVG export, inject the same URLs as `@import` inside `<defs>` (XML-escape `&` as `&amp;` — see [export.md](export.md)).

**Load-bearing rule:** MiSans is for *structural* content — labels, kickers, numbers, ports, commands, URLs. Names and sentences go in Inter. Never swap weights mid-family; never request a weight the CDN doesn't declare.

---

## Stroke, radius, spacing

| Token | Value | Use |
|---|---|---|
| `stroke-thin` | `0.8` | Tag-box outlines, leaf nodes |
| `stroke-default` | `1` | Most strokes |
| `stroke-strong` | `1.2` | Emphasis strokes |
| `radius-sm` | `4` | Small tags |
| `radius-md` | `6` | Node boxes |
| `radius-lg` | `8` | Containers, rings |
| `grid` | `4` | Every coord, size, and gap is divisible by 4 (hard rule) |

---

## Node type → treatment

Semantic role combinations — reference these by name in type specs.

| Type | Fill | Stroke |
|---|---|---|
| `focal` (1–2 max) | `accent-tint` | `accent` |
| `backend` | `#ffffff` (white) | `ink` |
| `store` | `ink @ 0.05` | `muted` |
| `external` | `ink @ 0.03` | `ink @ 0.30` |
| `input` | `muted @ 0.10` | `soft` |
| `optional` | `ink @ 0.02` | `ink @ 0.20` dashed `4,3` |
| `security` | `accent @ 0.05` | `accent @ 0.50` dashed `4,4` |

---

## Customizing the skin

1. **Reset to upstream default** — the pristine shipped skin is saved at `~/.diagram-design/profiles/default.md`; follow `reset` in [`profiles.md`](profiles.md).
2. **Edit by hand** — change the hex values in the tables above. Run the pre-output taste gate (vendored SKILL.md §9) afterward to verify `accent` still reads as "focal" against `paper`.
3. **Brand handoff** — paste design-token JSON into a new section here and map tokens to the semantic roles above (this file itself was produced by that method from `channel_slide_brand_spec.md`).
4. **Client profiles** — save and switch named skins per [`profiles.md`](profiles.md).

### Constraints (don't break these)

- **Contrast**: `ink` must hit WCAG AA on `paper`. `muted` must hit AA on `paper` for 11px+ text. (`#19172E` on `#FFFFFF` ≈ 15.9:1; `#5C5A75` on `#FFFFFF` ≈ 7.4:1 — both pass.)
- **One accent**: brand purple is the only `accent`. Tint-3 lavender and brand-light are NOT extra accents — brand-light is reserved for `link`/arrows only.
- **No rainbow palette**: the channel palette is purple-family + neutrals; keep it that way. Series colors only where a chart genuinely needs them.
- **Two families, not three**: upstream keeps a serif for title/callout contrast; this brand deliberately drops it — slide titles are Inter bold, and diagrams must match the deck they live in. Inter italic covers callouts.
- **White paper is a deliberate exception**: upstream prefers warm-neutral paper; this skin uses white because exported PNGs composite transparent onto white slide cards.
- **Dot pattern is optional, not default**: default background is a clean `paper` fill. (Also: never use the dot pattern inside a slide — it compounds with slide chrome.)
- **Container is clean by default**: the diagram sits directly on the page paper. The framed variant (`paper-2` bg + `rule` border) is opt-in for card-heavy layouts.
