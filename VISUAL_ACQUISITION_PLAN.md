# Top Huatulco visual acquisition plan

Date: 2026-05-29
Status: active pre-launch media pass

## Why this is the next step

The content spine is now much stronger: all nine bay pages and the 3-day / 5-day itinerary pages have decision-led visitor guidance. The biggest remaining launch blocker is visual credibility.

Current inventory is too thin for a public destination site:

- 12 local image files total.
- Most are inherited Top El Salvador / Lovable assets.
- Only one image path is referenced repeatedly in public Huatulco pages: `/images/lovable/hero-traveler.jpg`.
- No Huatulco-specific media manifest exists yet.
- No route-specific bay imagery exists for Tangolunda, Chahué, Santa Cruz, El Maguey, Órgano, Cacaluta, Chachacual, San Agustín, or Conejos.

Production DNS should stay gated until this media gap is fixed.

## Source rules

1. Prefer owned or sister-site Huatulco/Oaxaca coast photos if available.
2. Use real, location-specific open-license photos when owned photos are not available.
3. Track every source in a machine-readable manifest and visible `/image-credits/` page.
4. Avoid Google Maps, TripAdvisor, Instagram, random blog photos, all-rights-reserved Flickr, and non-commercial/no-derivatives licenses.
5. Use AI only for conservative crop/color/sharpness/upscale on license-safe source photos. Do not invent documentary-looking Huatulco beaches or landmarks.
6. Stock/generic photos may support practical guide mood pages, but not specific bay pages.

## Launch-critical routes needing images

### Tier 1: route-specific images required before public launch

- `/` homepage: 8-12 authentic Huatulco/Oaxaca coast images.
- `/destinations/` bays hub: one representative image per bay card.
- `/destinations/tangolunda/`
- `/destinations/chahue/`
- `/destinations/santa-cruz/`
- `/destinations/el-maguey/`
- `/destinations/organo/`
- `/destinations/cacaluta/`
- `/destinations/chachacual/`
- `/destinations/san-agustin/`
- `/destinations/conejos/`
- `/itineraries/3-days-huatulco/`
- `/itineraries/5-days-oaxaca-coast/`

### Tier 2: important before launch review

- `/things-to-do/boat-tours/`
- `/things-to-do/snorkeling/`
- `/things-to-do/copalita-archaeology/`
- `/things-to-do/la-crucecita-market/`
- `/things-to-do/mazunte-day-trip/`
- `/travel-guide/first-time-visitors/`
- `/travel-guide/airport-arrival/`
- `/travel-guide/getting-around/`
- `/travel-guide/safety/`
- `/food-culture/`

### Tier 3: useful supporting media

- Remaining beach/town/travel guide pages.
- Social/OG images.
- Small orientation graphics or maps if real photos are unavailable.

## Candidate review board requirements

Create a review-only board at `/media-review/` before wiring images into public pages. The board must:

- be noindexed;
- show thumbnail, route target, source URL, creator, license, derivative/commercial-use status, and notes;
- distinguish exact-place candidates from generic mood/context candidates;
- hide or reject PDFs, logos, watermarked images, all-rights-reserved images, and uncertain licenses;
- make it easy to approve/reject images for production use.

## Acceptance target for first media pass

A useful first pass is not the final media library. The first target is:

- 40-60 candidate images in the review board;
- at least 1 credible candidate for every Tier 1 route;
- 3-5 candidates each for Santa Cruz, Tangolunda, Cacaluta/Chachacual, San Agustín, and homepage hero/mosaic use;
- source metadata complete enough that approved assets can be safely promoted later.

## Next action

Build `src/data/visual-needs.json`, then source open-license candidates into `src/data/visual-candidates.json` and `/media-review/`.
