# UI Kit — Folk with Folks website (Katha storefront)

A high-fidelity recreation of the **Folk with Folks** marketing site, fronting the
**Katha** DIY-puppet-kit line. Built React + Babel (inline JSX), styled with the brand
tokens. Functional icons are **Lucide** (CDN) in ink; brand marks/motifs are the
first-party SVGs.

> This brand had no prior website. These screens are an **original application of the
> brand system** to a plausible storefront — faithful to the brand book's voice, colour,
> type, logo and motif rules, not a copy of an existing product.

## Run
Open `index.html`. Everything is client-side.

## Files
| File | What's inside |
|---|---|
| `index.html` | Page shell + all component CSS, font/Lucide/React loaders |
| `SiteChrome.jsx` | `SiteHeader`, `SiteFooter`, `BrandLockup`, `BrandWordmarkDark`, `ToranaMarkLight`, `Motif` |
| `Storefront.jsx` | `Hero`, `KitGrid`, `KitCard`, `HowItWorks`, `StoryBand`, `Newsletter` |
| `app.jsx` | `App`, `CartDrawer`, `Toast` — interactive add-to-cart flow |

## Interactions
- **Add to box** on any kit card → cart count increments, toast confirms, item appears
  in the slide-out **cart drawer** (open via the bag icon).
- Newsletter form swaps to a confirmation on submit.
- Hover lifts kit cards into their hard ink shadow; buttons nudge on press.

## Components covered
Sticky header w/ nav + cart badge · folk hero with torana "stage" card · product
(kit) cards · numbered how-it-works band (indigo) · Fraunces story pull-quote ·
newsletter capture · multi-column ink footer · slide-out cart drawer · toast.
