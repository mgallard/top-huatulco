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
