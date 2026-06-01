from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
IGNORE = {'node_modules', 'dist'}
REQUIRED_ROUTES = [
    '/', '/destinations/', '/destinations/tangolunda/', '/destinations/chahue/',
    '/destinations/santa-cruz/', '/destinations/el-maguey/', '/destinations/organo/',
    '/destinations/cacaluta/', '/destinations/chachacual/', '/destinations/san-agustin/',
    '/destinations/conejos/', '/travel-guide/', '/travel-guide/airport-arrival/',
    '/travel-guide/best-time-to-visit/', '/travel-guide/safety/', '/travel-guide/getting-around/',
    '/itineraries/', '/itineraries/3-days-huatulco/', '/things-to-do/', '/food-culture/',
    '/tours/', '/beaches/', '/towns-cities/', '/towns-cities/la-crucecita/', '/image-credits/'
]
BANNED = ['lorem ipsum', 'coming soon', 'todo', 'fixme', 'placeholder', 'AI slop']
BAD_LINKS = ['san-agust-n', '/rgano/', '/chahu/', 'puerto-ngel']
ENTITY_DEPTH_REQUIREMENTS = {
    '/food-culture/': ['data-entity-depth=\'food-culture\'', 'Terra-Cotta', 'El Sabor de Oaxaca', 'Mercader', 'Casa Bocana', 'Mercado 3 de Mayo', 'data-visible-sources=\'true\''],
    '/tours/': ['data-entity-depth=\'tours\'', 'Oceanico Huatulco', 'Huatulco Watersports', 'Tours en Huatulco', 'Pilo Vázquez', 'Marinautica Huatulco', 'data-visible-sources=\'true\''],
    '/things-to-do/snorkeling/': ['data-entity-depth=\'snorkeling\'', 'Maguey', 'Chachacual', 'Cacaluta', 'Santa Cruz marina operators'],
    '/things-to-do/boat-tours/': ['data-entity-depth=\'boat-tours\'', 'Start at Santa Cruz', 'classic shared panga', 'small-group nature boat', 'private/custom boat', 'data-visible-sources=\'true\''],
    '/things-to-do/copalita-archaeology/': ['data-entity-depth=\'copalita\'', 'Bocana del Río Copalita', 'INAH Bocana del Río Copalita listing', 'Bocana beach restaurants', 'data-visible-sources=\'true\''],
    '/things-to-do/la-crucecita-market/': ['data-entity-depth=\'la-crucecita-market\'', 'Mercado 3 de Mayo', 'La Crucecita zócalo', 'Terra-Cotta', 'El Sabor de Oaxaca'],
}
MEDIA_REQUIREMENTS = {
    '/destinations/chahue/': ['data-approved-route-media=\'true\'', 'Huatulco', '/images/photos/huatulco-huatulco-jpg-destinations-chahue.webp'],
    '/destinations/cacaluta/': ['data-approved-route-media=\'true\'', 'CacalutaPlaya', '/images/photos/huatulco-cacalutaplaya-jpg-destinations-cacaluta.webp'],
    '/things-to-do/snorkeling/': ['data-approved-route-media=\'true\'', 'Playa Riscalillo', '/images/photos/huatulco-playa-riscalillo-bah-as-de-huatulco-1-jpg-mosaic.webp'],
    '/things-to-do/boat-tours/': ['data-approved-route-media=\'true\'', 'Maguey Bay', '/images/photos/huatulco-maguey-bay-jpg-mosaic.webp'],
    '/food-culture/': ['data-approved-route-media=\'true\'', 'La Crucecita Oaxaca Mexico'],
    '/itineraries/5-days-oaxaca-coast/': ['data-approved-route-media=\'true\'', 'Bahia San Agustin Huatulco camping', '/images/photos/huatulco-bahia-san-agustin-huatulco-camping-webp.webp'],
    '/things-to-do/copalita-archaeology/': ['data-approved-route-media=\'true\'', 'data-copalita-viewpoint-media=\'true\'', 'La Bocana beach viewed from a Copalita Eco-Archaeological Park lookout', '/images/photos/huatulco-vista-de-la-playa-la-bocana-huatulco-jpg-things-to-do-copalita-archaeology.webp'],
    '/image-credits/': ['data-approved-image-credits=\'huatulco\'', 'Huatulco.jpg', 'CacalutaPlaya.JPG', 'La Crucecita Oaxaca Mexico.jpg', 'Vista de la playa La Bocana, Huatulco.jpg'],
}
RESPONSIVE_REQUIREMENTS = {
    '/destinations/': [
        'data-destinations-comparison',
        'data-mobile-table-cards',
        'data-mobile-table-card',
        'data-responsive-table=\'desktop-scroll\'',
        'md:hidden',
        'md:block',
    ],
}
LAUNCH_UTILITY_REQUIREMENTS = {
    '/': ['data-launch-decision-spine=\'true\'', 'data-launch-path-link=\'first-time\'', 'Which bay fits today?', 'Where do meals fit?', 'Open first-time guide →'],
    '/towns-cities/': ['data-hub-path-link=\'la-crucecita\'', 'href=\'/towns-cities/la-crucecita/\'', 'href=\'/towns-cities/puerto-angel/\''],
    '/itineraries/': ['data-hub-child-cta=\'itinerary-depth\'', 'href=\'/itineraries/4-days-relax-snorkel/\'', 'href=\'/itineraries/snorkel-boat-day/\''],
    '/travel-guide/': ['data-hub-child-cta=\'travel-guide-depth\'', 'href=\'/travel-guide/getting-around/\'', 'href=\'/travel-guide/packing-list/\''],
}
SITEWIDE_STRUCTURE_EXEMPT_ROUTES = {'/', '/about/', '/privacy/', '/terms/', '/image-credits/', '/media-review/'}
SITEWIDE_STRUCTURE_REQUIREMENTS = {
    '/destinations/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: pick the bay by the day you want', 'data-structure-verdict=\'true\''],
    '/beaches/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: choose beaches by conditions', 'data-responsive-table=\'structure-decision\''],
    '/towns-cities/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: use each town for a specific job', 'data-guide-nav'],
    '/food-culture/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: plan meals around town nights', 'data-structure-next-links=\'true\''],
    '/tours/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: buy clarity', 'data-responsive-table=\'structure-decision\''],
    '/things-to-do/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: choose the activity by the kind of day', 'data-guide-nav'],
    '/itineraries/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: choose the route by pace', 'data-guide-nav'],
    '/travel-guide/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: solve logistics before choosing more beaches', 'data-guide-nav'],
    '/towns-cities/la-crucecita/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: use La Crucecita', 'data-guide-nav'],
    '/towns-cities/santa-cruz/': ['data-sitewide-structure=\'tourism-guide\'', 'Quick verdict: use Santa Cruz', 'data-guide-nav'],
}

