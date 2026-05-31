from pathlib import Path
import html

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'https://tophuatulco.com'


def write(path: str, text: str):
    p = ROOT / path
    p.write_text(text, encoding='utf-8')


def replace_once(path: str, old: str, new: str):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    if old not in text:
        raise SystemExit(f'Missing target in {path}: {old[:80]}')
    p.write_text(text.replace(old, new, 1), encoding='utf-8')

# 1) Homepage decision spine: a clear visitor path that is not another generic card grid.
home_spine = """
<section class='section-pad bg-white' data-launch-decision-spine='true'><div class='container-xl'>
  <div class='max-w-3xl'>
    <p class='eyebrow'>Fast planning path</p>
    <h2 class='mt-2 text-3xl'>Answer the four questions that shape a Huatulco trip</h2>
    <p class='mt-3 leading-7 text-ink/70'>Use these as the main route through the site. They are designed for visitors who need to make decisions quickly, not browse every page.</p>
  </div>
  <div class='mt-8 grid gap-5 md:grid-cols-2 xl:grid-cols-4'>
    <a class='card block p-6 hover:-translate-y-1 hover:shadow-soft transition' href='/travel-guide/first-time-visitors/' data-launch-path-link='first-time'>
      <span class='text-sm font-bold uppercase tracking-[.16em] text-primary'>1 · Start</span>
      <h3 class='mt-3 font-heading text-xl font-semibold text-ink'>What kind of Huatulco trip is this?</h3>
      <p class='mt-3 text-sm leading-6 text-ink/70'>Choose resort ease, town access, boat days, family pacing, or a west-coast side trip before locking the itinerary.</p><span class='mt-5 inline-flex text-sm font-bold text-primary'>Open first-time guide →</span>
    </a>
    <a class='card block p-6 hover:-translate-y-1 hover:shadow-soft transition' href='/destinations/' data-launch-path-link='bay-choice'>
      <span class='text-sm font-bold uppercase tracking-[.16em] text-primary'>2 · Bays</span>
      <h3 class='mt-3 font-heading text-xl font-semibold text-ink'>Which bay fits today?</h3>
      <p class='mt-3 text-sm leading-6 text-ink/70'>Compare Tangolunda, Chahué, Santa Cruz, Maguey, San Agustín, and boat-only bays by access and water conditions.</p><span class='mt-5 inline-flex text-sm font-bold text-primary'>Compare the bays →</span>
    </a>
    <a class='card block p-6 hover:-translate-y-1 hover:shadow-soft transition' href='/itineraries/4-days-relax-snorkel/' data-launch-path-link='first-itinerary'>
      <span class='text-sm font-bold uppercase tracking-[.16em] text-primary'>3 · Plan</span>
      <h3 class='mt-3 font-heading text-xl font-semibold text-ink'>What is the easiest good itinerary?</h3>
      <p class='mt-3 text-sm leading-6 text-ink/70'>Use the slower 4-day plan if you want beach time, one real snorkel morning, town food, and room for weather.</p><span class='mt-5 inline-flex text-sm font-bold text-primary'>Open the 4-day plan →</span>
    </a>
    <a class='card block p-6 hover:-translate-y-1 hover:shadow-soft transition' href='/food-culture/' data-launch-path-link='food-evening'>
      <span class='text-sm font-bold uppercase tracking-[.16em] text-primary'>4 · Evenings</span>
      <h3 class='mt-3 font-heading text-xl font-semibold text-ink'>Where do meals fit?</h3>
      <p class='mt-3 text-sm leading-6 text-ink/70'>Use La Crucecita for planned meals and errands; use the bays for seafood lunches tied to beach days.</p><span class='mt-5 inline-flex text-sm font-bold text-primary'>Plan food and evenings →</span>
    </a>
  </div>
</div></section>
""".strip()
replace_once('index.html', "</section>\n<section class='section-pad'><div class='container-xl'><p class='eyebrow'>Start here</p>", "</section>\n" + home_spine + "\n<section class='section-pad'><div class='container-xl'><p class='eyebrow'>Start here</p>")

