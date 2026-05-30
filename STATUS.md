# Top Huatulco status — 2026-05-30

Working folder: /home/osohermes/projects/top-huatulco
Live preview alias: https://top-huatulco.vercel.app
GitHub backup: https://github.com/mgallard/top-huatulco
Latest commit: 928ea47 Fix destinations mobile comparison layout
Vercel project: top-huatulco under mogensgallardo-8987s-projects; preview/staging alias only, no TopHuatulco.com DNS connected.

Current state:
- Rebuilt as a 46-route Vite/Tailwind static tourism guide based on the Top El Salvador / Top tourism standard.
- Completed bay/itinerary launch-depth pass: all 9 bay pages now include quick verdict, choose/avoid/pair-with, access, water/safety, services, crowd timing, orientation fallback, common mistakes, current-check source links, and FAQ structure. The 3-day and 5-day itineraries now have real day-by-day plans.
- Completed first approved-media promotion: approved WebP assets are wired into homepage hero/mosaic plus Tangolunda, Santa Cruz, El Maguey, San Agustín, 3-day itinerary, and La Crucecita market; visible credits and `media-sources.json` are in place.
- Completed priority entity-depth pass for practical pages: `/food-culture/`, `/tours/`, `/things-to-do/snorkeling/`, `/things-to-do/boat-tours/`, `/things-to-do/copalita-archaeology/`, and `/things-to-do/la-crucecita-market/` now include named restaurants, markets, operators, comparison logic, and live-check/source prompts.
- Completed second media sourcing/promotion pass: added source-checked open-license/local WebP route media to `/destinations/chahue/`, `/destinations/cacaluta/`, `/things-to-do/snorkeling/`, `/things-to-do/boat-tours/`, `/food-culture/`, and `/itineraries/5-days-oaxaca-coast/`; updated `public/images/photos/media-sources.json`, `/image-credits/`, `CONTENT_ENRICHMENT_SOURCES.md`, and `MEDIA_SECOND_PASS.md`.
- Completed responsive/mobile correction for `/destinations/`: the bay comparison now renders as stacked mobile cards on phone widths, keeps the full table for desktop/tablet, and has regression coverage for `data-responsive-table` / `data-mobile-table-cards` markers.
- Deterministic scripts now include `scripts/entity_depth_pass.py` and `scripts/apply_second_media_pass.py`. Regression coverage asserts entity-depth, approved-media, and responsive table/mobile-card markers in `scripts/verify-static-site.py`.

Verification passed:
- `git diff --check`
- `npm run test`
- `npm run lint`
- `npm run audit:tourism`
- `npm run build`
- Asset manifest verification: all 16 local WebP derivatives exist with matching dimensions.
- Remote marker checks passed on Chahué, Cacaluta, snorkeling, boat tours, food/culture, 5-day itinerary, image credits, and `/destinations/` responsive markers.
- Simulated 390px mobile QA passed on `/destinations/`: table hidden, 9 stacked comparison cards visible, no document horizontal overflow.
- Browser visual QA passed for Chahué, Cacaluta, image credits, and the deployed `/destinations/` mobile card view. Food/culture image URL/dimensions verified live; visual model flagged a likely lazy/viewport false negative, but DOM reports complete image load at 1600x1200.
- Vercel deployment aliased to https://top-huatulco.vercel.app.

Known blockers / next actions:
1. Production DNS remains gated. Do not connect TopHuatulco.com until Mogens explicitly approves after content/media review.
2. Remaining hard media gaps: `/destinations/organo/`, `/destinations/chachacual/`, `/destinations/conejos/`, and `/things-to-do/copalita-archaeology/` still need owned photos or a new reviewed candidate board. These were intentionally not filled with generic scenery.
3. Kanban DB currently errors with `no such column: claim_lock`; use COMMAND_CENTER.md and this status file as fallback until Kanban is repaired.

Resume command:
cd /home/osohermes/projects/top-huatulco && hermes --resume