VISITOR_REFERENCE_REQUIREMENTS = {
    '/towns-cities/': ['data-priority-guide-depth=\'visitor-reference\'', 'Choose by what you want to do', 'La Crucecita solves food and errands', 'Simple route logic'],
    '/towns-cities/la-crucecita/': ['data-priority-guide-depth=\'visitor-reference\'', 'Terra-Cotta', 'Mercado 3 de Mayo', 'Mini route for a first visit'],
    '/towns-cities/santa-cruz/': ['data-priority-guide-depth=\'visitor-reference\'', 'boat departures', 'La Crucecita for dinner', 'Mini route for a first visit'],
    '/towns-cities/copalita/': ['data-priority-guide-depth=\'visitor-reference\'', 'Bocana del Río Copalita', 'INAH', 'Mini route for a first visit'],
    '/towns-cities/mazunte/': ['data-priority-guide-depth=\'visitor-reference\'', 'Mexican Turtle Center', 'Punta Cometa', 'San Agustinillo'],
    '/towns-cities/puerto-angel/': ['data-priority-guide-depth=\'visitor-reference\'', 'working coastal town and fishing port', 'Zipolite', 'San Agustinillo'],
    '/things-to-do/': ['data-section-depth-reset=\'true\'', 'Choose activities by the kind of day you want', 'A boat day depends on sea conditions'],
    '/things-to-do/boat-tours/': ['data-section-depth-reset=\'true\'', 'Quick verdict', 'Choose it, skip it, or pair it correctly', 'How this usually fits into a real trip'],
    '/things-to-do/snorkeling/': ['data-section-depth-reset=\'true\'', 'condition-dependent', 'Local options to check', 'Better backup idea'],
    '/things-to-do/golf-tangolunda/': ['data-section-depth-reset=\'true\'', 'verify-before-booking', 'Las Parotas', 'Better backup idea'],
    '/itineraries/': ['data-section-depth-reset=\'true\'', 'Choose the itinerary by how much movement your group wants', '3 nights', '5+ nights'],
    '/itineraries/4-days-relax-snorkel/': ['data-section-depth-reset=\'true\'', 'data-itinerary-day=\'Day 4\'', 'Base, meals, and pacing rules', 'Mercado 3 de Mayo'],
    '/itineraries/snorkel-boat-day/': ['data-section-depth-reset=\'true\'', 'data-itinerary-day=\'Day plan\'', 'Backup plan', 'Santa Cruz'],
    '/travel-guide/': ['data-section-depth-reset=\'true\'', 'Solve the practical questions before you choose beaches', 'airport transfer', 'Getting around'],
    '/travel-guide/airport-arrival/': ['data-section-depth-reset=\'true\'', 'Step-by-step', 'first-hour priorities', 'Same-week check'],
    '/travel-guide/getting-around/': ['data-section-depth-reset=\'true\'', 'Decision rules that prevent friction', 'Short taxi hop', 'Rental car'],
    '/travel-guide/best-time-to-visit/': ['data-section-depth-reset=\'true\'', 'Dry-season beach trip', 'Shoulder trip', 'Rainier/warmer period'],
    '/travel-guide/safety/': ['data-section-depth-reset=\'true\'', 'Remote/scenic beaches', 'water conditions', 'return transport'],
    '/travel-guide/first-time-visitors/': ['data-section-depth-reset=\'true\'', 'Choose a base', '3 nights', '5+ nights'],
    '/travel-guide/money-tipping/': ['data-section-depth-reset=\'true\'', 'small bills', 'Markets/small food', 'taxis'],
    '/travel-guide/packing-list/': ['data-section-depth-reset=\'true\'', 'Boat/snorkel day', 'Dry bag', 'town/culture kit'],
    '/food-culture/': ['data-priority-guide-depth=\'visitor-reference\'', 'data-food-directory=\'true\'', 'A better food plan for 3 to 5 days', 'Bay seafood palapas'],
}

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs=[]
        self.title=''
        self.desc=False
        self.canon=False
        self._in_title=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='a' and attrs.get('href'):
            self.hrefs.append(attrs['href'])
        if tag=='meta' and attrs.get('name')=='description' and attrs.get('content'):
            self.desc=True
        if tag=='link' and attrs.get('rel')=='canonical' and attrs.get('href'):
            self.canon=True
        if tag=='title':
            self._in_title=True
    def handle_endtag(self, tag):
        if tag=='title': self._in_title=False
    def handle_data(self, data):
        if self._in_title: self.title += data

