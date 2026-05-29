# Tourist Attraction & Destination Page Structures Guide

Source: Mogens' approved tourism page-structure guide plus Oso Hermes implementation recommendations.
Last updated: 2026-05-29

Use this as a canonical page-contract reference for tourism sites such as Top El Salvador, Top San José del Cabo, Top Los Cabos, Top Todos Santos, Top Cancun Mexico, Top Huatulco, and future destination brands.

## Purpose

This guide defines repeatable, SEO-friendly, visitor-useful page structures by content type. It should be used during:

1. New site planning and route maps.
2. Static page generation.
3. Content-depth resets when pages feel thin or skeletal.
4. QA before preview deployment or production DNS approval.
5. Cross-site standardization across the tourism portfolio.

The standard is not “more words.” The standard is: can a real visitor decide where to go, how to get there, what it costs or requires, what to avoid, what to pair nearby, and which related page to read next?

## General Best Practices

Applies to most pages:

- Hero first: strong visual hero, one clear H1, benefit-driven subheadline, primary CTA, secondary CTA.
- Mobile-first and fast: optimized WebP/AVIF where possible, lazy-loaded images below the fold, responsive tables/cards.
- Scannable content: short paragraphs, bullets, H2/H3 hierarchy, meaningful section labels, icon support where useful.
- Multiple CTAs: place relevant CTAs at natural decision points, not only at the bottom.
- Authentic visuals: use destination-specific photos. Track source, license, credit, and page target.
- SEO foundations: unique title, meta description, canonical, OpenGraph, one H1, descriptive internal links.
- Schema: use truthful JSON-LD only. TouristAttraction as base where appropriate; Beach, LandmarkOrHistoricalBuilding, Church, TouristDestination, Place, or LocalBusiness only when accurate and backed by page content.
- Trust and practicality: honest limitations, source/live-check notes, current logistics, safety, weather/season caveats.
- Internal linking: every page should connect to its parent hub, related sibling pages, relevant itinerary/practical guide, and a next-step CTA.
- No fake features: do not add fake booking, fake search, fake reviews, fake ratings, fake maps, or placeholder widgets.

## Portfolio-Level Rule

Use this guide as a shared page contract, but adapt the content, palette, hero/media, and decision logic per destination. Do not make the sites clones.

Examples:
- Top Los Cabos: regional umbrella, comparison and base-choice logic first; deep local intent should point to sister sites.
- Top San José del Cabo: historic town, marina, beaches, art, dining, SJD arrival, calmer upscale tone.
- Top Todos Santos: Pueblo Mágico, Pacific/desert/art/history, beach safety, day trips, boutique stays.
- Top Cancun Mexico: large resort/urban/archaeology/transport/sargassum decision engine.
- Top El Salvador: countrywide surf/volcano/town/route planning with safety and drive-time clarity.
- Top Huatulco: nine-bay comparison, boat tours, HUX airport, beach access/facilities, Oaxaca coast context.

## 1. Beach / Nature Attraction Page

Best for: beaches, bays, waterfalls, viewpoints, parks, natural outdoor sites.

Required structure:

1. Hero section
   - Destination-specific image/video.
   - H1 with primary keyword.
   - Subheadline explaining who it is best for.
   - CTAs: Plan your visit, View map/how to get there, See nearby/itinerary.

2. Quick overview
   - Short description of the vibe.
   - Best for / not best for.
   - Recommended visit length.

3. Highlights / why visit
   - Grid or icon cards: water/sand/setting, atmosphere, facilities, access, family fit, photo value.

4. Things to do and activities
   - Swimming, snorkeling, surfing, walking, photography, food, boat tours, wildlife, sunset.
   - Be explicit about conditions and ability level.

5. Location, access and map
   - Directions from main hubs.
   - Parking, taxi, bus, boat, walking, accessibility.
   - Reliable map or orientation-card fallback plus external map link.

6. Practical visitor information
   - Best time, facilities, restrooms, shade, food, rentals, safety, what to bring, local rules, cash/card reality.

7. Photo and video gallery
   - Route-specific media with alt text and credits.
   - Avoid generic stock for named places unless clearly labelled as mood/context.

8. Reviews / trust signals
   - Only use real reviews or quote official/local context. Do not invent aggregate ratings.

