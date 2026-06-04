---
name: katha-design
description: Use this skill to generate well-branded interfaces, packaging mockups, kit collateral, and content for Katha — the DIY puppet-kit line by Folk with Folks. Katha inherits all Folk with Folks foundations (palette, type, motifs, voice) and adds its own logotype, per-character badges, and kit-naming conventions. Use this skill when working on Katha kits (Chanakya's Kit of Wit, Tenali's Kit of Mischief, Birbal's Kit of Cleverness), Katha product pages, Katha social, or anything carrying the Katha mark.
user-invocable: true
---

# Katha — design skill

**A story for clever hands.** Katha is the Folk with Folks DIY puppet-kit line.
Pencil-box that opens into a puppet stage. Indian folk characters that a child builds,
performs, and keeps.

## How to use this skill

1. **Read `README.md`** in this folder first — it lists what Katha inherits from FwF and
   what is Katha-specific (logotype, badges, naming, packaging, voice flavour).
2. **Read `../folk-with-folks/README.md`** for the foundations Katha inherits (colour,
   type, voice, visual rules, motifs, brand architecture).
3. **Open `chanakya-kit-of-wit-bible.html`** for the flagship kit's deep reference
   (positioning, narrative, packaging, Katha Quest gamified dashboard).
4. **Pull tokens** from `../brand-core/tokens.css`. Fonts in `../brand-core/fonts/`.
   Shared brand artwork (motifs, torana, divider, buti) in `../brand-core/shared-assets/`.
   Never invent new colours, fonts, or motifs.
5. **Use Katha-specific assets** from `assets/` (logotype, character badges, packaging).
   If a needed asset is a TODO, flag it and use a placeholder.
6. **Reuse the PDP UI kit** in `ui_kits/pdp/` for product detail pages.

If creating visual artifacts (kit mocks, packaging mockups, social posts, slides), copy
assets out and create static HTML for the user to view. If working on production code,
read the rules here and design as an expert in this brand.

If invoked with no other guidance, ask which kit / surface (PDP, packaging, social, slide,
print collateral), then act as an expert designer.

## Non-negotiables (Katha-specific)

- **Katha logotype:** Fraunces italic, weight 600–700, terracotta on paper / paper on indigo.
  Never re-typeset in another family. Always paired with the endorsement eyebrow
  *"a folk with folks kit"* in Hanken 600 ALL-CAPS tracked, ink at 70%.
- **Kit naming:** `<character>'s Kit of <trait>` — sentence case (e.g. *Chanakya's Kit of Wit*).
  Never SHOUTING; never Title Case Every Word.
- **Character badges:** circular, single motif inside, character name in Bricolage 800.
  Stay within the FwF palette — terracotta, marigold, neem are the badge fills.
- **Voice:** inherits FwF voice; leans *a little more cheeky* on the kit copy. Treat the kid
  as clever. "Wonky has more personality" is canonical encouragement.
- **Safety:** ⚠ on small-parts warnings, always pre-pending a sentence that explains *why*.
  Never an emoji elsewhere.

## Non-negotiables (inherited from FwF — always also apply)

- **Colour:** Ink `#2A241F` · Paper `#F4ECDD` · Paper Deep `#EADDC6` · Card `#FBF6EB` ·
  Terracotta `#C24E3A` · Marigold `#E8A33D` · Indigo `#2E3A59` · Neem `#5C7A4A` · Maroon `#7A2E2E`.
- **Type:** Bricolage (display) · Fraunces italic (story, *and* the Katha logotype) · Hanken (body).
- **Look:** 2px ink borders · 14px radius · hard ink offset shadow (no blur, no glow) ·
  paper-grain dots · sparse motifs · torana arch as framing device.
