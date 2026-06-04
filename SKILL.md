---
name: folkswithfolks
description: Use this skill when working anywhere in the Folk with Folks ecosystem — the master brand, the Katha DIY puppet-kit line, the folkswithfolks.in marketing site, or any work spanning all three. Contains the shared design foundations (palette, type, fonts, motifs, voice) plus both brand packages and the live site. Choose this skill for cross-brand work; for brand-only work, the per-package skills in folk-with-folks/ and katha/ are scoped narrower.
user-invocable: true
---

# folkswithfolks — combined skill

This is the umbrella skill for the whole repo. Use it when work spans more than one
package, or when you're not yet sure which package owns what you're building.

## Start here

1. Read `README.md` (this folder) — it explains the file layout, sync model, and editing
   rules.
2. Read `brand-core/tokens.css` — the source of truth for colours, type, spacing, radii,
   shadows.
3. Pick the right package for the task:
   - **Master brand work** (FwF studio identity, marketing site, brand book) →
     `folk-with-folks/` and read its `README.md` + `SKILL.md`.
   - **Sub-brand work** (Katha kits, packaging, PDP, social) → `katha/` and read its
     `README.md` + `SKILL.md`.
   - **Shared foundation changes** (a new colour, a new motif) → `brand-core/`, then
     follow the editing checklist in `README.md` §5.
   - **Live-site changes** (folkswithfolks.in pages, copy, layout) → `site/`, then push;
     CI deploys.

## House rules

- **Tokens live once, in `brand-core/tokens.css`.** Never inline a hex code. Never define
  the same colour in a second place.
- **Fonts live once, in `brand-core/fonts/`.** Self-hosted via `@font-face` in
  `tokens.css`. No CDN font calls.
- **Shared brand artwork** (motifs, torana, divider, buti pattern) lives once, in
  `brand-core/shared-assets/`. Both brands import from there.
- **`site/colors_and_type.css` and `site/fonts/` are mirrors.** Edit the source in
  `brand-core/`, then run `tools/sync-brand-core.ps1` (Windows) or `.sh` (Unix/WSL).
- **Voice is one system.** FwF defines it (`folk-with-folks/README.md` §5). Katha inherits
  with a little more cheek (`katha/README.md` §3.5). Don't fork the voice.
