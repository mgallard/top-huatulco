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
    '/things-to-do/snorkeling/': ['data-entity-depth=\'snorkeling\'', 'Maguey / La Entrega', 'San Agustín', 'Chachacual', 'Cacaluta', 'Oceanico Huatulco'],
    '/things-to-do/boat-tours/': ['data-entity-depth=\'boat-tours\'', 'Start at Santa Cruz', 'Classic shared panga', 'Small-group nature boat', 'Private/custom boat', 'data-visible-sources=\'true\''],
    '/things-to-do/copalita-archaeology/': ['data-entity-depth=\'copalita\'', 'Bocana del Río Copalita', 'official INAH listing', 'Casa Bocana', 'data-visible-sources=\'true\''],
    '/things-to-do/la-crucecita-market/': ['data-entity-depth=\'la-crucecita-market\'', 'Mercado 3 de Mayo', 'Iglesia de La Crucecita', 'Terra-Cotta', 'El Sabor de Oaxaca'],
}
MEDIA_REQUIREMENTS = {
    '/destinations/chahue/': ['data-approved-route-media=\'true\'', 'Huatulco', '/images/photos/huatulco-huatulco-jpg-destinations-chahue.webp'],
    '/destinations/cacaluta/': ['data-approved-route-media=\'true\'', 'CacalutaPlaya', '/images/photos/huatulco-cacalutaplaya-jpg-destinations-cacaluta.webp'],
    '/things-to-do/snorkeling/': ['data-approved-route-media=\'true\'', 'Playa Riscalillo'],
    '/things-to-do/boat-tours/': ['data-approved-route-media=\'true\'', 'Maguey Bay'],
    '/food-culture/': ['data-approved-route-media=\'true\'', 'La Crucecita Oaxaca Mexico'],
    '/itineraries/5-days-oaxaca-coast/': ['data-approved-route-media=\'true\'', 'Bahia San Agustin Huatulco camping'],
    '/image-credits/': ['data-approved-image-credits=\'huatulco\'', 'Huatulco.jpg', 'CacalutaPlaya.JPG', 'La Crucecita Oaxaca Mexico.jpg'],
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
VISITOR_REFERENCE_REQUIREMENTS = {
    '/towns-cities/': ['data-priority-guide-depth=\'visitor-reference\'', 'Choose by what you want to do', 'La Crucecita solves food and errands', 'Simple route logic'],
    '/towns-cities/la-crucecita/': ['data-priority-guide-depth=\'visitor-reference\'', 'Terra-Cotta', 'Mercado 3 de Mayo', 'Mini route for a first visit'],
    '/towns-cities/santa-cruz/': ['data-priority-guide-depth=\'visitor-reference\'', 'boat departures', 'La Crucecita for dinner', 'Mini route for a first visit'],
    '/towns-cities/copalita/': ['data-priority-guide-depth=\'visitor-reference\'', 'Bocana del Río Copalita', 'INAH', 'Mini route for a first visit'],
    '/towns-cities/mazunte/': ['data-priority-guide-depth=\'visitor-reference\'', 'Mexican Turtle Center', 'Punta Cometa', 'San Agustinillo'],
    '/towns-cities/puerto-angel/': ['data-priority-guide-depth=\'visitor-reference\'', 'working coastal town and fishing port', 'Zipolite', 'San Agustinillo'],
    '/itineraries/': ['data-priority-guide-depth=\'visitor-reference\'', 'How to choose your plan', 'protects calm mornings', 'Snorkel + boat day'],
    '/itineraries/4-days-relax-snorkel/': ['data-priority-guide-depth=\'visitor-reference\'', 'Base and pacing strategy', 'data-itinerary-day=\'4\'', 'Mercado 3 de Mayo'],
    '/itineraries/snorkel-boat-day/': ['data-priority-guide-depth=\'visitor-reference\'', 'data-itinerary-day=\'4\'', 'Maguey/La Entrega', 'Santa Cruz'],
    '/travel-guide/': ['data-priority-guide-depth=\'visitor-reference\'', 'Start with logistics, then pick beaches', 'Airport arrival', 'Getting around'],
    '/travel-guide/airport-arrival/': ['data-priority-guide-depth=\'visitor-reference\'', 'authorized airport taxi/transport desk', 'Tangolunda, Chahué, Santa Cruz'],
    '/travel-guide/getting-around/': ['data-priority-guide-depth=\'visitor-reference\'', 'Taxi for town/bay loops', 'boat for bay-hopping', 'rental for west along the Oaxaca coast day trips'],
    '/travel-guide/best-time-to-visit/': ['data-priority-guide-depth=\'visitor-reference\'', 'Green-season travel', 'Holiday periods', 'calm morning'],
    '/travel-guide/safety/': ['data-priority-guide-depth=\'visitor-reference\'', 'water, heat, transport', 'flags, swell', 'Remote beaches'],
    '/travel-guide/first-time-visitors/': ['data-priority-guide-depth=\'visitor-reference\'', 'Tangolunda/resort comfort', 'La Crucecita food/errands', 'three anchors'],
    '/travel-guide/money-tipping/': ['data-priority-guide-depth=\'visitor-reference\'', 'small bills', 'taxis, markets, tips', 'cards for larger restaurant/hotel charges'],
    '/travel-guide/packing-list/': ['data-priority-guide-depth=\'visitor-reference\'', 'Reef-conscious sun protection', 'Dry bag', 'day kit'],
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
    if any(part in IGNORE for part in p.parts):
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

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Static site verification passed')
