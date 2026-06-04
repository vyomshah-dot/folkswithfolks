# Folk with Folks — Design System

> **Tales you can hold.**

This repository is the design system for **Folk with Folks**, an Indian folk-craft
studio (puppetry, stop-motion, folk tales, and craft kits for curious kids) and its
sub-brand **Katha** (DIY puppet kits). It contains the brand foundations (colour,
type, motifs), real visual assets (logo, patterns), CSS tokens, preview cards for the
Design System tab, UI kits, and sample slides.

---

## 1. Brand at a glance

| | |
|---|---|
| **Studio** | Folk with Folks |
| **Sub-brand** | Katha (DIY puppet kits) |
| **Tagline** | Tales you can hold. |
| **Personality** | Handmade, warm, a little cheeky and wonky. Block-print and clay, not glossy plastic. Credible enough for a studio, playful enough for a 7-year-old. |
| **Audience** | Curious kids (~7) and the adults who buy for / make with them. |

The visual world is **block-print and clay**: warm paper grounds, ink line-art,
terracotta and marigold accents, and sparse folk motifs (buti flowers, dots,
triangles, suns, leaves) framed by a stepped **torana** (puppet-stage) arch.

---

## 2. Sources

This system is built from two inputs, both reproduced/stored in this project:

1. **The written brand brief** (personality, palette, type, visual language, voice).
2. **`brand-book.html`** — the official *Folk with Folks Brand Book v1 (2026)*, supplied
   as an attachment and copied to the project root. **This is the authoritative source.**
   It contains the real logo geometry, the seal, the buti pattern, the folk divider,
   CMYK/RGB values, the brand architecture (FwF → Katha), kit-naming pattern, and voice
   samples. Open it directly for the fullest reference.

No GitHub repo or Figma file was provided.

> ✅ **Assets are extracted from the brand book, not invented.** The vectors in `assets/`
> (`fwf-symbol.svg`, `fwf-symbol-mono.svg`, `fwf-seal.svg`, `fwf-divider.svg`,
> `fwf-pattern-buti.svg`, and the lockup) are lifted verbatim from the brand book's inline
> SVG, recoloured only within the approved palette. The `motifs.svg` set (sun, triangle,
> leaf, dot, diamond, buti) is the one piece **drawn here** to match the brand book's named
> “motif set” slot — flag if you have official motif art.
>
> ✅ **Fonts are self-hosted.** All three families ship as variable TTFs in `fonts/`
> (Bricolage Grotesque, Fraunces roman + italic, Hanken Grotesk roman + italic) and are
> wired via `@font-face` in `colors_and_type.css` — no CDN dependency, fully offline.

---

## 3. Colour — use exactly

The brief specifies an exact palette. **Do not invent new colours.**

| Token | Name | Hex | Role |
|---|---|---|---|
| `--ink` | Ink | `#2A241F` | Primary text, line art |
| `--paper` | Paper | `#F4ECDD` | Default background |
| `--paper-deep` | Paper Deep | `#EADDC6` | Secondary background / cards |
| `--terracotta` | Terracotta | `#C24E3A` | Primary accent, buttons, heading highlight |
| `--marigold` | Marigold | `#E8A33D` | Secondary accent, dots, highlights |
| `--indigo` | Indigo | `#2E3A59` | Deep background blocks |
| `--neem` | Neem Leaf | `#5C7A4A` | Tertiary accent |
| `--maroon` | Maroon | `#7A2E2E` | Warnings / deep accent |

**Usage ratio:** ~60% paper · 20% ink · 12% terracotta + marigold · 8% indigo / neem / maroon.

---

## 4. Typography — Google Fonts

| Role | Family | Weights / style | Notes |
|---|---|---|---|
| Display / headlines / wordmark | **Bricolage Grotesque** | 800 / 600 | letter-spacing −2% |
| Story / quotes / flourish | **Fraunces** | italic | optical, warm |
| Body / UI / instructions | **Hanken Grotesk** | 400 / 600 | line-height 1.6 |

**Scale (px):** H1 64 · H2 44 · H3 24 · lead 21 · body 17 · caption 13.

See `colors_and_type.css` for the full token set (base + semantic). The three families are
self-hosted from `fonts/` via `@font-face` (variable TTFs) — no CDN required.

---

## 5. Content fundamentals

**Voice:** warm, curious, cheeky. We *tell, don't lecture*. Short sentences. A wink,
never a sneer. Treat kids as clever and adults as kids-who-forgot.

