# Top Huatulco status — 2026-05-30

Working folder: /home/osohermes/projects/top-huatulco
Live preview alias: https://top-huatulco.vercel.app
GitHub backup: https://github.com/mgallard/top-huatulco
Latest commit: c1e49f4 Improve Huatulco priority guide depth
Vercel project: top-huatulco under mogensgallardo-8987s-projects; preview/staging alias only, no TopHuatulco.com DNS connected.

Current state:
- Rebuilt as a 46-route Vite/Tailwind static tourism guide based on the Top El Salvador / Top tourism standard.
- Completed bay/itinerary launch-depth pass: all 9 bay pages now include quick verdict, choose/avoid/pair-with, access, water/safety, services, crowd timing, orientation fallback, common mistakes, current-check source links, and FAQ structure. The 3-day and 5-day itineraries now have real day-by-day plans.
- Completed first approved-media promotion: approved WebP assets are wired into homepage hero/mosaic plus Tangolunda, Santa Cruz, El Maguey, San Agustín, 3-day itinerary, and La Crucecita market; visible credits and `media-sources.json` are in place.
- Completed priority entity-depth pass for practical pages: `/food-culture/`, `/tours/`, `/things-to-do/snorkeling/`, `/things-to-do/boat-tours/`, `/things-to-do/copalita-archaeology/`, and `/things-to-do/la-crucecita-market/` now include named restaurants, markets, operators, comparison logic, and live-check/source prompts.
- Regression coverage now asserts entity-depth markers and named-place/operator content in `scripts/verify-static-site.py`. Source usage notes are recorded in `CONTENT_ENRICHMENT_SOURCES.md`. Deterministic generator: `scripts/entity_depth_pass.py`.

Verification passed:
- `git diff --check`
- `npm run test`
- `npm run lint`
- `npm run audit:tourism`
- `npm run build`
- Remote marker checks passed on food/culture, tours, snorkeling, boat tours, Copalita archaeology, and La Crucecita market.
- Browser visual QA passed for food/culture and tours; the tours operator comparison matrix rendered cleanly on desktop.
- Vercel deployment aliased to https://top-huatulco.vercel.app.

Known blockers / next actions:
1. Production DNS remains gated. Do not connect TopHuatulco.com until Mogens explicitly approves after content/media review.
2. Remaining media gaps: Chahué, Órgano, Cacaluta, Chachacual, Conejos, 5-day itinerary, snorkeling, Copalita, food/culture, boat tours, and several practical pages still need better approved/owned route-specific imagery.
3. Kanban DB currently errors with `no such column: claim_lock`; use COMMAND_CENTER.md and this status file as fallback until Kanban is repaired.

Resume command:
cd /home/osohermes/projects/top-huatulco && hermes --resume
