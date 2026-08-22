---
name: channel-slide-deck-brand
description: "Use when building YouTube slide decks for Derek's channel."
---

# Channel Slide Deck Brand

Derek's YouTube channel uses a consistent slide deck design system. Use this spec whenever building slide decks (PPTX or HTML) for his videos.

## Design System Reference

Full spec file: `C:\Users\derek\autods\channel_slide_brand_spec.md`

### Quick Reference

**Colors:**
- Primary purple: `#6D5DF6`
- Light purple: `#8B7DF9`
- Ink (titles): `#19172E`
- Body text: `#5C5A75`
- Meta/footer: `#A3A0BC`
- Tint backgrounds: `#EFEBFF` (pills/icons), `#F4F1FF` (panels), `#DCD5FF` (watermarks), `#E4E0FF` (subtext on purple)

**Fonts:**
- MiSans — kickers, labels, numbers, panel titles, pills, captions (9.5–56pt)
- Inter — slide titles (33pt bold), subtitles/body (15pt), footers (11pt)

**Slide size:** 13.33 × 7.50 inches (16:9)

**Layout templates:**
1. **Title slide** — left content + right panel with chip cards
2. **Content slide** — vertical accent bar + kicker + title + subtitle + optional right panel with watermark number
3. **Grid/plan slide** — title + card grid + full-width purple banner

**Recurring elements:**
- Footer: series name (bottom-left) + slide number "XX / XX" (bottom-right), Inter 11pt `#A3A0BC`
- Vertical accent bar: `#6D5DF6`, 0.097" wide
- Number badges: 0.42" square, active (purple fill/white text) vs inactive (tint fill/purple text)
- Goal pills: `#EFEBFF` bg, `#6D5DF6` text, "→ continues with /goal" pattern
- Watermark numbers: MiSans 100pt bold, `#DCD5FF`

## How to Use

1. Load the full spec from `C:\Users\derek\autods\channel_slide_brand_spec.md`
2. For PPTX output: use python-pptx, create slides at 13.33×7.50", apply colors/fonts per spec
3. For HTML output: use CSS variables for the color tokens, Google Fonts for Inter, host MiSans locally or via CDN
   - **MiSans CDN weight pitfall:** jsdelivr `misans@4.1.0` ships NON-standard weights — Regular=330, Medium=380, Semibold=520, Bold=630. `font-weight: 400/600/700` triggers synthetic bold or wrong faces. Use the exact declared weights (kickers/labels/watermarks → 630, banner text → 520, captions → 380).
   - **Font verification pitfall:** the CDN subsets faces by `unicode-range`, so `document.fonts.check('16px MiSans')` returns false on an empty probe. Verify with `document.fonts.load('630 16px MiSans', 'sample text')` first, then check.
4. Match the layout templates based on slide purpose
5. Always include the footer (series name + slide number) on every slide except the title
6. Use the vertical accent bar on content slides to anchor the left margin

## Diagrams for Decks (vendored diagram-design)

When a deck needs a diagram (architecture, flow, comparison, timeline — 38 editorial types), use the vendored diagram-design subsystem instead of hand-drawing SVG:

1. **Read** `vendor/diagram-design/SKILL.md` first — it is the full instruction set (diagram-type selection, accessible-SVG contract, connector rules, motion, export).
2. **Style comes pre-skinned:** `vendor/diagram-design/references/style-guide.md` carries the channel brand on the semantic tokens (`paper`/`ink`/`accent`/`muted` = channel values, MiSans + Inter). Do NOT re-skin per diagram — the tokens flow through every diagram type automatically.
3. **Deck-destined diagrams:** use the `slide-16x9` preset and export `png @2` → **2560×1440**, which drops full-bleed onto the 13.33 × 7.50" slide. The presentation type ramp applies — if it won't fit, drop a level of detail rather than shrinking type. **PNG transparency pitfall:** `omit_background=True` only clears the browser's default backdrop — any `background` set on `html`/`body` in the page CSS (or a full-canvas `<rect>` behind the diagram) still paints and ships an opaque PNG. Set no page background and no backing rect.
4. **Verify before export:** `python vendor/diagram-design/scripts/self_check.py <diagram.html>` must print `OK`. It enforces the accessible-SVG contract (role=img, diagram-prefixed title/desc as first children), single-file safety, and motion rules.
5. **Fonts:** Inter via the approved Google Fonts `<link>`; MiSans via `@import` inside a `<style>` block — **never a `<link>` tag** (the self-check approves only `fonts.googleapis.com/css2` stylesheet links). Use the exact CDN-declared weights (380/520/630) per the style guide's font-stack section.
6. **Reset/re-skin:** the pristine upstream default is snapshotted at `~/.diagram-design/profiles/default.md`; upstream's profile verbs (`save`/`load`/`switch`/`reset`) work against it.