9. FAQ
   - Accordion near the end, after main editorial content.
   - 3 to 6 useful questions: crowds, family, parking, water conditions, access, facilities.

10. Nearby attractions and related content
   - Link sibling beaches/nature pages, town/base pages, itineraries, food, travel-guide pages.

11. Final CTA
   - Route to itinerary, map, destination hub, or planning guide.

Key emphasis: sensory experience, activities, safety, access, facilities, and honest fit.

## 2. Historical Building / Cathedral / Landmark Page

Best for: churches, cathedrals, missions, ruins, museums, monuments, heritage buildings.

Required structure:

1. Hero section
   - Exterior, interior, or iconic feature.
   - H1 focused on significance.

2. Introduction and significance
   - Why it matters culturally, religiously, architecturally, historically.
   - Why a visitor should include it.

3. History and story
   - Timeline or narrative.
   - Construction, important periods, restorations, controversy/legend when relevant.

4. Architecture / must-see features
   - Specific features with plain-language explanations.
   - Close-up images where possible.

5. Visitor information
   - Hours, ticket/access rules, dress code, photography, etiquette, accessibility, duration.
   - Use live-check wording for volatile facts.

6. Tours and experiences
   - Guided tours, audio guides, rooftop access, special events, nearby museum pairing.

7. Photo/video gallery
8. Reviews/trust signals
9. FAQ
10. Nearby attractions
11. Final CTA

Key emphasis: respect, education, cultural context, and clear logistics.

Schema: TouristAttraction plus LandmarkOrHistoricalBuilding, Church, Museum, Place, or TouristDestination only when accurate.

## 3. Smaller Town / Pueblo / Day Trip Page

Best for: villages, towns, pueblos, small resort areas, side-trip bases.

Required structure:

1. Hero section
   - Atmospheric village, street, coast, mountain, plaza, or local-life image.
   - H1 positioning it as a specific type of escape or base.

2. Quick overview / why visit
   - What makes it different from the main destination.
   - Best for / not best for.
   - Day trip vs overnight verdict.

3. How to get there
   - Critical section.
   - Options by car, bus, taxi, boat, tour, shuttle.
   - Time, friction, approximate cost category, safety/road notes, last-return risk.
   - Map or orientation-card fallback.

4. Things to do and highlights
   - Walks, beaches, food, viewpoints, markets, galleries, hikes, boat trips, local events.

5. Where to eat and stay
   - Light recommendations or directory-style cards if page intent warrants it.
   - Link deeper dining/stay pages if available.

6. Practical day-trip tips
   - Best time, what to bring, cash, independent vs tour, safety, weather, accessibility.

7. Photo gallery
8. Reviews/trust signals
9. FAQ
10. Plan your visit / related content

Key emphasis: transportation, realistic pacing, authentic vibe, and relationship to the main hub.

Long-tail SEO: “day trip to [town] from [main destination]”, “is [town] worth visiting”, “how to get from [hub] to [town]”.

## 4. Homepage

Purpose: discovery and navigation hub.

Required structure:

- Large hero with value proposition and visitor-first positioning.
- Quick category navigation: beaches/destinations, things to do, where to stay, food, itineraries, travel guide.
- Featured highlights with real destination context.
- Decision module: best areas, trip styles, first-time choices, seasonal caveats.
- Itinerary teasers.
- Trust/freshness strip: practical guide, source policy, image credits, update date if relevant.
- Strong CTAs to high-intent guides.

Avoid:
- Generic “paradise awaits” copy.
- A homepage that only advertises cards without helping users choose.
- Inert chips that look clickable.
- Public “preview/source/process” language.

## 5. Things to Do / Activities Hub

Purpose: browse and filter experiences.

Required structure:

- Hero + quick verdict on how to choose activities.
- Category filters or scannable sections: water, culture, food, nature, nightlife, family, rainy-day, free/low-cost.
- Cards with image/icon, short description, best for, duration, effort, cost category, link.
- “How to choose” decision table.
- Safety/seasonality notes.
- Links to detail pages, itineraries, and booking/live-check resources where appropriate.

## 6. Where to Stay / Accommodations

Purpose: comparison and booking support.

Required structure:

