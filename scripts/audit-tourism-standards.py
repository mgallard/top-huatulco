#!/usr/bin/env python3
"""Lightweight audit for Mogens' tourism page standards.

This does not replace full site tests. It catches common standard failures early:
- missing standards/source files
- missing metadata/H1/canonical
- broken internal links
- FAQ blocks appearing before substantial content
- itinerary titles that promise N days without N day markers
- visible process/placeholder wording
- no obvious visitor-decision language on key pages

Review-only/private media boards are skipped because they intentionally contain
classifier UI text and draft asset metadata that would be inappropriate on
public guide pages.
"""
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import re, sys

ROOT = Path(__file__).resolve().parents[1]
IGNORE_PARTS = {'node_modules', 'dist', '.git', '.vercel', '__pycache__', 'public'}
IGNORE_ROUTE_PREFIXES = ('/media-review/', '/owner-photo-gallery/')
BANNED = [
    'lorem ipsum', 'coming soon', 'todo:', 'fixme', 'placeholder',
    'ai slop', 'source map:', 'internal note', 'launch polish',
    'do not publish', 'preview uses', 'sister-site media library'
]
DECISION_TERMS = [
    'best for', 'skip if', 'choose', 'avoid', 'pair', 'how to get',
    'getting there', 'best time', 'what to bring', 'practical', 'verify before'
]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ''
        self.h1 = 0
        self.desc = False
        self.canon = False
        self.hrefs = []
        self.imgs = []
        self._title = False
        self.text_chunks = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'title': self._title = True
        if tag == 'h1': self.h1 += 1
        if tag == 'meta' and attrs.get('name') == 'description' and attrs.get('content'): self.desc = True
        if tag == 'link' and attrs.get('rel') == 'canonical' and attrs.get('href'): self.canon = True
        if tag == 'a' and attrs.get('href'): self.hrefs.append(attrs['href'])
        if tag == 'img': self.imgs.append(attrs)
    def handle_endtag(self, tag):
        if tag == 'title': self._title = False
    def handle_data(self, data):
        if self._title: self.title += data
        if data.strip(): self.text_chunks.append(data)

def route_for(path):
    if path == ROOT / 'index.html': return '/'
    return '/' + str(path.parent.relative_to(ROOT)).strip('/') + '/'

def is_ignored_route(route):
    return any(route.startswith(prefix) for prefix in IGNORE_ROUTE_PREFIXES)

def html_files():
    for p in ROOT.rglob('*.html'):
        if any(part in IGNORE_PARTS for part in p.parts):
            continue
        route = route_for(p)
        if is_ignored_route(route):
            continue
        yield p

def internal_target(href, current_route):
    href = href.split('#',1)[0].split('?',1)[0].strip()
    if not href or href.startswith(('http://','https://','mailto:','tel:','#')): return None
    if href.startswith('/assets/') or href.startswith('/images/') or href.startswith('/icons') or href.endswith(('.pdf','.jpg','.jpeg','.png','.webp','.svg','.css','.js')): return None
    if href.startswith('/'):
        normalized = href
    else:
        # Resolve relative to current directory route.
        base = current_route if current_route.endswith('/') else current_route + '/'
        normalized = '/' + posixpath.normpath(posixpath.join(base, href)).lstrip('/')
        if not normalized.endswith('/') and '.' not in normalized.rsplit('/', 1)[-1]:
            normalized += '/'
    return ROOT/'index.html' if normalized == '/' else ROOT/normalized.strip('/')/'index.html'

errors=[]
warnings=[]
if not (ROOT/'TOURISM_PAGE_STANDARDS.md').exists():
    errors.append('Missing TOURISM_PAGE_STANDARDS.md')
if not ((ROOT/'CONTENT_SOURCE_MAP.md').exists() or (ROOT/'CONTENT_ENRICHMENT_SOURCES.md').exists()):
    warnings.append('No CONTENT_SOURCE_MAP.md or CONTENT_ENRICHMENT_SOURCES.md found')

pages=list(html_files())
for p in pages:
    txt=p.read_text(encoding='utf-8', errors='ignore')
    low=txt.lower()
    route=route_for(p)
    parser=PageParser(); parser.feed(txt)
    visible_low=' '.join(parser.text_chunks).lower()
    if not parser.title.strip(): errors.append(f'{route} missing title')
    if parser.h1 != 1: errors.append(f'{route} should have exactly one H1; found {parser.h1}')
    if not parser.desc: errors.append(f'{route} missing meta description')
    if not parser.canon: warnings.append(f'{route} missing canonical')
    for banned in BANNED:
        if banned in visible_low:
            errors.append(f'{route} has banned public/process wording: {banned}')
    for href in parser.hrefs:
        target=internal_target(href, route)
        if target and not target.exists():
            errors.append(f'{route} broken internal link {href}')
    faq_pos = low.find('faq')
    h2_positions = [m.start() for m in re.finditer(r'<h2\b', low)]
    if faq_pos != -1 and len(h2_positions) >= 3 and faq_pos < h2_positions[min(2, len(h2_positions)-1)]:
        warnings.append(f'{route} FAQ appears early; verify it follows main editorial content')
    promised = None
    route_match = re.search(r'/(\d+)-days?[-/]', route)
    title_match = re.match(r'\s*(\d+)\s*[- ]?day', parser.title.lower())
    if route_match:
        promised = int(route_match.group(1))
    elif title_match:
        promised = int(title_match.group(1))
    if promised:
        day_markers = 0
        # Count single day cards plus compact ranges like Days 3–4 as two days.
        for a,b in re.findall(r'days?\s+(\d+)\s*[–—-]\s*(\d+)', visible_low):
            a=int(a); b=int(b); day_markers += max(1, b-a+1)
        singles = re.findall(r'\bday\s+(\d+)\b', visible_low)
        ranged_numbers = {n for pair in re.findall(r'days?\s+(\d+)\s*[–—-]\s*(\d+)', visible_low) for n in pair}
        day_markers += sum(1 for n in singles if n not in ranged_numbers)
        if promised > 1 and day_markers < promised:
            errors.append(f'{route} promises {promised} days but only shows {day_markers} day markers')
    key_route = route == '/' or any(seg in route for seg in ['/destinations/', '/beaches/', '/things-to-do/', '/where-to-stay/', '/food', '/itineraries/', '/travel-guide/', '/towns'])
    if key_route and not any(term in low for term in DECISION_TERMS):
        warnings.append(f'{route} lacks obvious visitor-decision terms from the standard')
    for img in parser.imgs:
        if not img.get('alt'):
            warnings.append(f'{route} image missing alt text')

print(f'Tourism standard audit: {len(pages)} HTML pages checked')
if warnings:
    print('\nWARNINGS:')
    print('\n'.join('- '+w for w in warnings[:80]))
    if len(warnings) > 80: print(f'- ... {len(warnings)-80} more warnings')
if errors:
    print('\nERRORS:')
    print('\n'.join('- '+e for e in errors[:120]))
    if len(errors) > 120: print(f'- ... {len(errors)-120} more errors')
    sys.exit(1)
print('Tourism standard audit passed with no blocking errors')