Upstream: `cathrynlavery/diagram-design` v2.6, pinned `648c2a5`, MIT — see `vendor/diagram-design/LICENSE` and `THIRD_PARTY_LICENSES.md`. A verified sample lives in `examples/` at the repo root.

## Pacing & Split Decisions (outro slides specifically)

Before building the deck, decide **one** per slide and confirm with the user when ambiguous. The right number of slides for an outro is "as many as the narration has natural beats, minus one for every beat you cram":

- **3 slides** = the standard outro arc (surprise/proof → scale-up → CTA). Use when the script has a tight three-beat structure and the outro lands all of "scale applies to you + comment-bait + link" in one breath.
- **4 slides** = use when the unique mechanism (e.g., "it tells you the odds before dialing") deserves its own slide instead of being one card. The CTA end-card then becomes a full-bleed quote poster.
- **2 slides** = only when the outro is genuinely two-beat ("result" + "CTA"). Don't under-pack.

When in doubt, ask via `clarify` with two specific options ("spread across two slides" vs "replace current CTA with this end-card"). For Derek's pace, default-recommend **spread** rather than replace — under-shooting creates cramped cards; spreading makes each beat a poster.

## python-pptx Pitfalls (Pitfalls section)

- **`RGBColor` lives in `pptx.dml.color`, NOT `pptx.dgm.color`**. The wrong import fails at module load with `ModuleNotFoundError`.
- **`ROUNDED_RECTANGLE.adjustments[0] = N`** sets corner radius. `N=0` makes a sharp rectangle, `N≈0.4` gives gentle pill rounding. Wrapping in `try/except` is fine — older builds silently ignore it.
- **Slide width is 13.33", height is 7.50".** Anything with `top + height > 7.50"` is off-slide. The slide-number footer at `Inches(7.55)` is the canonical wrong value — use `Inches(7.15)` to leave room for a closing pill above, or place inside a horizontal banner.
- **PowerPoint COM locks open files.** If the user has the .pptx open, `prs.save()` raises `PermissionError [Errno 13]`. Detect via the `~$<file>.pptx` lockfile in `ls`. **Workaround**: bump filename (`...-v2.pptx` → `...-v3.pptx`) and surface the lock in the delivery note so the user closes it before re-running.
- **Font name strings matter.** `font.name = "MiSans Latin"` (NOT `"MiSans"`) so PowerPoint doesn't synthesize fallbacks. Inter is reliable cross-platform.

## Bundled Build Template

See `templates/pine-outro-builder.py` for a working, reusable python-pptx scaffold. It encodes all brand tokens, three layout templates (content / grid / end-card), and the helper functions (`add_rect`, `add_rounded`, `add_text`, `add_multi`, `add_footer`, `add_panel_text`, `add_kicker`). For a new video's outro:

1. Copy `templates/pine-outro-builder.py` to `autods/build_<series>_outro_pptx.py`
2. Update `FOOTER` to the new series name
3. Update `OUT_PATH` to a fresh filename (v2/v3/v4 to dodge PowerPoint locks)
4. Rewrite each slide's content section — the helpers stay
5. `cd ~/autods && python build_<series>_outro_pptx.py`

See `references/python-pptx-pitfalls.md` for the gotchas that bit us, with error messages and fixes.

