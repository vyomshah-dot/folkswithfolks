# site — folkswithfolks.in

The live marketing site (3D-cast flagship). This folder is what GitHub Pages publishes
to **folkswithfolks.in**.

## Contents

```
site/
├── index.html              ← the site (open this)
├── colors_and_type.css     ← MIRROR of ../brand-core/tokens.css (do not edit here)
├── the-house.css           ← layout & section styles (site-only)
├── tweaks-panel.jsx        ← in-page Tweaks controls
├── fonts/                  ← MIRROR of ../brand-core/fonts/ (do not edit here)
└── assets/
    ├── chanakya-hero.jpg
    ├── torana-frame.svg
    └── models/             ← the 3 puppet GLBs (Chanakya, Tenali, Birbal)
```

> **`colors_and_type.css` and `fonts/` are mirrors.** The source of truth lives in
> `../brand-core/`. Whenever you edit `brand-core/tokens.css` or `brand-core/fonts/`,
> run the sync script:
>
> ```powershell
> # Windows
> powershell -File ../tools/sync-brand-core.ps1
> ```
> ```bash
> # macOS / Linux / WSL
> bash ../tools/sync-brand-core.sh
> ```
>
> CI runs this automatically before publishing — so deploys are always in sync.

Three.js, React and Babel load from public CDNs at runtime, so the page needs an
internet connection to render the 3D cast and the Tweaks panel.

## Run it locally

```bash
cd site
python3 -m http.server 8000
# then visit http://localhost:8000
```

## How it's deployed

GitHub Actions (`.github/workflows/pages.yml` at the repo root):

1. Checks out the repo
2. Runs `tools/sync-brand-core.sh` to refresh `site/colors_and_type.css` + `site/fonts/`
3. Publishes `site/` to GitHub Pages → **folkswithfolks.in**

Every push to `main` triggers a deploy.

## Custom domain

The repo-root `CNAME` file (committed) holds `www.folkswithfolks.in`. Point your DNS:

- `CNAME www → <username>.github.io`  (or apex A records per GitHub Pages docs)

`.nojekyll` is included so GitHub Pages serves files as-is.
