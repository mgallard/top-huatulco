# Top Huatulco launch utility and trust audit

Date: 2026-05-30
Scope: non-photo launch readiness after the towns/itineraries/travel-guide/food depth pass.

## What this pass fixes

1. Launch files
   - `public/sitemap.xml` is generated from current public directory routes.
   - `public/robots.txt` allows public routes, disallows the review-only `/media-review/` board, and points to the sitemap.

2. Visitor paths / internal linking
   - Homepage now has a four-question planning spine for first-time visitors, bay choice, itinerary choice, and meals.
   - Towns, itineraries, and travel-guide hubs now link into their child guides instead of presenting inert decision cards.
   - The no-photo next-step goal is better navigation and trust, not another broad copy pass.

3. Content-gap classification
   - Launch blockers: unresolved route-specific photo gaps remain separate and are intentionally not handled here.
   - Pre-review improvements completed here: sitemap/robots trust files, better hub-child links, and homepage decision spine.
   - Later SEO expansion: deeper long-tail pages for lodging zones, family travel, accessibility, and month-by-month weather can wait until after human review.

## Remaining non-photo improvements to consider after review

- Add a dedicated "where to stay in Huatulco" decision page if the site will target lodging intent.
- Add print-friendly checklists only if the travel-guide pages get user traction.
- Add a source-freshness pass immediately before DNS approval to re-check official access, transport, and operator links.

## DNS gate

The preview can be reviewed at `https://top-huatulco.vercel.app`, but production DNS for `TopHuatulco.com` should remain untouched until explicit approval.
