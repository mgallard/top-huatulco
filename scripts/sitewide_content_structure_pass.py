from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

GUIDE_ATTRS = "data-subject-led-guide='true' data-sitewide-structure='tourism-guide'"
START = "<!-- sitewide-content-structure:start -->"
END = "<!-- sitewide-content-structure:end -->"


def read(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def write(rel, text):
    path = ROOT / rel
    path.write_text(text.rstrip() + "\n", encoding='utf-8')
    print(f"updated {rel}")


def add_main_attrs(html):
    m = re.search(r"<main([^>]*)>", html)
    if not m:
        return html
    attrs = m.group(1)
    additions = []
    if "data-subject-led-guide" not in attrs:
        additions.append("data-subject-led-guide='true'")
    if "data-sitewide-structure" not in attrs:
        additions.append("data-sitewide-structure='tourism-guide'")
    if not additions:
        return html
    new = f"<main{attrs} {' '.join(additions)}>"
    return html[:m.start()] + new + html[m.end():]


def strip_block(html):
    return re.sub(rf"\n?{re.escape(START)}.*?{re.escape(END)}\n?", "\n", html, flags=re.S)


def nav(items):
    links = ''.join(
        f"<a class='rounded-2xl border border-border bg-white px-4 py-3 text-sm font-bold text-ink/75 shadow-soft hover:text-primary' data-guide-nav-link href='#{anchor}'>{label}</a>"
        for anchor, label in items
    )
    return f"""
<nav class='section-pad !py-6' data-guide-nav aria-label='On-page guide sections'>
  <div class='container-xl'>
    <div class='rounded-[2rem] border border-border bg-surface p-5 shadow-card'>
      <p class='text-xs font-bold uppercase tracking-[.18em] text-primary'>On this page</p>
      <div class='mt-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-4'>{links}</div>
    </div>
  </div>
</nav>"""


def decision_module(kicker, title, verdict, choose, avoid, backup, sources, links):
    link_html = ''.join(f"<a class='inline-flex min-h-11 items-center justify-center rounded-full bg-primary px-5 py-2.5 text-sm font-bold text-white hover:brightness-110' href='{href}'>{label}</a>" for href, label in links)
    return f"""
<section id='structure-verdict' class='section-pad !pb-6 !pt-8' data-structure-verdict='true'>
  <div class='container-xl max-w-6xl'>
    <div class='grid gap-6 lg:grid-cols-[1.05fr_.95fr]'>
      <article class='card p-7 sm:p-8'>
        <p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>{kicker}</p>
        <h2 class='mt-2 font-heading text-3xl font-semibold'>Quick verdict: {title}</h2>
        <p class='mt-4 leading-8 text-ink/75'>{verdict}</p>
      </article>
      <aside class='card bg-surface p-7 sm:p-8'>
        <h2 class='font-heading text-2xl font-semibold'>Choose / avoid</h2>
        <ul class='mt-4 list-disc space-y-3 pl-5 leading-7 text-ink/75'>
          <li><strong>Choose this when:</strong> {choose}</li>
          <li><strong>Avoid this when:</strong> {avoid}</li>
          <li><strong>Better backup idea:</strong> {backup}</li>
        </ul>
      </aside>
    </div>
    <div class='mt-6 overflow-hidden rounded-[1.5rem] border border-border bg-white shadow-card' data-responsive-table='structure-decision'>
      <table class='w-full text-sm'>
        <thead><tr class='bg-secondary text-left text-ink/65'><th class='p-4'>Visitor question</th><th class='p-4'>Decision rule</th></tr></thead>
        <tbody>
          <tr class='border-t border-border'><td class='p-4 font-bold'>What should I decide first?</td><td class='p-4 text-ink/75'>{choose}</td></tr>
          <tr class='border-t border-border'><td class='p-4 font-bold'>What can go wrong?</td><td class='p-4 text-ink/75'>{backup}</td></tr>
          <tr class='border-t border-border'><td class='p-4 font-bold'>What should I verify?</td><td class='p-4 text-ink/75'>{sources}</td></tr>
        </tbody>
      </table>
    </div>
    <div class='mt-6 flex flex-wrap gap-3' data-structure-next-links='true'>{link_html}</div>
  </div>
</section>"""


def insert_after_hero(html, block):
    html = strip_block(html)
    html = add_main_attrs(html)
    pos = html.find("</section>", html.find("<main"))
    if pos == -1:
        raise RuntimeError('Could not find hero section')
    pos += len("</section>")
    return html[:pos] + "\n" + START + block + "\n" + END + html[pos:]


def insert_before_marker(html, marker, block):
    html = strip_block(html)
    html = add_main_attrs(html)
    candidates = [marker]
    candidates += [
        "<section id='beach-grid' class='section-pad'><div class='container-xl'><div class='grid",
        "<section id='bay-comparison' class='section-pad' data-destinations-comparison>",
        "<section id='towns-grid' class='section-pad'><div class='container-xl max-w-6xl'><div class='card p-7'><h2>Choose by what you want to do</h2>",
        "<section id='food-directory' class='section-pad' data-entity-depth='food-culture'>",
        "<section id='operator-options' class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='tours'>",
        "<section id='activity-chooser' class='section-pad'><div class='container-xl max-w-6xl'>",
        "<section id='itinerary-chooser' class='section-pad'><div class='container-xl max-w-6xl'>",
        "<section id='travel-questions' class='section-pad'><div class='container-xl max-w-6xl'>",
    ]
    idx = -1
    for candidate in candidates:
        idx = html.find(candidate)
        if idx != -1:
            break
    if idx == -1:
        raise RuntimeError(f'Marker not found: {marker}')
    return html[:idx] + START + block + "\n" + END + "\n" + html[idx:]

hub_data = {
    'beaches/index.html': dict(
        nav=[('structure-verdict','Quick verdict'),('beach-grid','Beach guide cards'),('check-before','Check first'),('structure-next-links','Next guides')],
        marker="<section class='section-pad'><div class='container-xl'><div class='grid",
        block=decision_module('Beach planning', 'choose beaches by conditions, not by the prettiest name',
            'Huatulco beaches change by access, shade, food, swell, boat traffic, and time of day. The right choice is usually one easy beach plus one meal plan, not a rushed attempt to sample every bay.',
            'you know whether the group wants calm swimming, snorkeling, seafood lunch, sunset, or quiet scenery.',
            'you only have a vague “best beach” list; Tangolunda, Chahué, Maguey, Cacaluta, and Chachacual solve different days.',
            'If wind or visibility is poor, switch to La Crucecita, Chahué sunset, Mercado 3 de Mayo, or a pool/rest afternoon instead of forcing a remote beach.',
            'Same-week sea state, road/boat access, restaurant/payment availability, and return transport.',
            [('/destinations/','Compare all bays'),('/things-to-do/snorkeling/','Plan snorkeling'),('/travel-guide/getting-around/','Check transport')])
    ),
    'destinations/index.html': dict(
        nav=[('structure-verdict','Quick verdict'),('bay-comparison','Bay comparison'),('bay-guides','Full bay guides'),('structure-next-links','Next guides')],
        marker="<section class='section-pad' data-destinations-comparison>",
        block=decision_module('Bay planning', 'pick the bay by the day you want',
            'The nine bays are close on a map but not interchangeable. Start with the visitor problem: easy resort day, marina/boat logistics, calm seafood lunch, remote scenery, snorkel conditions, or quiet viewpoint.',
            'you compare access, services, swimming, food, and return logistics before choosing the bay.',
            'you treat remote boat-access bays as simple taxi beach days or assume every bay is safe/swimmable in the same conditions.',
            'If the water day weakens, use Santa Cruz for a lighter harbor meal, La Crucecita for town time, or Chahué for an easy sunset instead of overcommitting.',
            'Sea state, operator route, park-area rules, beach-club/public-access details, and return rides.',
            [('/beaches/','Beach chooser'),('/things-to-do/boat-tours/','Boat-tour guide'),('/itineraries/4-days-relax-snorkel/','4-day plan')])
    ),
    'towns-cities/index.html': dict(
        nav=[('structure-verdict','Quick verdict'),('towns-grid','Town cards'),('route-logic','Route logic'),('check-before','Check first')],
        marker="<section class='section-pad'><div class='container-xl max-w-6xl'><div class='card p-7'><h2>Choose by what you want to do</h2>",
        block=decision_module('Town planning', 'use each town for a specific job',
            'Huatulco planning gets easier when each town has a role: La Crucecita for meals/errands, Santa Cruz for boats, Copalita/Bocana for river-mouth and archaeology context, Mazunte and Puerto Ángel for longer coast days.',
            'you are deciding where to spend a morning, evening, or coast day and need practical route logic.',
            'you expect every nearby place to be a quick filler stop; Mazunte and Puerto Ángel need real drive-time and return planning.',
            'If a west-coast day feels too long, keep the day local: La Crucecita + Chahué, Santa Cruz + boat/lunch, or Copalita/Bocana only.',
            'Road timing, return taxis/transfers, INAH access for Copalita, turtle-center/opening details for Mazunte, and weather.',
            [('/towns-cities/la-crucecita/','La Crucecita'),('/towns-cities/santa-cruz/','Santa Cruz'),('/travel-guide/getting-around/','Transport guide')])
    ),
    'food-culture/index.html': dict(
        nav=[('structure-verdict','Quick verdict'),('food-directory','Named food options'),('meal-plan','3–5 day meal plan'),('check-before','Check first')],
        marker="<section class='section-pad' data-entity-depth='food-culture'>",
        block=decision_module('Food planning', 'plan meals around town nights and beach lunches',
            'Food is not a separate errand in Huatulco. Use La Crucecita for your most reliable planned dinners, Mercado 3 de Mayo for daytime town texture, and bay palapas for simple seafood tied to the beach you are already visiting.',
            'you match the meal to the day: town dinner after errands, beach seafood after swimming, market morning before an easy afternoon.',
            'you chase a restaurant ranking across town when the day already has heat, boat timing, or return-transport friction.',
            'If a restaurant is closed or full, keep a nearby town backup rather than crossing between bays at dinner time.',
            'Hours, closing days, reservation needs, payment options, current menus, and holiday/weekend crowds.',
            [('/towns-cities/la-crucecita/','Town food base'),('/things-to-do/la-crucecita-market/','Market guide'),('/itineraries/4-days-relax-snorkel/','Food in itinerary')])
    ),
    'tours/index.html': dict(
        nav=[('structure-verdict','Quick verdict'),('operator-options','Operator comparison'),('choose-format','Choose format'),('check-before','Check first')],
        marker="<section class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='tours'>",
        block=decision_module('Tour planning', 'buy clarity, not just a low headline price',
            'A good Huatulco tour is defined by route honesty, sea-condition flexibility, inclusion clarity, meeting point, group size, and whether the operator can explain why a bay is worth using that day.',
            'you know the exact route, pickup/meeting point, inclusions, fees, group size, cancellation rules, and weather backup.',
            'you are comparing only price or letting a hotel desk sell a vague “five bays” plan without naming stops and conditions.',
            'If sea conditions are wrong, choose a land day: Copalita, La Crucecita, Chahué sunset, or a shorter Santa Cruz meal/walk plan.',
            'Operator license/reputation, route changes, park fees, snorkel gear, lunch/drinks, cancellation policy, and return time.',
            [('/things-to-do/boat-tours/','Boat tours'),('/things-to-do/snorkeling/','Snorkeling'),('/things-to-do/copalita-archaeology/','Copalita')])
    ),
}

# Add stronger hub structure.
for rel, data in hub_data.items():
    html = read(rel)
    block = nav(data['nav']) + data['block']
    if data['marker'].startswith("<section class='section-pad'><div") or data['marker'].startswith("<section class='section-pad' data"):
        new = insert_before_marker(html, data['marker'], block)
    else:
        new = insert_before_marker(html, data['marker'], block)
    # Add stable anchors to existing first sections where needed.
    new = new.replace("<section class='section-pad'><div class='container-xl'><div class='grid", "<section id='beach-grid' class='section-pad'><div class='container-xl'><div class='grid")
    new = new.replace("<section class='section-pad' data-destinations-comparison>", "<section id='bay-comparison' class='section-pad' data-destinations-comparison>")
    new = new.replace("<div class='mt-12'>\n      <div class='mb-5 max-w-3xl'>\n        <p class='overline'>Bay guides", "<div id='bay-guides' class='mt-12'>\n      <div class='mb-5 max-w-3xl'>\n        <p class='overline'>Bay guides")
    new = new.replace("<section class='section-pad'><div class='container-xl max-w-6xl'><div class='card p-7'><h2>Choose by what you want to do</h2>", "<section id='towns-grid' class='section-pad'><div class='container-xl max-w-6xl'><div class='card p-7'><h2>Choose by what you want to do</h2>")
    new = new.replace("<section class='section-pad bg-surface'><div class='container-xl max-w-5xl'><div class='card p-7'><h2>Simple route logic</h2>", "<section id='route-logic' class='section-pad bg-surface'><div class='container-xl max-w-5xl'><div class='card p-7'><h2>Simple route logic</h2>")
    new = new.replace("<section class='section-pad bg-surface' data-visible-sources='true'>", "<section id='check-before' class='section-pad bg-surface' data-visible-sources='true'>")
    new = new.replace("<section class='section-pad' data-entity-depth='food-culture'>", "<section id='food-directory' class='section-pad' data-entity-depth='food-culture'>")
    new = new.replace("<section class='section-pad bg-white'><div class='container-xl max-w-5xl'><div class='card p-7'><h2>A better food plan", "<section id='meal-plan' class='section-pad bg-white'><div class='container-xl max-w-5xl'><div class='card p-7'><h2>A better food plan")
    new = new.replace("<section class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='tours'>", "<section id='operator-options' class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='tours'>")
    new = new.replace("<section class='mt-10 grid gap-6 lg:grid-cols-3'>", "<section id='choose-format' class='mt-10 grid gap-6 lg:grid-cols-3'>")
    write(rel, new)


# Strengthen already-reset section hubs so they meet the same sitewide structure contract.
extra_hubs = {
    'things-to-do/index.html': dict(
        marker="<section class='section-pad'><div class='container-xl max-w-6xl'>",
        nav=[('structure-verdict','Quick verdict'),('activity-chooser','Activity chooser'),('check-before','Check first'),('structure-next-links','Next guides')],
        block=decision_module('Activity planning', 'choose the activity by the kind of day your group can handle',
            'Huatulco activities depend on sea conditions, heat, drive tolerance, and how much planning your group wants. Choose one anchor activity, keep the next block flexible, and avoid stacking boat, market, archaeology, and sunset plans into the same day.',
            'you know whether today is a water day, a town day, a culture day, or a low-effort sunset/meal day.',
            'you are trying to do every famous activity in one short trip or forcing a boat/snorkel day when conditions are poor.',
            'If weather, water, or group energy changes, switch to La Crucecita market, Chahué sunset, Santa Cruz lunch, or a lighter bay plan.',
            'Sea state, operator inclusions, opening days, return transport, heat, and payment/cash needs.',
            [('/things-to-do/boat-tours/','Boat tours'),('/things-to-do/snorkeling/','Snorkeling'),('/things-to-do/la-crucecita-market/','Market guide')])
    ),
    'itineraries/index.html': dict(
        marker="<section class='section-pad'><div class='container-xl max-w-6xl'>",
        nav=[('structure-verdict','Quick verdict'),('itinerary-chooser','Itinerary chooser'),('check-before','Check first'),('structure-next-links','Next guides')],
        block=decision_module('Itinerary planning', 'choose the route by pace before choosing attractions',
            'The best Huatulco itinerary protects the first water morning, keeps one town/market or rest block flexible, and avoids pretending that every bay, town, and coast road belongs in a short stay.',
            'you match the plan to trip length: 3 nights for essentials, 4 days for relaxed snorkeling, 5+ nights for Oaxaca coast side trips.',
            'you have a late arrival, mixed-energy group, or no backup day but still plan remote beaches and a long coast drive.',
            'If a water day fails, move the boat/snorkel plan to the next morning and use La Crucecita, Chahué, or Copalita as the dry-day substitute.',
            'Arrival time, base location, sea conditions, drive tolerance, opening days, and return transport.',
            [('/itineraries/3-days-huatulco/','3-day plan'),('/itineraries/4-days-relax-snorkel/','4-day plan'),('/itineraries/5-days-oaxaca-coast/','5-day coast plan')])
    ),
    'travel-guide/index.html': dict(
        marker="<section class='section-pad'><div class='container-xl max-w-6xl'>",
        nav=[('structure-verdict','Quick verdict'),('travel-questions','Planning questions'),('check-before','Check first'),('structure-next-links','Next guides')],
        block=decision_module('Travel basics', 'solve logistics before choosing more beaches',
            'The travel-guide section should prevent avoidable friction: arrival confusion, taxi assumptions, poor base choice, cash problems, unsafe water decisions, and packing gaps. Use it before locking tours or remote beach plans.',
            'you need practical rules for airport arrival, taxis, rental cars, seasons, money, safety, packing, or first-time planning.',
            'you are only looking for inspiration and have not yet chosen where you sleep, how you move, or what you will do if conditions change.',
            'If a plan feels complicated, simplify the base: pick La Crucecita/Tangolunda/Santa Cruz logic first, then choose one beach or tour per day.',
            'Airport arrival timing, taxi/transfer rules, current weather/sea conditions, ATM/cash needs, and official safety guidance.',
            [('/travel-guide/airport-arrival/','Airport arrival'),('/travel-guide/getting-around/','Getting around'),('/travel-guide/first-time-visitors/','First-time guide')])
    ),
}
for rel, data in extra_hubs.items():
    html = read(rel)
    block = nav(data['nav']) + data['block']
    new = insert_before_marker(html, data['marker'], block)
    new = new.replace(data['marker'], data['marker'].replace("<section ", "<section id='" + {'things-to-do/index.html':'activity-chooser','itineraries/index.html':'itinerary-chooser','travel-guide/index.html':'travel-questions'}[rel] + "' "), 1)
    write(rel, new)

# Strengthen town detail pages without replacing route-specific copy.
town_details = {
    'towns-cities/la-crucecita/index.html': ('La Crucecita', 'Use La Crucecita as the practical center: dinner, market, ATMs, pharmacies, taxis, coffee, and a soft first-night walk.', 'town dinner or errands', 'a beach day with no town need', 'pair with Chahué sunset or Santa Cruz boats'),
    'towns-cities/santa-cruz/index.html': ('Santa Cruz', 'Use Santa Cruz for boat departures, waterfront lunch, cruise arrival orientation, and easy harbor logistics.', 'boat-day logistics', 'quiet remote beach scenery', 'pair with La Crucecita dinner after the marina'),
    'towns-cities/copalita/index.html': ('Copalita / Bocana', 'Use Copalita and Bocana for river-mouth scenery, west-side meals, beach energy, and archaeology context if INAH access is current.', 'west-side culture and beach context', 'a quick no-planning stop', 'pair with Tangolunda or Chahué on the return'),
    'towns-cities/mazunte/index.html': ('Mazunte', 'Use Mazunte as a real Oaxaca coast day trip, not a quick Huatulco filler stop.', 'a full coast day with early departure', 'a tired group or late start', 'pair with San Agustinillo and a planned return'),
    'towns-cities/puerto-angel/index.html': ('Puerto Ángel', 'Use Puerto Ángel for a longer working-coast contrast with Zipolite/San Agustinillo/Mazunte, not as a resort-style beach substitute.', 'coast-road exploration', 'low-friction beach comfort', 'pair with Mazunte or Zipolite if the day has enough time'),
}
for rel, (name, verdict, choose, avoid, pair) in town_details.items():
    html = read(rel)
    block = nav([('structure-verdict','Quick verdict'),('mini-route','Mini route'),('check-before','Check first'),('structure-next-links','Next guides')]) + decision_module('Town guide', f'use {name} for the right kind of day', verdict, choose, avoid, f'If timing slips, shorten the plan: {pair}.', 'Opening hours, road timing, return transport, weather, and any official access rules.', [('/towns-cities/','Compare towns'),('/travel-guide/getting-around/','Transport guide'),('/itineraries/5-days-oaxaca-coast/','Coast itinerary')])
    new = insert_after_hero(html, block)
    write(rel, new)

# Add subject-led markers to already-strong destination and activity/itinerary/travel detail pages.
for sub in ['destinations', 'things-to-do', 'itineraries', 'travel-guide']:
    for path in (ROOT/sub).glob('*/index.html'):
        rel = path.relative_to(ROOT).as_posix()
        html = read(rel)
        new = add_main_attrs(html)
        if new != html:
            write(rel, new)


# Itinerary detail pages already have day-by-day structure; add an explicit quick-verdict label so the structure is obvious.
itinerary_verdicts = {
    'itineraries/3-days-huatulco/index.html': 'Quick verdict: use this short plan to protect one boat morning, one town/culture block, and enough easy beach time without turning three days into a checklist.',
    'itineraries/4-days-relax-snorkel/index.html': 'Quick verdict: use this route when the group wants relaxed snorkeling, easy meals, and one flexible backup morning instead of a rushed bay-counting trip.',
    'itineraries/5-days-oaxaca-coast/index.html': 'Quick verdict: use this longer plan when you can add Mazunte, Puerto Ángel, or coast-road context without stealing the best Huatulco water mornings.',
    'itineraries/snorkel-boat-day/index.html': 'Quick verdict: use this as a single water-day plan built around Santa Cruz, realistic sea conditions, and a backup if visibility or wind is poor.',
}
for rel, verdict in itinerary_verdicts.items():
    html = read(rel)
    html = add_main_attrs(html)
    if "data-itinerary-quick-verdict='true'" not in html:
        anchor = "</nav>"
        idx = html.find(anchor)
        if idx == -1:
            raise RuntimeError(f'No itinerary nav found in {rel}')
        idx += len(anchor)
        card = f"\n  <div class='mt-6 rounded-[1.5rem] border border-border bg-white p-6 shadow-card' data-itinerary-quick-verdict='true'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>Quick verdict</p><p class='mt-3 leading-7 text-ink/75'>{verdict}</p></div>"
        html = html[:idx] + card + html[idx:]
        write(rel, html)

# Add audit artifact.
(ROOT / 'SITEWIDE_CONTENT_STRUCTURE_AUDIT.md').write_text("""# Top Huatulco Sitewide Content Structure Audit

Date: 2026-05-31

## Problem addressed

The previous passes improved priority sections, but the site still had inconsistent information architecture. Some hubs were still mostly grids, some guide pages had good facts but lacked a visible subject-led reading path, and several town/food/tour pages did not consistently expose the same visitor decision contract.

## New sitewide contract

Every public tourism hub or guide should now expose the route as a visitor decision, not just a list of cards:

1. `data-subject-led-guide='true'` and `data-sitewide-structure='tourism-guide'` on public tourism guide pages.
2. A visible `On this page` guide navigation where the page needs more than a simple card grid.
3. A `Quick verdict` section that tells the visitor how to use the page.
4. Choose / avoid / backup guidance.
5. A practical decision table or equivalent scannable decision module.
6. Source/current-detail verification language for volatile details.
7. Clear next-step internal links.

## Sections corrected in this pass

- Bays hub `/destinations/`
- Beaches hub `/beaches/`
- Towns hub `/towns-cities/`
- Town detail pages under `/towns-cities/`
- Food/culture `/food-culture/`
- Tours `/tours/`
- Subject-led marker coverage on destination, activity, itinerary, and travel-guide detail pages

## What this does not solve

This pass fixes content structure and visitor decision flow. It does not solve the remaining hard media gaps for Órgano, Chachacual, Conejos, or Copalita archaeology.
""", encoding='utf-8')
print('wrote SITEWIDE_CONTENT_STRUCTURE_AUDIT.md')