- Area/base decision guide first: who should stay where and why.
- Neighborhood/zone cards with pros, tradeoffs, beach/access, nightlife, transport.
- Hotel style cards: all-inclusive, boutique, family, budget, nightlife, romantic, surf, remote.
- Map/orientation section.
- Booking/live-check CTA.
- Internal links to neighborhood, beach, transport, itinerary pages.

Avoid thin hotel lists without base-choice logic.

## 7. Where to Eat / Restaurants & Dining

Purpose: food discovery and decision support.

Required structure:

- Food identity intro: local dishes, dining culture, meal timing, price/cash/reservation reality.
- Area-by-area dining guidance.
- Cuisine/type filters: seafood, tacos, fine dining, markets, coffee, nightlife, family.
- Named directory cards only where useful and verifiable.
- Dish/photo cards when available.
- Live-check/source CTAs for opening hours and reservations.

## 8. Itineraries and Suggested Plans

Purpose: help visitors plan time.

Required structure:

- Hero with audience and trip length.
- Quick assumptions: arrival airport/base, pace, transport, season, who it suits.
- Day-by-day plan. If title says 3 days, include Day 1, Day 2, Day 3.
- Each day: morning, afternoon, evening, transport/routing, backup/Plan B.
- Map/orientation or route logic.
- Estimated cost categories, not brittle exact prices unless sourced and live-checked.
- Customization options by traveler type.
- Links to detail pages for each stop.
- Printable/downloadable version when useful.

Avoid generic Morning/Afternoon/Evening blocks that do not match the promised number of days.

## 9. Practical Information / Visitor Essentials

Purpose: centralized logistics and friction reduction.

Required structure:

- Hub-style layout with clear sections: getting there, getting around, safety, weather, money, health, SIM/eSIM, packing, etiquette, accessibility.
- Topic-specific content. Do not use physical-place scaffold labels like “map and orientation” on abstract topics unless a map is genuinely useful.
- Tables/checklists for quick decisions.
- Official/live-check links for volatile rules and services.
- Internal links to arrival, airport, transport, weather/season, safety, itinerary pages.

## 10. Events and Festivals

Purpose: time-sensitive planning.

Required structure:

- Calendar/month/season organization.
- Date ranges with live-check caveats.
- Cards with what it is, where, who it suits, ticket/access reality, planning tips.
- Prominent upcoming events.
- Annual traditions page if exact dates change.

## 11. Neighborhoods / Areas Page

Purpose: base-choice and local orientation.

Required structure:

- Map-centric or orientation-card layout.
- Area cards with: vibe, best for, not best for, transport, beach/access, dining/nightlife, hotel style.
- Comparison table.
- Links to lodging, dining, beaches, itineraries.

## 12. Interactive Map / Explorer

Purpose: map-first browsing.

Required structure:

- Clear categories/layers.
- Honest visible point counts.
- Clickable points linking to detail pages.
- Selected place marker/label/popup.
- Mobile-friendly list fallback.
- Do not fake map interactivity; if no map exists, use an orientation-card fallback.

## 13. Blog / Travel Guide Article

Purpose: long-form SEO support and planning depth.

Required structure:

- Strong title answering a specific visitor question.
- Intro verdict.
- Clear H2 structure.
- Original practical advice, not generic filler.
- Related guide links after main content or near the end.
- Visible sources/live-checks where helpful.
- FAQ after main editorial content.

## Additional Recommendations and Improvements

### A. Add a “quick verdict” module to most pages

Recommended fields:
- Best for
- Skip if
- Time needed
- Easiest access
- Best time
- Main tradeoff

This helps pages feel useful immediately and improves snippet value.

### B. Add “choose / avoid / pair with” logic

For decision pages and attraction pages, include:
- Choose this if...
- Avoid this if...
- Pair it with...
- Better alternative when...

This is often more useful than a long description.

### C. Treat maps as trust elements

Every place page should have either:
- A reliable map embed that visually renders; or
- A designed orientation sketch/card with external Google Maps/OpenStreetMap links.

Blank or fragile embeds are worse than no map.

### D. Add source/live-check boxes for volatile facts

Use for:
- Hours
- Prices
- tickets
- seasonal access
- ferry/boat/shuttle schedules
- safety advisories
- parks/ruins/museums
- operator availability