| Dimension | Rule |
|---|---|
| **Person** | Mostly **"you"** ("Open the box", "Watch it come alive"). "We" for the studio's own promises ("We'll print your name on it"). |
| **Sentence length** | Short. Often fragments. Imperatives lead ("Snip here. Yes, right there."). |
| **Casing** | Sentence case everywhere — headlines, buttons, labels. ALL-CAPS only for tiny tracked-out eyebrow labels (e.g. `KATHA KIT`, `AGES 7+`). Never SHOUTING sentences. |
| **Tone toward mistakes** | Encouraging and a little contrarian — "Made a wonky one? Good. Wonky has more personality." Wonkiness is a feature, not a defect. |
| **Numbers / claims** | Sparse. No invented stats, no "data slop". A price, an age, a piece-count — that's it. |
| **Emoji** | Effectively **none** in marketing/product copy. The one sanctioned exception is a single **⚠** on a safety warning (small parts). Use motif SVGs, not emoji, for delight. |
| **Punctuation flavour** | Em-dashes for the aside-with-a-wink. Occasional ellipsis to invite ("Little maker…"). Exclamation marks: rare, earned. |

**Examples (house style):**
- Hero: *"Tales you can hold."* / *"A story for clever hands."*
- Button: *"Open the box"* · *"Start a tale"* (verb-first, sentence case)
- Empty state: *"No puppets yet. Every studio starts with one."*
- Safety: *"⚠ Small parts — a grown-up should help with the snipping."*
- Avoid: *"Utilise the enclosed implement to separate components."* (cold, corporate, lecturing)

The **Fraunces italic** voice is reserved for *story* — folk-tale snippets, quotes,
the narrator's wink. **Hanken** carries everything practical (instructions, UI).
**Bricolage** is the loud, confident headline voice.

---

## 6. Visual foundations

**Overall vibe:** block-print and clay. Warm, handmade, a touch wonky. Flat ink line-art
over warm paper, with terracotta/marigold as the joy and indigo/neem/maroon as seasoning.
Nothing glossy, nothing corporate.

- **Colour** — Exact palette only (§3). Ratio ~60 paper / 20 ink / 12 terracotta+marigold
  / 8 indigo+neem+maroon. Terracotta is the action colour; marigold is delight/highlight;
  indigo is for deep "night" blocks (footers, feature bands); maroon is warnings only.
- **Backgrounds** — Default is **Paper `#F4ECDD`** carrying a subtle **paper-grain dot
  texture** (radial dots, ~9px grid, ~12% ink). Deep blocks use **Indigo** with a paper-dot
  grain at ~14%. The **buti pattern** appears as a *quiet* field behind blocks — never
  full-bleed under body text, never loud. No photographic backgrounds by default; if photos
  are used they should read warm/handmade (clay, paper, craft tables), not stock-y.
- **Type** — Bricolage (display, −2% tracking), Fraunces italic (story), Hanken (body, 1.6).
  Scale: 64 / 44 / 24 / 21 / 17 / 13.
- **Spacing** — 4px base scale (4·8·12·16·24·32·48·64·96). Generous, calm.
- **Borders** — The signature is a crisp **2px ink border** on cards, inputs, buttons,
  chips. Hairline dividers at 12% ink.
- **Corner radii** — Friendly but not bubbly: **14px** default, 8px small, 22px large,
  full pill for tags and some buttons.
- **Shadows** — **Hard ink offset, NEVER blurred.** `5px 5px 0` ink is the signature
  ("hard shadow"); 3px for smaller elements; a terracotta variant for playful emphasis.
  No soft drop-shadows, **no glows** — ever.
- **The torana / stepped-arch** is the recurring framing device. Use it to crown heroes,
  section headers, and feature cards — it turns any block into a little stage.
- **Motifs** (dot, triangle, sun, neem leaf, buti flower, diamond) are used **sparsely**
  as punctuation and delight — corners, between sections, beside a heading. Never a confetti
  storm.
- **Animation** — Gentle and handmade. Short (120–220ms), ease-out. A tiny **press nudge**
  (`translate(2px,2px)`) on buttons so they feel physically pushed, paired with a darker
  terracotta. Optional small **bounce/wobble** on playful elements (puppets, motifs) — wonky,
  not springy-slick. Fades for entrances. No parallax, no slick easing curves.
- **Hover** — Buttons lighten slightly (terracotta → `#CC5942`); ghost buttons fill with
  12% ink; cards may lift by gaining/deepening their hard shadow (offset grows), not by
  blurring.
- **Press** — Colour darkens (`--terracotta-press #A8412F`) and the element nudges down-right
  into its own shadow.
- **Focus** — A **3px terracotta hard shadow** (no blur) instead of a browser glow.
- **Transparency / blur** — Used minimally. Tints (ink at 12/45/70%) for text hierarchy and
  hairlines; **no frosted glass / backdrop-blur** — it fights the flat block-print feel.
- **Cards** — Paper-Deep fill, 2px ink border, 14px radius, optional 5px hard ink shadow.
  Flat. Imagery (motif or product) sits inside the border, not bleeding past it.

