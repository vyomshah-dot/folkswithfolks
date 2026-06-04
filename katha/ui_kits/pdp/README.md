# UI Kit — Katha product detail page

A Katha kit **product detail page (PDP)** for *Chanakya's Kit of Wit*, reusing the site
chrome and adding commerce components. React + Babel, brand tokens, Lucide icons in ink.

> Original application of the brand system (no prior product existed) — faithful to the
> brand book's naming pattern (*"Chanakya's Kit of Wit"*), voice, and visual language.

## Run
Open `index.html`.

## Files
| File | What's inside |
|---|---|
| `index.html` | Page shell + all PDP CSS + loaders |
| `SiteChrome.jsx` | Shared `SiteHeader` / `SiteFooter` / `Motif` (copied from the website kit) |
| `PDP.jsx` | `Breadcrumb`, `Gallery`, `BuyPanel`, `QtyStepper`, `ContentsList`, `BuildSteps`, `ReviewList`, `CharBadge` |
| `app.jsx` | `App` + `Toast`, wires the qty + add-to-cart |

## Interactions
- **Gallery** thumbnails switch the main view (box face / puppets / stage / cards).
- **Quantity stepper** + **Add to box** updates the header cart badge and fires a toast.
- **"In the box"** is an accordion (one row open at a time).

## Components covered
Breadcrumb · indigo gallery with motif thumbnails + a Katha box-face mock · buy panel
(badges, price, qty stepper, CTA, ship facts) · accordion · numbered build steps ·
star-rated review cards · character badge.
