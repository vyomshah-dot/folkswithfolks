---
name: folk-with-folks-design
description: Use this skill to generate well-branded interfaces and assets for Folk with Folks (an Indian folk-craft studio) and its Katha DIY puppet-kit line — for production or throwaway prototypes/mocks/decks. Contains essential design guidelines, colours, type, fonts, brand vectors (logo, seal, buti pattern, motifs), and UI-kit components for prototyping.
user-invocable: true
---

# Folk with Folks — design skill

**Tales you can hold.** A handmade, warm, a-little-cheeky folk-craft studio. Block-print
and clay, not glossy plastic. Credible enough for a studio, playful enough for a 7-year-old.

## How to use this skill
1. **Read `README.md`** first — it is the full system (colour, type, content/voice, visual
   foundations, iconography, brand architecture, and a file index).
2. **Open `brand-book.html`** for the authoritative reference (logo geometry, seal, pattern,
   CMYK values, voice samples).
3. **Pull tokens** from `../brand-core/tokens.css` (CSS vars for colour + type, plus ready
   element styles). Never invent new colours or fonts — the palette and the three families
   are fixed. Fonts are self-hosted in `../brand-core/fonts/`.
4. **Copy assets**: master-brand marks (logo, seal) live in this package's `assets/`;
   shared visual language (motifs, buti pattern, divider, torana frame) lives in
   `../brand-core/shared-assets/`. Don't hand-draw new motifs — reuse these so the hand
   stays consistent across both FwF and Katha.
5. **Reuse UI components** from `ui_kits/website/` (FwF marketing site / Katha storefront)
   and `../katha/ui_kits/pdp/` (Katha product detail page).

If creating visual artifacts (slides, mocks, throwaway prototypes), copy assets out and create
static HTML files for the user to view. If working on production code, copy assets and read the
rules here to design as an expert in this brand.

If invoked with no other guidance, ask what the user wants to build, ask a few focused questions,
then act as an expert designer who outputs HTML artifacts **or** production code as needed.

## Non-negotiables
- **Colour (exact):** Ink `#2A241F` · Paper `#F4ECDD` · Paper Deep `#EADDC6` · Card `#FBF6EB`
  · Terracotta `#C24E3A` · Marigold `#E8A33D` · Indigo `#2E3A59` · Neem `#5C7A4A` · Maroon `#7A2E2E`.
  Ratio ≈ 60 paper / 20 ink / 12 terracotta+marigold / 8 indigo+neem+maroon.
- **Type:** Bricolage Grotesque (display, −2% tracking) · Fraunces italic (story/quotes) ·
  Hanken Grotesk (body/UI, 1.6).
- **Look:** 2px ink borders · 14px radius · hard ink offset shadow (NO blur, NO glow) · subtle
  paper-grain dots · sparse folk motifs · stepped torana arch as the framing device.
- **Voice:** warm, curious, cheeky. Tell, don't lecture. Short sentences, sentence case,
  mostly "you". Effectively no emoji (lone exception: ⚠ on safety warnings).
- **Logo:** never recolour the figures outside the palette, never stretch/rotate, never add
  gradients/shadows, never re-typeset the wordmark. Clear space = one figure-height; min 120px.
- **Icons:** brand/decorative → motif SVGs in `../brand-core/shared-assets/`; functional UI controls → Lucide in ink.