---

## 7. Iconography

Folk with Folks does **not** ship a conventional UI icon font. Its "icons" are the
**folk motif set** — flat, block-print symbols drawn in the palette:

- **Primary system:** first-party motif SVGs in `assets/` — `motifs.svg` (dot, triangle,
  sun, neem leaf, buti flower, diamond), `pattern-buti.svg`, `torana-frame.svg`, and the
  logo files. These are the brand's signature marks and should be used for delight,
  bullets, section dividers, and decoration.
- **Functional UI icons** (cart, menu, close, arrows, search, etc.) are **not** part of the
  brand artwork and were not provided. For these, use **[Lucide](https://lucide.dev)** from
  CDN — its 2px rounded-stroke geometry sits comfortably next to the 2px ink borders and the
  hand-drawn motifs. **Always set Lucide `stroke` to `--ink` (`#2A241F`)**, stroke-width 2,
  so functional icons read as the same "ink line-art" hand as the motifs.
  > ⚠️ **Substitution flag:** Lucide is a *substitute* for functional icons — no functional
  > icon set was provided in the brief. Swap it out if you adopt an official set.
- **Emoji:** not used as iconography (see §5). The lone exception is **⚠** on safety
  warnings.
- **Unicode glyphs:** sparingly fine for tiny arrows/checks (→ ✓ ✕) inside chips and
  do/don't lists, always in ink or an accent colour.

**Rule of thumb:** decorative + brand → motif SVG; functional control → Lucide in ink.
Never hand-roll a new motif in a one-off design — reuse the assets here so the hand stays
consistent.

## 8. Brand architecture

Folk with Folks is the **master brand** (the studio). Everything is "a Folk with Folks ___".

| Tier | Name | Role |
|---|---|---|
| Master brand | **Folk with Folks** | The studio. Owns the mark, palette, voice. Signs off everything: *"a Folk with Folks kit / film / workshop."* |
| Product line | **Katha** | DIY puppet-making kits. Uses FwF palette + type; its own playful **Fraunces-italic terracotta logotype** and per-character badges. |
| Channel (future) | **Folk with Folks** (YouTube) | Animated folk tales — the studio's voice on screen. |

- **Kit naming pattern:** *character + "Kit of [trait]"* — e.g. *Chanakya's Kit of Wit*,
  *Tenali's Kit of Mischief*, *Birbal's Kit of Cleverness*.
- **Endorsement line:** *"a folk with folks kit"* (eyebrow under the Katha logotype).
- **Social:** `@katha.by.vyom` — symbol-in-circle avatar, motif highlight covers,
  behind-the-build carousels.
- **Voice sample (Katha copy):** *"Chanakya outwitted kings. You're about to out-wit a
  cardboard box. Roughly the same energy."*

---

## 9. Index — what's in this package

This package (`folk-with-folks/`) holds master-brand-specific files. Foundations (tokens,
fonts, shared brand artwork) live one level up in `../brand-core/` and are inherited by
both this package and `../katha/`. See the repo-root `README.md` for the full file-management
model.

**This package**
- `README.md` — this file (foundations, content, visual, iconography, architecture).
- `brand-book.html` — the official Brand Book v1 (authoritative reference; open in browser).
- `SKILL.md` — Agent-Skills front-matter so this folder can be used as a Claude skill.

**`assets/`** — FwF master-brand vectors (the studio's mark)
- `fwf-symbol.svg` / `logo-torana-stage.svg` — primary Torana Stage symbol (full colour)
- `fwf-symbol-mono.svg` — one-colour symbol (emboss / stamp / foil)
- `logo-lockup.svg` — symbol + lowercase wordmark + tagline
- `fwf-seal.svg` — circular seal / stamp
- `logos/` — all logo PNG exports (lockup, wordmark, seal variants)

**`preview/`** — Design System tab cards (colour, type, spacing, components, brand). 21 cards.

**`ui_kits/`**
- `website/` — Folk with Folks marketing site / Katha storefront (hero, kit grid, cart). See its `README.md`.

> The **Katha product detail page** kit moved to `../katha/ui_kits/pdp/` — it belongs to
> the Katha sub-brand package.

**Inherited from `../brand-core/`** (shared by FwF and Katha)
- `tokens.css` — colour + type tokens and ready-made element styles (was `colors_and_type.css`).
- `fonts/` — Bricolage Grotesque, Fraunces (roman + italic), Hanken Grotesk (roman + italic).
- `shared-assets/` — `motifs.svg`, `torana-frame.svg`, `fwf-divider.svg`,
  `fwf-pattern-buti.svg`, `pattern-buti.svg`. The studio's visual language; Katha reuses these.

> **No slide deck** is included: none was provided, and a template shouldn't be invented.
> The brand book lists a deck/pitch template as a future slot to fill.