# 2) Hub pages: turn decision cards into actual path cards with thumb-friendly links.
town_links = {
    'La Crucecita': '/towns-cities/la-crucecita/',
    'Santa Cruz': '/towns-cities/santa-cruz/',
    'Copalita / Bocana': '/towns-cities/copalita/',
    'Mazunte': '/towns-cities/mazunte/',
    'Puerto Ángel': '/towns-cities/puerto-angel/',
}
travel_links = {
    'Airport arrival': '/travel-guide/airport-arrival/',
    'Getting around': '/travel-guide/getting-around/',
    'Best time': '/travel-guide/best-time-to-visit/',
    'Safety': '/travel-guide/safety/',
    'Money & tipping': '/travel-guide/money-tipping/',
    'Packing': '/travel-guide/packing-list/',
}
itinerary_links = {
    '3 days': '/itineraries/3-days-huatulco/',
    '4 days relax + snorkel': '/itineraries/4-days-relax-snorkel/',
    '5 days Oaxaca coast': '/itineraries/5-days-oaxaca-coast/',
    'Snorkel + boat day': '/itineraries/snorkel-boat-day/',
}

def card_link_pass(path: str, mapping: dict[str, str], label: str):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    for title, href in mapping.items():
        marker = f"<h3 class='font-heading text-xl font-semibold text-ink'>{title}</h3>"
        start = text.find(marker)
        if start == -1:
            raise SystemExit(f'Missing card title {title} in {path}')
        close = text.find('</p></div>', start)
        if close == -1:
            raise SystemExit(f'Missing card close for {title} in {path}')
        insert = f"</p><a class='mt-5 inline-flex min-h-11 items-center justify-center rounded-full bg-primary px-5 py-2.5 text-sm font-bold text-white hover:brightness-110' data-hub-path-link='{html.escape(title.lower().replace(' ', '-'))}' href='{href}'>{label}</a></div>"
        text = text[:close] + insert + text[close+len('</p></div>'):]
    p.write_text(text, encoding='utf-8')

card_link_pass('towns-cities/index.html', town_links, 'Open town guide')
card_link_pass('travel-guide/index.html', travel_links, 'Open guide')
card_link_pass('itineraries/index.html', itinerary_links, 'Open itinerary')

# 3) Simple, generated launch files based on every public route except noindex review board.
routes = []
for p in sorted(ROOT.rglob('index.html')):
    if any(part in p.parts for part in {'.git','node_modules','dist'}):
        continue
    route = '/' if p.parent == ROOT else '/' + str(p.parent.relative_to(ROOT)).strip('/') + '/'
    if route == '/media-review/':
        continue
    routes.append(route)

def priority(route: str) -> str:
    if route == '/': return '1.0'
    if route in {'/destinations/','/itineraries/','/travel-guide/','/food-culture/','/towns-cities/'}: return '0.9'
    if route.startswith(('/destinations/','/itineraries/','/travel-guide/','/towns-cities/','/things-to-do/')): return '0.8'
    return '0.5'

items = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for route in routes:
    loc = DOMAIN + (route if route != '/' else '/')
    items.append(f"  <url><loc>{loc}</loc><changefreq>weekly</changefreq><priority>{priority(route)}</priority></url>")
items.append('</urlset>')
write('public/sitemap.xml', '\n'.join(items) + '\n')
write('public/robots.txt', "User-agent: *\nAllow: /\nDisallow: /media-review/\nSitemap: https://tophuatulco.com/sitemap.xml\n")

# 4) Reviewable gap audit for non-photo launch blockers and post-review work.
write('LAUNCH_GAP_AUDIT.md', """# Top Huatulco launch utility and trust audit

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
""")

print(f'launch utility pass complete: {len(routes)} public routes in sitemap')
