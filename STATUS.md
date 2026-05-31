# Top Huatulco status — 2026-05-30

Working folder: /home/osohermes/projects/top-huatulco
Live preview alias: https://top-huatulco.vercel.app
GitHub backup: https://github.com/mgallard/top-huatulco
Latest code commit: pending section-depth reset for Things to do, Itineraries, and Travel guide
Vercel project: top-huatulco under mogensgallardo-8987s-projects; preview/staging alias only, no TopHuatulco.com DNS connected.

Current state:
- Rebuilt as a 46-route Vite/Tailwind static tourism guide based on the Top El Salvador / Top tourism standard.
- Completed bay/itinerary launch-depth pass: all 9 bay pages now include quick verdict, choose/avoid/pair-with, access, water/safety, services, crowd timing, orientation fallback, common mistakes, current-check source links, and FAQ structure. The 3-day and 5-day itineraries now have real day-by-day plans.
- Completed first approved-media promotion: approved WebP assets are wired into homepage hero/mosaic plus Tangolunda, Santa Cruz, El Maguey, San Agustín, 3-day itinerary, and La Crucecita market; visible credits and `media-sources.json` are in place.
- Completed priority entity-depth pass for practical pages: `/food-culture/`, `/tours/`, `/things-to-do/snorkeling/`, `/things-to-do/boat-tours/`, `/things-to-do/copalita-archaeology/`, and `/things-to-do/la-crucecita-market/` now include named restaurants, markets, operators, comparison logic, and live-check/source prompts.
- Completed second media sourcing/promotion pass: added source-checked open-license/local WebP route media to `/destinations/chahue/`, `/destinations/cacaluta/`, `/things-to-do/snorkeling/`, `/things-to-do/boat-tours/`, `/food-culture/`, and `/itineraries/5-days-oaxaca-coast/`; updated `public/images/photos/media-sources.json`, `/image-credits/`, `CONTENT_ENRICHMENT_SOURCES.md`, and `MEDIA_SECOND_PASS.md`.
- Completed responsive/mobile correction for `/destinations/`: the bay comparison now renders as stacked mobile cards on phone widths, keeps the full table for desktop/tablet, and has regression coverage for `data-responsive-table` / `data-mobile-table-cards` markers.
- Completed visitor-reference depth pass for weak towns, itineraries, travel-guide, and food sections: town pages now explain how to choose La Crucecita, Santa Cruz, Copalita/Bocana, Mazunte, and Puerto Ángel by purpose and route logic; the 4-day and snorkel/boat itineraries now have practical day cards; travel-guide pages now include decision rules for airport arrival, getting around, seasons, safety, money, packing, and first-time planning; `/food-culture/` now has stronger named-place/dish/use-case guidance.
- Completed non-photo launch utility/trust pass: generated sitemap/robots coverage for 46 public routes, excluded `/media-review/` from sitemap and disallowed it in robots, added a homepage four-question planning spine, added visible hub-child CTAs for towns/itineraries/travel-guide, and documented remaining non-photo launch gaps in `LAUNCH_GAP_AUDIT.md`.
- Completed section-depth reset for the weak Things to do, Itineraries, and Travel guide sections: rebuilt one model page for each section (`/things-to-do/boat-tours/`, `/itineraries/4-days-relax-snorkel/`, `/travel-guide/getting-around/`) and scaled the subject-led structure across 22 pages with quick verdicts, choose/avoid logic, day-by-day planning, backup rules, practical logistics, local options, source/live-check links, responsive tables, and `SECTION_DEPTH_RESET_AUDIT.md`.
- Deterministic scripts now include `scripts/entity_depth_pass.py`, `scripts/apply_second_media_pass.py`, `scripts/visitor_reference_depth_pass.py`, `scripts/launch_utility_trust_pass.py`, and `scripts/section_depth_reset.py`. Regression coverage asserts entity-depth, approved-media, responsive table/mobile-card, visitor-reference depth, section-depth reset, launch-utility, sitemap, robots, and audit markers in `scripts/verify-static-site.py`.

Verification passed:
- `git diff --check`
- `npm run test`
- `npm run lint`
- `npm run audit:tourism`
- `npm run build`
- Asset manifest verification: all 16 local WebP derivatives exist with matching dimensions.
- Remote marker checks passed on towns hub, La Crucecita, 4-day itinerary, snorkel/boat itinerary, getting-around guide, food/culture, Chahué, Cacaluta, snorkeling, boat tours, 5-day itinerary, image credits, homepage launch spine, hub-child CTAs, sitemap, robots, `/destinations/` responsive markers, and the new section-depth reset markers on Things to do / Itineraries / Travel guide hubs and model pages.
- Simulated 390px mobile QA passed on homepage, towns hub, itineraries hub, travel-guide hub, 4-day itinerary, getting-around guide, food/culture, `/destinations/`, and the three rebuilt model pages (`/things-to-do/boat-tours/`, `/itineraries/4-days-relax-snorkel/`, `/travel-guide/getting-around/`): no document horizontal overflow; homepage has 4 launch path links, towns hub has 5 child CTAs, itineraries hub has 4, travel-guide hub has 6; `/destinations/` still hides the desktop table and shows 9 stacked comparison cards.
- Browser visual QA passed for the deployed homepage launch spine, upgraded towns hub, rebuilt Things to do model page, expanded 4-day itinerary, food/culture page, Chahué, Cacaluta, image credits, and the deployed `/destinations/` mobile card view. Food/culture image URL/dimensions verified live; homepage mosaic images also report complete natural dimensions live.
- Vercel deployment aliased to https://top-huatulco.vercel.app.

Known blockers / next actions:
1. Production DNS remains gated. Do not connect TopHuatulco.com until Mogens explicitly approves after content/media review.
2. Remaining hard media gaps: `/destinations/organo/`, `/destinations/chachacual/`, `/destinations/conejos/`, and `/things-to-do/copalita-archaeology/` still need owned photos or a new reviewed candidate board. These were intentionally not filled with generic scenery.
3. Kanban DB currently errors with `no such column: claim_lock`; use COMMAND_CENTER.md and this status file as fallback until Kanban is repaired.

Resume command:
cd /home/osohermes/projects/top-huatulco && hermes --resume
