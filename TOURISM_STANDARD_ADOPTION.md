# Tourism Standards Adoption - Top Huatulco

Status: Standard installed on 2026-05-29.

Canonical local standard: `TOURISM_PAGE_STANDARDS.md`
Reusable Hermes reference: `static-tourism-sites/references/tourism-destination-page-structure-guide.md`

## Site role

Nine-bay Oaxaca coast guide: bay comparison, HUX airport, boat tours, beach facilities/access, towns, coastal day trips.

## First pages/sections to audit or upgrade

1. All 9 bay pages using the beach/nature contract
2. Destinations hub with compare/choose logic
3. HUX airport and getting-around guides
4. Boat tour, snorkeling, and beach-access practical pages
5. Itineraries that cluster bays realistically

## Avoid

Do not leave bay pages as generic beach blurbs; access, facilities, water conditions, and best-for logic are the point.

## Required implementation pattern

1. Classify the route by page type before writing or editing.
2. Apply the matching page contract from `TOURISM_PAGE_STANDARDS.md`.
3. Add quick verdict / choose-avoid-pair logic where it helps real visitors decide.
4. Add or preserve source/live-check boxes for volatile facts.
5. Verify internal links, metadata, maps/fallbacks, photos/credits, truthful schema, and no public process wording.
6. Run `python3 scripts/audit-tourism-standards.py` plus the repo's normal test/lint/build gates before deploy.
7. Keep production DNS gated until Mogens explicitly approves.