Wording should be visitor-facing: “Verify before you go,” not “source map.”

### E. Schema must be truthful

Only include aggregateRating, offers, openingHours, address, geo, sameAs, or business details when actually known and represented on-page. Do not invent ratings, coordinates, or opening hours.

### F. Media standards

- Every priority route needs at least one relevant hero image.
- Use owner/sister-site media first when rights are clear.
- Open-license media must be credited visibly on image-credits page.
- Generic stock can support mood/context but should not carry named destination pages.
- Alt text should describe the image and place, not keyword-stuff.

### G. Internal link contract

Each detail page should link to:
- Parent hub.
- 2 to 4 sibling/nearby pages.
- 1 practical guide.
- 1 itinerary or trip-planning page.
- 1 final CTA destination.

Each hub page should expose child pages with obvious visitor-facing card links. Detail routes that only work by direct URL are a launch blocker.

### H. QA gates

Before preview deployment or production review, verify:

- All routes exist and internal links resolve.
- One H1 per page.
- Title/meta/canonical present.
- No placeholder/coming-soon/TODO/scaffold/process text visible.
- FAQ appears after main content.
- Promised itinerary day count matches actual day cards.
- Maps render or have intentional fallback.
- Images exist, load, and have alt text.
- Third-party images have visible credits.
- Schema is valid and truthful.
- Representative pages pass browser visual QA, not just string tests.

## Implementation Pattern Across the Current Top Sites

For each site, add or maintain a local copy/reference file such as:

- PROJECT_PLAN.md: route map and phases.
- CONTENT_SOURCE_MAP.md or CONTENT_ENRICHMENT_SOURCES.md: source usage and copy rules.
- CONTENT_STANDARDS.md: local adaptation of this page contract.
- MEDIA_SOURCES.md or media-sources.json: image provenance.
- STATUS.md: current state, preview URL, blockers, next actions.

Recommended adoption order:

1. Top Huatulco
   - Apply full beach/nature page contract to all 9 bay pages.
   - Add or improve HUX airport, boat tours, towns, itineraries, and practical guide pages.

2. Top San José del Cabo
   - Apply landmark/town/dining/beach contracts.
   - Emphasize art district, historic center, Puerto Los Cabos, SJD arrival, nearby beaches, dining.

3. Top Los Cabos
   - Use regional umbrella variant: comparison, base choice, trip style, regional itinerary logic.
   - Link deeper local intent to San José/Cabo/Todos Santos sister sites where appropriate.

4. Top Todos Santos
   - Apply pueblo/day-trip, beach safety, history/heritage, boutique stay, food/art contracts.
   - Strong Pacific safety and realistic transport/pacing.

5. Top Cancun Mexico
   - Apply large-destination contracts: zones, beaches, archaeology, sargassum/weather, airport/transport, itineraries.
   - Needs strong decision tables and source/live-check modules.

6. Top El Salvador
   - Apply countrywide variant: regions, surf towns, volcanoes, beaches, routes, safety, drive times, itineraries.
   - Avoid one-city template; make route planning first-class.

## Agent Usage Rule

When building or improving a Top* tourism site:

1. Load the static-tourism-sites skill.
2. Read this reference.
3. Classify every route by page type.
4. Apply the matching page contract.
5. Add site-specific modules and avoid clone-like repetition.
6. Run tests, lint, build, browser QA, preview deploy, commit, and Command Center/Kanban update.
7. Keep production DNS gated until explicit approval.


---

# Local Adoption Notes: Top Huatulco

Role: Nine-bay Oaxaca coast guide: bay comparison, HUX airport, boat tours, beach facilities/access, towns, coastal day trips.

Priority page contracts to apply first:
- All 9 bay pages using the beach/nature contract
- Destinations hub with compare/choose logic
- HUX airport and getting-around guides
- Boat tour, snorkeling, and beach-access practical pages
- Itineraries that cluster bays realistically

Important avoidance rule: Do not leave bay pages as generic beach blurbs; access, facilities, water conditions, and best-for logic are the point.

Implementation rule: when adding or revising pages here, run `python3 scripts/audit-tourism-standards.py` in addition to the repo's normal `npm run test`, `npm run lint`, and `npm run build` gates where available.
