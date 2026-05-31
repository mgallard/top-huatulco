# Top Huatulco Section Depth Reset Audit

Date: 2026-05-30
Scope: Things to do, Itineraries, Travel guide

## Why this pass happened

A previous pass gave these sections the right skeleton, but many pages still read too thin for the tourism website standard. The weak spots were mostly practical utility: pages had markers and headings, but not enough decision support, route logic, named anchors, backup plans, or same-week verification cues.

## New standard applied

Each affected section now uses a stricter subject-led visitor-reference pattern:

- Quick verdict: should a visitor actually put this in the plan?
- Choose / avoid logic: who it fits and who should skip it.
- Practical logistics: transport, timing, heat, water conditions, cash, return planning.
- Scenario rules: how it fits arrival days, families, active travelers, and backup days.
- Local options to check: named places, operators, markets, bay anchors, or base areas where appropriate.
- Responsive comparison tables marked with `data-responsive-table`.
- Visible source/live-check section marked with `data-visible-sources='true'`.
- `data-section-depth-reset='true'` and `data-subject-led-guide='true'` markers for regression testing.

## Model pages rebuilt first

1. Things to do model: `/things-to-do/boat-tours/`
   - Rebuilt around route style, Santa Cruz departure logic, operator/inclusion questions, shared vs private boat tradeoffs, water-condition backup, and named operator comparison anchors.

2. Itinerary model: `/itineraries/4-days-relax-snorkel/`
   - Rebuilt around explicit Day 1 to Day 4 cards, morning/afternoon/evening/transport guidance, base strategy, Mercado 3 de Mayo / Copalita backup day, departure-day limits, and water-condition flexibility.

3. Travel guide model: `/travel-guide/getting-around/`
   - Rebuilt around base-area choice, taxi vs pickup vs driver vs rental logic, return-transport risks, same-week checks, and local Huatulco movement rules.

## Scaled pages

Things to do:
- `/things-to-do/`
- `/things-to-do/boat-tours/`
- `/things-to-do/snorkeling/`
- `/things-to-do/copalita-archaeology/`
- `/things-to-do/la-crucecita-market/`
- `/things-to-do/mazunte-day-trip/`
- `/things-to-do/golf-tangolunda/`
- `/things-to-do/sunset-chahue/`
- `/things-to-do/surf-open-coast/`

Itineraries:
- `/itineraries/`
- `/itineraries/3-days-huatulco/`
- `/itineraries/4-days-relax-snorkel/`
- `/itineraries/5-days-oaxaca-coast/`
- `/itineraries/snorkel-boat-day/`

Travel guide:
- `/travel-guide/`
- `/travel-guide/airport-arrival/`
- `/travel-guide/getting-around/`
- `/travel-guide/best-time-to-visit/`
- `/travel-guide/first-time-visitors/`
- `/travel-guide/money-tipping/`
- `/travel-guide/packing-list/`
- `/travel-guide/safety/`

## Sources / live-check anchors used

- Huatulco Airport information and transfer references.
- Taxi Huatulco transfer reference.
- INAH Bocana del Río Copalita listings.
- Local/operator comparison anchors including Paraiso Huatulco, Huatulco Salvaje, and Aventura Mundo Huatulco.
- Mazunte / turtle-center context.
- Las Parotas / Tangolunda golf current-status cross-check references.

## Remaining editorial judgment

This pass fixes the specific thinness problem in the three called-out sections. It does not solve the separate known photo/media trust gaps for Organo, Chachacual, Conejos, and Copalita archaeology. DNS remains blocked until explicit approval.
