# Katha — Design System

> **A story for clever hands.**

Katha is the Folk with Folks DIY puppet-kit line — *character + "Kit of [trait]"*
(Chanakya's Kit of Wit, Tenali's Kit of Mischief, Birbal's Kit of Cleverness). Each kit
turns an Indian folk character into something a child builds, performs, and keeps.

This package documents Katha's design system. Katha **inherits** the Folk with Folks
foundations — palette, type, motifs, voice — from `../brand-core/` and `../folk-with-folks/`.
This folder captures only what is *Katha-specific*: its logotype, per-character badges,
kit-packaging conventions, and product-line voice samples.

---

## 1. Position in the architecture

| Tier | Name | Role |
|---|---|---|
| Master brand | **Folk with Folks** | The studio. Owns the mark, palette, voice. Signs everything. See `../folk-with-folks/README.md`. |
| Product line | **Katha** *(this package)* | DIY puppet-making kits. Uses FwF palette + type; its own playful **Fraunces-italic terracotta logotype** and per-character badges. |
| Endorsement line | *"a folk with folks kit"* | Eyebrow under the Katha logotype on every kit. Always sentence-case, ink at 70%. |

> Authoritative deep reference: [`chanakya-kit-of-wit-bible.html`](./chanakya-kit-of-wit-bible.html)
> — the flagship kit's full bible (positioning, narrative, gameplay loop, packaging, Katha Quest gamified dashboard).

---

## 2. What's the same as Folk with Folks

These come from `../brand-core/` and the FwF brand book; **do not duplicate or redefine**:

- **Colour palette** — Ink, Paper, Paper Deep, Card, Terracotta, Marigold, Indigo, Neem, Maroon.
  See `../brand-core/tokens.css` and FwF README §3.
- **Type** — Bricolage Grotesque (display) / Fraunces (story, italic) / Hanken Grotesk (body).
  Fonts in `../brand-core/fonts/`.
- **Visual foundations** — 2px ink borders, 14px radius, hard-ink offset shadows, paper-grain
  dot texture, sparse folk motifs, stepped torana arch. See FwF README §6.
- **Motif set & shared artwork** — `../brand-core/shared-assets/` (motifs, buti pattern,
  divider, torana frame).
- **Voice fundamentals** — warm, curious, cheeky. Tell, don't lecture. Sentence case, mostly
  "you", effectively no emoji. See FwF README §5.

---

## 3. What's specific to Katha

### 3.1 Logotype
- **Family:** Fraunces, **italic**, weight 600–700.
- **Colour:** Terracotta `#C24E3A` on Paper; on Indigo blocks, Paper `#F4ECDD`.
- **Tracking:** −1% (slightly tighter than FwF wordmark).
- **Endorsement:** the eyebrow *"a folk with folks kit"* in Hanken 600, ALL-CAPS tracked,
  ink at 70%, sitting under the Katha logotype.
- **Source:** `assets/katha-logotype.svg` *(TODO: place the official vector here)*.

### 3.2 Per-character badges
Each kit has a **character badge** — a circular seal at ~120 px featuring the character's
name in Bricolage and a tiny motif (Chanakya → sun, Tenali → diamond, Birbal → leaf).
- Chanakya — sun motif, terracotta seal, "Kit of Wit"
- Tenali — diamond motif, marigold seal, "Kit of Mischief"
- Birbal — neem-leaf motif, neem seal, "Kit of Cleverness"
- **Source:** `assets/badges/` *(TODO: place official badge vectors here)*.

### 3.3 Kit naming pattern
**`<character>'s Kit of <trait>`** — sentence case after the apostrophe. Examples:
*Chanakya's Kit of Wit*, *Tenali's Kit of Mischief*, *Birbal's Kit of Cleverness*.
Never *KIT OF WIT* (no all-caps sentences); never *Kit Of Wit* (trait is one word, lowercased
preposition style).

### 3.4 Packaging system
The pencil-box-that-opens-into-a-stage. Outer sleeve in Paper Deep with the torana arch
embossed, inner tray in Indigo. Character badge centred on the sleeve; endorsement line
below; safety glyph (⚠) bottom-left only when small parts apply. Full geometry lives in
the Chanakya bible.

### 3.5 Voice — product-line flavour
Inherits FwF voice but leans *a little more cheeky* on the kit:
- *"Chanakya outwitted kings. You're about to out-wit a cardboard box. Roughly the same energy."*
- *"Snip here. Yes, right there."*
- *"Made a wonky one? Good. Wonky has more personality."*

### 3.6 Social channel
- Handle: **`@katha.by.vyom`**
- Avatar: Katha symbol-in-circle (terracotta on paper)
- Highlight covers: single motif on Paper Deep, never busy
- Content pattern: behind-the-build carousels, finished-puppet reels, kid demos

---

## 4. Index — what's in this package

- `README.md` — this file.
- `SKILL.md` — Agent-Skills front-matter so Claude can invoke this as a Katha-only skill.
- `brand-book.html` — Katha overlay book (slim — defers to FwF's book for foundations).
- `chanakya-kit-of-wit-bible.html` — flagship kit deep reference.
- `assets/` — Katha-specific marks: logotype, character badges, kit packaging templates.
  *(Several entries are TODOs — see §3 for what to fill in.)*
- `ui_kits/pdp/` — Katha product detail page (gallery, buy panel, reviews). Originally
  `ui_kits/katha-pdp/` in the old structure.

**Inherits from `../brand-core/` and `../folk-with-folks/`:**
- All tokens, fonts, motifs, torana, divider, buti pattern, voice rules, visual foundations,
  and brand architecture.

---

## 5. TODOs for the human

- [ ] Place official `katha-logotype.svg` in `assets/`.
- [ ] Place character badge vectors in `assets/badges/` (Chanakya, Tenali, Birbal).
- [ ] Place packaging dieline / mockup in `assets/packaging/`.
- [ ] Confirm whether Katha needs its own per-character colour overrides (e.g. Tenali = marigold
      accent dominant) or whether it stays palette-neutral.
- [ ] If a Katha-only voice/content style guide is needed beyond §3.5, write `voice.md`.