def route_file(route):
    return ROOT/'index.html' if route=='/' else ROOT/route.strip('/')/'index.html'

errors=[]
for route in REQUIRED_ROUTES:
    if not route_file(route).exists():
        errors.append(f'Missing required route {route}')

for p in ROOT.rglob('index.html'):
    if any(part in IGNORE for part in p.parts) or 'media-review' in p.parts:
        continue
    txt=p.read_text(encoding='utf-8', errors='ignore')
    rel='/' if p.name=='index.html' and p.parent==ROOT else '/' + str(p.parent.relative_to(ROOT)).strip('/') + '/'
    parser=Parser(); parser.feed(txt)
    if not parser.title.strip(): errors.append(f'{rel} missing title')
    if not parser.desc: errors.append(f'{rel} missing meta description')
    if not parser.canon: errors.append(f'{rel} missing canonical')
    low=txt.lower()
    for b in BANNED:
        if b.lower() in low:
            errors.append(f'{rel} has banned text {b}')
    for b in BAD_LINKS:
        if b in txt:
            errors.append(f'{rel} has bad slug/link {b}')
    for marker in ENTITY_DEPTH_REQUIREMENTS.get(rel, []):
        if marker not in txt:
            errors.append(f'{rel} missing entity-depth marker/content {marker}')
    for marker in MEDIA_REQUIREMENTS.get(rel, []):
        if marker not in txt:
            errors.append(f'{rel} missing approved-media marker/content {marker}')
    for marker in RESPONSIVE_REQUIREMENTS.get(rel, []):
        if marker not in txt:
            errors.append(f'{rel} missing responsive marker/content {marker}')
    for marker in VISITOR_REFERENCE_REQUIREMENTS.get(rel, []):
        if marker not in txt:
            errors.append(f'{rel} missing visitor-reference marker/content {marker}')
    for marker in LAUNCH_UTILITY_REQUIREMENTS.get(rel, []):
        if marker not in txt:
            errors.append(f'{rel} missing launch-utility marker/content {marker}')
    for marker in SITEWIDE_STRUCTURE_REQUIREMENTS.get(rel, []):
        if marker not in txt:
            errors.append(f'{rel} missing sitewide-structure marker/content {marker}')
    if rel not in SITEWIDE_STRUCTURE_EXEMPT_ROUTES and '/media-review/' not in rel:
        if "data-subject-led-guide='true'" not in txt and 'data-subject-led-guide="true"' not in txt:
            errors.append(f'{rel} missing subject-led guide marker')
        if "data-sitewide-structure='tourism-guide'" not in txt and 'data-sitewide-structure="tourism-guide"' not in txt:
            errors.append(f'{rel} missing sitewide tourism-guide marker')
        if 'Quick verdict' not in txt:
            errors.append(f'{rel} missing Quick verdict content')
    if '<table' in txt and 'data-responsive-table' not in txt:
        errors.append(f'{rel} has table without data-responsive-table wrapper')
    for href in parser.hrefs:
        if href.startswith(('http://','https://','mailto:','#')): continue
        if href.startswith('/assets/') or href.startswith('/icons.svg'): continue
        target = ROOT/'index.html' if href=='/' else ROOT/href.strip('/')/'index.html'
        if not target.exists():
            errors.append(f'{rel} broken internal link {href}')

