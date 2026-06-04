# folkswithfolks

> **Tales you can hold.** The single source of truth for everything Folk with Folks —
> the studio, the Katha kit line, the website, and the design systems behind them.

This repo powers four things and keeps them in sync:

| What | Where it lives | What it is |
|---|---|---|
| **Folk with Folks design system** | [`folk-with-folks/`](./folk-with-folks/) | Master-brand design tokens, brand book, assets, UI kits |
| **Katha design system** | [`katha/`](./katha/) | Sub-brand overlay for the DIY puppet-kit line |
| **Shared foundations** | [`brand-core/`](./brand-core/) | Tokens, fonts, shared brand artwork — inherited by both brands |
| **folkswithfolks.in** | [`site/`](./site/) | The live marketing site, auto-deployed via GitHub Pages |

---

## 1. File-management rules

The whole point of this layout is that **one edit in one place propagates everywhere**.

### Single source of truth: `brand-core/`

`brand-core/tokens.css` is the only place colours, type scale, spacing, radii, and shadows
are defined. Both `folk-with-folks/` and `katha/` read from it. The live site reads a
mirrored copy that is kept in sync automatically.

**Never** duplicate a colour or a token value. If you find yourself typing a hex code
that isn't in `tokens.css`, stop — either it already exists with a different name, or
it shouldn't exist at all.

### What belongs where

- **`brand-core/`** — anything that **both** FwF and Katha use. Tokens, fonts, motif set,
  buti pattern, torana frame, divider. The studio's visual DNA.
- **`folk-with-folks/`** — anything that is the **master brand's identity**: the FwF logo
  marks, the seal, the brand book, FwF-only UI kits, FwF preview cards.
- **`katha/`** — anything that is **Katha-specific**: the Katha logotype, character
  badges, kit packaging, the Chanakya bible, the PDP UI kit.
- **`site/`** — anything that is **only the live folkswithfolks.in website**: the 3D-cast
  page, hero imagery, GLB models, the Tweaks panel. CSS tokens and fonts are *mirrored*
  from `brand-core/`, not original.

### Mirrored files (do not edit at the mirror)

`site/colors_and_type.css` and `site/fonts/` are **mirrors** of `brand-core/`. After any
brand-core edit, run:

```powershell
# Windows
powershell -File tools/sync-brand-core.ps1
```
```bash
# macOS / Linux / WSL
bash tools/sync-brand-core.sh
```

CI runs this before every deploy — so the live site can't drift from brand-core.

---

## 2. How the sync works

```
                     GitHub repo (this thing)
                     ────── single source of truth ──────
                       │                  │           │
        ┌──────────────┘                  │           └────────────┐
        ▼                                 ▼                        ▼
   Claude Code                      Claude.ai web              folkswithfolks.in
   (local clone)                    (Project synced            (GitHub Pages from
   reads SKILL.md                    to this repo)              site/ on every push)
        │                                  │                        │
   git pull                          re-indexes on push        GitHub Action deploys
```

| Surface | How it reads the repo | Refresh model |
|---|---|---|
| **GitHub** | Source of truth | every `git push` |
| **Claude Code** (this CLI on your machine) | Reads `SKILL.md` from the local clone | `git pull` |
| **Claude.ai chat / Projects** | Connect this GitHub repo to a Claude Project | auto re-syncs on push |
| **folkswithfolks.in** | GitHub Pages publishes `site/` after sync script runs | every push to `main` |

So: change a token in `brand-core/tokens.css` → push → all four are in sync.

---

## 3. Using this repo as a Claude skill

Both **Claude Code** (this CLI) and **Claude.ai web** can use this repo as a skill.

### From Claude Code (you, locally)
This repo ships three `SKILL.md` files. Open Claude Code from any of these working
directories and the skill activates:

| Skill | Working dir | Use it for |
|---|---|---|
| `folkswithfolks` (combined) | repo root | anything spanning both brands |
| `folk-with-folks-design` | `folk-with-folks/` | master brand work |
| `katha-design` | `katha/` | Katha kits, packaging, PDP |

### From Claude.ai chat
1. Create a **Project** on claude.ai.
2. Connect it to this GitHub repo (Project → Settings → Connect GitHub).
3. The Project re-syncs whenever you push. You can chat with Claude about the design
   system without uploading zips.

---

## 4. Index

- **`brand-core/`** — tokens.css · fonts/ · shared-assets/ (motifs, torana, divider, buti pattern)
- **`folk-with-folks/`** — README · SKILL.md · brand-book.html · assets/ (logo, seal, lockups) · preview/ (21 cards) · ui_kits/website/
- **`katha/`** — README · SKILL.md · brand-book.html · chanakya-kit-of-wit-bible.html · assets/ (TODOs for logotype + badges) · ui_kits/pdp/
- **`site/`** — the deployed marketing site; `colors_and_type.css` and `fonts/` are mirrors
- **`tools/`** — `sync-brand-core.ps1` / `.sh` — the mirror sync script
- **`.github/workflows/pages.yml`** — auto-deploy to GitHub Pages
- **`_archive/`** — old zips and one-off scraps (gitignored by default)

---

## 5. Editing checklist

| If you're changing… | Edit here | Then |
|---|---|---|
| A colour, type size, spacing, radius, or shadow | `brand-core/tokens.css` | run sync script (or just push — CI runs it) |
| A font file | `brand-core/fonts/` | run sync script |
| A motif, the buti pattern, the torana frame | `brand-core/shared-assets/` | nothing — both brands pick it up |
| The FwF logo, seal, or master-brand voice | `folk-with-folks/` | nothing — Katha inherits voice but not the FwF mark |
| The Katha logotype, character badges, kit naming, packaging | `katha/` | nothing |
| Anything on folkswithfolks.in that isn't tokens | `site/` | push (CI deploys) |