if not (ROOT/'public/robots.txt').exists(): errors.append('Missing robots.txt')
if not (ROOT/'public/sitemap.xml').exists(): errors.append('Missing sitemap.xml')
if not (ROOT/'LAUNCH_GAP_AUDIT.md').exists(): errors.append('Missing launch gap audit')
if not (ROOT/'SITEWIDE_CONTENT_STRUCTURE_AUDIT.md').exists(): errors.append('Missing sitewide content structure audit')
robots = (ROOT/'public/robots.txt').read_text(encoding='utf-8') if (ROOT/'public/robots.txt').exists() else ''
if 'Disallow: /media-review/' not in robots: errors.append('robots.txt must disallow review-only media board')
if 'Sitemap: https://tophuatulco.com/sitemap.xml' not in robots: errors.append('robots.txt missing sitemap directive')
if (ROOT/'public/sitemap.xml').exists():
    sitemap = (ROOT/'public/sitemap.xml').read_text(encoding='utf-8')
    public_routes = []
    for p in ROOT.rglob('index.html'):
        if any(part in IGNORE or part in {'.git'} for part in p.parts):
            continue
        rel = '/' if p.parent == ROOT else '/' + str(p.parent.relative_to(ROOT)).strip('/') + '/'
        if rel.startswith('/media-review/'):
            continue
        public_routes.append(rel)
    for rel in public_routes:
        loc = 'https://tophuatulco.com/' if rel == '/' else 'https://tophuatulco.com' + rel
        if loc not in sitemap:
            errors.append(f'sitemap.xml missing {loc}')
    if 'https://tophuatulco.com/media-review/' in sitemap:
        errors.append('sitemap.xml must not include review-only media board')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Static site verification passed')
