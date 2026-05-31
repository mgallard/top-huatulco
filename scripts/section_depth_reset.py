from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = "https://tophuatulco.com"

NAV = """<header class='sticky top-0 z-50 border-b border-border bg-white/95 backdrop-blur'>
  <nav class='container-xl flex min-h-16 items-center justify-between gap-5' aria-label='Primary navigation'>
    <a href='/' class='flex items-center gap-3'><span class='grid h-10 w-10 place-items-center rounded-full bg-primary text-sm font-black text-white shadow-soft'>HU</span><span class='font-heading text-lg font-semibold'>Top Huatulco</span></a>
    <div class='hidden items-center gap-5 text-sm font-bold text-ink/75 xl:flex'><a href='/destinations/' class='hover:text-primary'>Bays</a><a href='/beaches/' class='hover:text-primary'>Beaches</a><a href='/towns-cities/' class='hover:text-primary'>Towns</a><a href='/things-to-do/' class='hover:text-primary'>Things to do</a><a href='/itineraries/' class='hover:text-primary'>Itineraries</a><a href='/travel-guide/' class='hover:text-primary'>Travel guide</a><a href='/food-culture/' class='hover:text-primary'>Food</a><a href='/tours/' class='hover:text-primary'>Tours</a></div>
    <button type='button' class='inline-flex h-11 w-11 items-center justify-center rounded-full border border-border bg-white text-ink shadow-soft xl:hidden' data-mobile-menu-button aria-controls='mobile-menu' aria-expanded='false' aria-label='Open navigation menu'><svg class='site-icon' data-menu-icon aria-hidden='true'><use href='/icons.svg#bars'></use></svg></button>
  </nav>
  <div id='mobile-menu' data-mobile-menu class='container-xl hidden pb-4 xl:hidden'><div class='rounded-[1.5rem] border border-border bg-white p-3 text-sm font-bold shadow-card'><a href='/destinations/' class='block rounded-2xl px-4 py-3 hover:bg-secondary'>Bays</a><a href='/beaches/' class='block rounded-2xl px-4 py-3 hover:bg-secondary'>Beaches</a><a href='/towns-cities/' class='block rounded-2xl px-4 py-3 hover:bg-secondary'>Towns</a><a href='/things-to-do/' class='block rounded-2xl px-4 py-3 hover:bg-secondary'>Things to do</a><a href='/itineraries/' class='block rounded-2xl px-4 py-3 hover:bg-secondary'>Itineraries</a><a href='/travel-guide/' class='block rounded-2xl px-4 py-3 hover:bg-secondary'>Travel guide</a><a href='/food-culture/' class='block rounded-2xl px-4 py-3 hover:bg-secondary'>Food</a><a href='/tours/' class='block rounded-2xl px-4 py-3 hover:bg-secondary'>Tours</a></div></div>
</header>"""

FOOTER = """<footer class='border-t border-border bg-surface py-10 text-sm text-ink/60'><div class='container-xl grid gap-4 md:grid-cols-2'><div><strong class='text-ink'>Top Huatulco</strong><p class='mt-2'>Practical travel guides for Huatulco and the Oaxaca coast.</p></div><div class='md:text-right'><a href='/about/' class='font-bold text-primary'>About</a><span class='mx-2'>•</span><a href='/image-credits/' class='font-bold text-primary'>Sources & credits</a><span class='mx-2'>•</span><a href='/privacy/' class='font-bold text-primary'>Privacy</a></div></div></footer>
<script type='module' src='/src/main.js'></script>"""


def e(s):
    return escape(str(s), quote=True)


def page_html(title, desc, path, kicker, body, marker="data-section-depth-reset='true' data-subject-led-guide='true' data-priority-guide-depth='visitor-reference'"):
    return f"""<!doctype html>
<html lang='en'>
<head>
  <meta charset='UTF-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>
  <title>{e(title)} | Top Huatulco</title>
  <meta name='description' content='{e(desc)}'>
  <link rel='canonical' href='{DOMAIN}{path}'>
  <meta property='og:type' content='article'>
  <meta property='og:title' content='{e(title)} | Top Huatulco'>
  <meta property='og:description' content='{e(desc)}'>
  <meta property='og:url' content='{DOMAIN}{path}'>
  <meta name='theme-color' content='#2C9AB7'>
</head>
<body class='bg-background text-ink'>
{NAV}
<main {marker}>
<section class='bg-[linear-gradient(135deg,#EBF8FA_0%,#FFF7ED_100%)] py-12 sm:py-16'>
  <div class='container-xl'>
    <p class='font-script text-2xl leading-none text-primary'>{e(kicker)}</p>
    <h1 class='mt-3 max-w-4xl text-4xl font-semibold tracking-tight sm:text-5xl'>{e(title)}</h1>
    <p class='mt-4 max-w-3xl text-base leading-8 text-ink/70 sm:text-lg'>{e(desc)}</p>
  </div>
</section>
{body}
</main>
{FOOTER}
</body></html>"""


def card(title, text, extra=""):
    return f"<div class='card flex h-full flex-col p-6'>{extra}<h3 class='font-heading text-xl font-semibold text-ink'>{e(title)}</h3><p class='mt-3 leading-7 text-ink/75'>{text}</p></div>"


def ul(items):
    return "<ul class='mt-4 list-disc space-y-3 pl-5 leading-7 text-ink/75'>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def table(headers, rows):
    head = "".join(f"<th class='px-4 py-3 text-left font-heading text-sm text-ink'>{e(h)}</th>" for h in headers)
    body = "".join("<tr class='border-t border-border'>" + "".join(f"<td class='px-4 py-3 align-top text-sm leading-6 text-ink/75'>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f"<div class='mt-6 overflow-x-auto rounded-[1.25rem] border border-border bg-white shadow-card' data-responsive-table><table class='min-w-full'><thead class='bg-secondary/60'><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>"

SOURCES = {
    "infrastructure": [
        ("Huatulco Airport live flight/arrival checks", "https://www.huatulco-airport.com/"),
        ("Taxi Huatulco airport transfer reference", "https://www.taxihuatulco.com.mx/"),
        ("INAH Bocana del Río Copalita", "https://lugares.inah.gob.mx/en/node/4487"),
        ("INAH visitor listing for Bocana del Río Copalita", "https://lugares.inah.gob.mx/en/node/5540"),
    ],
    "operators": [
        ("Paraiso Huatulco activity desk", "https://www.paraisohuatulco.com/"),
        ("Huatulco Salvaje tour operator", "https://huatulcosalvaje.com/"),
        ("Aventura Mundo Huatulco", "https://aventuramundo.com/"),
    ],
    "regional": [
        ("Mazunte Pueblo Mágico / turtle center context", "https://www.gob.mx/sectur/articulos/mazunte-oaxaca"),
        ("Las Parotas Golf Club current-status cross-check", "https://www.tripadvisor.com/Attraction_Review-g2535585-d6989347-Reviews-Las_Parotas_Club_de_Golf_Huatulco-Tangolunda_Huatulco_Southern_Mexico.html"),
    ],
}


def source_box(source_keys):
    links=[]
    for key in source_keys:
        links.extend(SOURCES.get(key, []))
    return "<section class='section-pad pt-0' data-visible-sources='true'><div class='container-xl max-w-5xl'><div class='card bg-surface p-6'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>Current details to verify</p><p class='mt-3 leading-7 text-ink/75'>Use this guide for planning logic, then check same-week details before paying or driving: sea conditions, opening days, return transport, and operator inclusions can change.</p><div class='mt-4 flex flex-wrap gap-3'>" + "".join(f"<a class='rounded-full bg-white px-4 py-2 text-sm font-bold text-primary shadow-soft' href='{e(url)}' rel='nofollow noopener' target='_blank'>{e(label)}</a>" for label, url in links) + "</div></div></div></section>"

ACTIVITIES = {
"boat-tours": {
    "title":"Huatulco Bay Boat Tours",
    "desc":"How to choose a Huatulco bay boat tour without getting stuck on the wrong route, vague inclusions, or a long day that does not fit your group.",
    "verdict":"Do one bay boat tour if this is your first Huatulco trip. The value is not just seeing more beaches; it is understanding how Santa Cruz, Maguey, Órgano, Cacaluta, Chachacual, and the protected coastline fit together. Choose by route style, not by the lowest price.",
    "choose":["First-time visitors who want a one-day overview of the bays.","Families or couples who prefer one organized day instead of arranging multiple taxis and beach stops.","Snorkel-first travelers when the operator is honest about sea conditions and morning timing."],
    "avoid":["Anyone who gets seasick easily and cannot choose a calmer morning.","Travelers who only want quiet beach time; a private taxi to Maguey or Chahué may be easier.","Groups who dislike vendor-style lunch stops or unclear add-on costs."],
    "route":"Most shared trips start around Santa Cruz because the marina/pier infrastructure is there. A common route points the boat west and south along the bays, with swim or snorkel stops depending on conditions. Cacaluta and Chachacual are the scenic names visitors ask for, but the captain's call matters more than the brochure: wind, swell, and visibility decide where the water is worth entering.",
    "logistics":["Start from Santa Cruz unless your operator clearly includes hotel pickup and a realistic return plan.","Ask whether lunch, national-park fees, snorkel gear, drinks, and hotel pickup are included or separate.","Book the first good-weather morning you can, then keep the next day flexible as a backup.","For mixed-age groups, prioritize shade, toilets/lunch stop clarity, and easy boarding over maximum number of bays."],
    "directory":[("Paraiso Huatulco","Compare if you want a conventional local activity desk and hotel-zone pickup options."),("Huatulco Salvaje","Compare for smaller-group outdoor routes and clearer adventure positioning."),("Aventura Mundo Huatulco","Compare for activity bundles and practical day-tour logistics."),("Classic shared panga / private custom boat","Start at Santa Cruz, then compare a classic shared panga, a small-group nature boat, and a private/custom boat before paying.")],
    "pairs":[("/things-to-do/snorkeling/","Snorkeling guide"),("/destinations/santa-cruz/","Santa Cruz bay"),("/itineraries/snorkel-boat-day/","Boat-day itinerary")],
    "sources":["operators","infrastructure"]
},
"snorkeling": {
    "title":"Snorkeling in Huatulco",
    "desc":"A practical guide to choosing Huatulco snorkeling by bay, sea conditions, access, and group ability instead of assuming every pretty beach is easy in the water.",
    "verdict":"Snorkeling in Huatulco can be excellent, but it is condition-dependent. Plan it as a morning water decision, not as a fixed promise. Maguey is easier for casual visitors, while Chachacual and Cacaluta depend more on boat access and conditions.",
    "choose":["Visitors who can keep their best-weather morning flexible.","Families who are realistic about swimming ability and want a protected bay first.","Boat-day travelers who want scenery plus one or two water stops."],
    "avoid":["Days with rough water, poor visibility, or strong wind.","Remote beaches if your group needs bathrooms, shade, food, or easy exit options.","Booking only because a route says 'snorkel included' without asking where and when."],
    "route":"Use Maguey or the protected edges of Santa Cruz for the easiest version. Use a boat route toward Cacaluta or Chachacual when you want the scenic version and can accept that the captain may redirect. Do not treat open-coast beaches as beginner snorkel spots; Huatulco has protected bays and exposed Pacific edges, and they behave differently.",
    "logistics":["Ask the operator where snorkeling usually happens on the current week's conditions.","Bring a rash guard or shirt; the sun exposure on boats and shallow snorkel stops adds up fast.","If renting gear, check mask fit before leaving the dock or beach stand.","Keep a dry Plan B: La Crucecita market, Copalita, or a calm resort pool afternoon."],
    "directory":[("Maguey beach stands","Good for casual beach-and-snorkel days when the water is calm."),("Santa Cruz marina operators","Best comparison point for boat-based snorkel routes."),("Hotel activity desks","Convenient for families, but compare inclusions and return timing."),("Private boat option","Worth considering when you need shade, shorter timing, or flexible stops.")],
    "pairs":[("/things-to-do/boat-tours/","Boat tours"),("/destinations/el-maguey/","Maguey bay"),("/destinations/cacaluta/","Cacaluta beach")],
    "sources":["operators"]
},
"copalita-archaeology": {
    "title":"Copalita Archaeological Park",
    "desc":"How to visit Bocana del Río Copalita as a half-day Huatulco culture break, with access logic, heat planning, and what to verify before going.",
    "verdict":"Copalita is the best easy culture break from the Huatulco bays. Go for the river-mouth setting, viewpoints, trails, and a sense of Oaxaca's deeper history, not for a giant ruins complex like Monte Albán or Chichén Itzá.",
    "choose":["Travelers staying in Tangolunda, Conejos, Chahué, or Santa Cruz who want a half-day away from the beach.","Families who want a manageable history/nature stop before lunch.","Visitors who like viewpoints, shaded walking, and context more than big monuments."],
    "avoid":["The hottest part of the day if your group dislikes walking in heat.","Going without checking current opening/access status; local reports have changed over time.","Expecting a large museum-heavy site. Treat it as compact archaeology plus landscape."],
    "route":"The site sits near the Copalita river mouth west of Santa Cruz and close to the Bocana/Copalita side of the resort corridor. Pair it with Bocana beach or a Tangolunda-area lunch rather than forcing it into a full west-coast Mazunte day. If your driver waits, agree on timing before entering.",
    "logistics":["Check current INAH or local access notes before you go.","Go early, carry water, and wear shoes that handle dusty paths and uneven surfaces.","Ask a taxi driver for wait time or a confirmed pickup because return transport is not as simple as La Crucecita.","Pair with Bocana, Tangolunda, or a relaxed hotel afternoon, not another long-distance day trip."],
    "directory":[("INAH Bocana del Río Copalita listing","Use for location and official context."),("Local taxi from hotel zone","Best simple access if you do not have a rental car."),("Bocana beach restaurants","Possible lunch pairing after the site, depending on opening days."),("Tangolunda hotels","Easy base area for a morning Copalita visit.")],
    "pairs":[("/towns-cities/copalita/","Copalita and Bocana"),("/travel-guide/getting-around/","Getting around"),("/itineraries/3-days-huatulco/","3-day itinerary")],
    "sources":["infrastructure"]
},
"la-crucecita-market": {
    "title":"La Crucecita Market and Town Stop",
    "desc":"How to use La Crucecita market as a practical food, errands, coffee, souvenir, and rainy-afternoon stop instead of treating it like a polished attraction.",
    "verdict":"La Crucecita is the practical heart of a Huatulco trip. The market is useful for breakfast, fruit, tortillas, textiles, vanilla, coffee, mezcal browsing, and simple errands. It is not a staged attraction; that is the point.",
    "choose":["Visitors who want a real town break from resort zones.","Families who need snacks, pharmacy errands, cash, or a low-pressure lunch.","Food-curious travelers who want market counters before a beach afternoon."],
    "avoid":["Going only for nightlife energy; it is better as a daytime or early-evening town stop.","Expecting a giant Oaxaca City market. This is compact and practical.","Arriving hungry late in the afternoon without checking which food counters are open."],
    "route":"Start around the zócalo and church, then walk to Mercado 3 de Mayo and nearby shop streets. If you are coming from Santa Cruz or Chahué, a taxi makes this easy. If you are staying in Tangolunda, combine the market with dinner in town rather than making two separate taxi runs.",
    "logistics":["Bring small bills and cash; cards are not the right assumption for small purchases.","Go in the morning for food errands and a more functional market feel.","Use it as your cloudy-day or post-beach reset when water conditions are not ideal.","Pair with Terra-Cotta, El Sabor de Oaxaca, or another town dinner if you want a fuller evening."],
    "directory":[("Mercado 3 de Mayo","Best simple anchor for food counters, produce, souvenirs, and basics."),("La Crucecita zócalo","Good meeting point, evening stroll, church, and taxi reference."),("Terra-Cotta","Reliable town dinner candidate to compare."),("El Sabor de Oaxaca","Useful for visitors looking for Oaxacan flavors in town.")],
    "pairs":[("/food-culture/","Food and culture"),("/towns-cities/la-crucecita/","La Crucecita guide"),("/travel-guide/money-tipping/","Money and tipping")],
    "sources":["infrastructure"]
},
"mazunte-day-trip": {
    "title":"Mazunte Day Trip from Huatulco",
    "desc":"How to decide whether Mazunte is worth the long day from Huatulco, with route timing, turtle-center context, beach-town expectations, and safer alternatives.",
    "verdict":"Mazunte is worth it if you want a west-coast Oaxaca day with a Pueblo Mágico feel, beach-town cafes, and turtle-conservation context. It is not the easiest beach day from Huatulco; go only if your group accepts the drive and a longer return.",
    "choose":["Travelers with five or more nights who want to understand the wider Oaxaca coast.","Couples or independent travelers who like bohemian beach towns and slower lunches.","Visitors who can pair Mazunte with San Agustinillo or Puerto Ángel without rushing every stop."],
    "avoid":["Short trips where one full day away from Huatulco bays is too expensive in time.","Families who need easy bathrooms, predictable transport, and short drives.","Going only because it appears on a tour list; the drive is the main tradeoff."],
    "route":"Leave early from Huatulco, stop at Puerto Ángel or San Agustinillo only if it supports the day, then make Mazunte the main walk/lunch/sunset-style town. The Mexican Turtle Center is the named conservation anchor, but check current opening days before building the whole day around it.",
    "logistics":["Use a private driver or well-reviewed tour if you do not want to manage long return logistics.","Do not stack Mazunte, Zipolite, Puerto Ángel, and multiple beach swims unless your group wants a windshield day.","Carry cash and sun protection; beach-town services vary by season and day.","Have a closer Plan B: Copalita, La Crucecita, or San Agustín if the west-coast drive feels too much."],
    "directory":[("Mazunte Pueblo Mágico","Main west-coast town anchor and walking stop."),("Centro Mexicano de la Tortuga","Named turtle-conservation stop to verify before going."),("San Agustinillo","Nearby beach-town pairing if timing allows."),("Puerto Ángel","Fishing-town context stop, better as a short look than a rushed second destination.")],
    "pairs":[("/towns-cities/mazunte/","Mazunte guide"),("/towns-cities/puerto-angel/","Puerto Ángel guide"),("/itineraries/5-days-oaxaca-coast/","5-day coast itinerary")],
    "sources":["regional"]
},
"golf-tangolunda": {
    "title":"Golf in Tangolunda",
    "desc":"How to treat Huatulco golf as a verify-before-booking resort-zone morning, with current-status checks, transport, heat, and alternatives.",
    "verdict":"Golf is a niche Huatulco add-on, not a core reason to choose the destination. If Las Parotas / Tangolunda course access is operating for your dates, plan it as an early resort-zone morning and verify everything directly before promising it to your group.",
    "choose":["Golfers staying in Tangolunda who want one non-beach morning.","Groups where one traveler golfs while others stay at the resort or visit Chahué/La Crucecita.","Visitors comfortable confirming current status, tee times, rentals, and transport directly."],
    "avoid":["Building a whole trip around golf without direct confirmation.","Midday tee times in hot months unless you know your group handles heat.","Assuming club rentals, lessons, or restaurant service are available without checking."],
    "route":"Use Tangolunda as the anchor. If the course is available, keep the rest of the day close: resort lunch, Chahué, or La Crucecita dinner. Do not pair golf with a long west-coast day trip; that makes the schedule brittle.",
    "logistics":["Check the course's current operating status before booking flights around golf.","Confirm tee time, rental clubs, cart, dress expectations, payment method, and cancellation terms.","Arrange taxi both ways if your resort does not provide transport.","Use snorkeling, Copalita, or La Crucecita as backup if access is not operating."],
    "directory":[("Las Parotas / Tangolunda golf references","Verify direct/current status before committing."),("Tangolunda resort concierge","Useful for same-week status and transport checks."),("Chahué beach","Easy non-golf companion plan nearby."),("La Crucecita dinner","Best evening pairing after a resort-zone morning.")],
    "pairs":[("/destinations/tangolunda/","Tangolunda bay"),("/travel-guide/getting-around/","Getting around"),("/things-to-do/la-crucecita-market/","La Crucecita town stop")],
    "sources":["regional"]
},
"sunset-chahue": {
    "title":"Sunset and Evening in Chahué",
    "desc":"How to use Chahué for an easy late-afternoon beach walk, marina-adjacent dinner, or low-effort evening when a long excursion is too much.",
    "verdict":"Chahué is best as an easy evening reset, not a must-do spectacle. Use it when you want a simple beach walk, marina context, and dinner without the logistics of a remote bay.",
    "choose":["Visitors staying near Chahué, Santa Cruz, or La Crucecita.","Families who want a low-friction evening after a boat or arrival day.","Couples who want a beach walk before dinner but not a remote sunset mission."],
    "avoid":["Expecting the calmest swim conditions; Chahué can be stronger than it looks.","Going only for a once-in-a-lifetime sunset viewpoint.","Walking back long distances late if your hotel is not nearby."],
    "route":"Taxi or walk from nearby hotels, use the beach for a short stroll, then move to dinner rather than lingering with valuables in the dark. If the water looks rough, keep it as a view and sand stop, not a swim plan.",
    "logistics":["Go before dark enough to read the beach and choose your return plan.","Keep swimming conservative and respect local conditions.","Pair with La Crucecita dinner or a Chahué-area restaurant instead of a second excursion.","Carry only what you need for the evening."],
    "directory":[("Playa Chahué","Main evening beach-walk anchor."),("Chahué marina area","Useful orientation point and dinner nearby."),("La Crucecita zócalo","Easy follow-up for dinner or ice cream."),("Santa Cruz","Alternative if your group wants a busier bay-front feel.")],
    "pairs":[("/destinations/chahue/","Chahué bay"),("/food-culture/","Food guide"),("/travel-guide/safety/","Safety guide")],
    "sources":["infrastructure"]
},
"surf-open-coast": {
    "title":"Surf and Open-Coast Water Days",
    "desc":"How to think about surf, open-coast beaches, lessons, and safety around Huatulco without confusing exposed Pacific water with protected bay swimming.",
    "verdict":"Huatulco is more famous for bays than surf. Treat surf or open-coast days as condition-led and ability-led. Beginners should look for lessons and local guidance; swimmers should not assume an exposed beach is safe because it looks beautiful.",
    "choose":["Travelers who understand ocean conditions and are willing to ask local advice.","Beginners who book a lesson instead of improvising at an exposed beach.","Visitors with extra days who can keep surf plans flexible."],
    "avoid":["Families looking for the easiest swim day; use Maguey, Santa Cruz, or hotel pools instead.","Remote beaches with no lifeguards/services if your group lacks ocean experience.","Any day when swell, wind, or local warnings say no."],
    "route":"Use the bay guides to separate protected-water days from open-coast days. If a local school or operator recommends a specific break, follow their timing and transport plan. Keep a dry fallback so a no-surf day does not feel wasted.",
    "logistics":["Ask about board rental, lesson level, rash guard, transport, and where the lesson actually happens.","Do not leave valuables unattended on quiet beaches.","Protect the afternoon from heat and sun; lessons are better earlier.","If conditions are wrong, switch to Copalita, La Crucecita, or a bay-view lunch."],
    "directory":[("Local surf instructors","Verify same-week conditions and beginner suitability."),("Open-coast beaches","Use only with local advice and clear exit points."),("Maguey / Santa Cruz","Better fallback for easy water days."),("Copalita","Dry half-day backup when water is not cooperating.")],
    "pairs":[("/travel-guide/safety/","Safety guide"),("/destinations/","Bay comparison"),("/things-to-do/snorkeling/","Snorkeling guide")],
    "sources":["operators"]
},
}

ITINS = {
"3-days-huatulco": {
    "title":"3 Days in Huatulco Itinerary",
    "desc":"A first-trip Huatulco plan that protects one boat day, one town/culture day, and enough easy beach time to avoid turning a short trip into a checklist.",
    "fit":"Best for first-time visitors with two full days and one arrival/departure cushion. Choose Santa Cruz, Chahué, or Tangolunda as your base depending on whether you want marina access, central movement, or resort calm.",
    "avoid":"Avoid this route if your real goal is Mazunte or the wider Oaxaca coast. With only three days, west-coast day trips steal too much time from the bays.",
    "days":[
        ("Day 1", "Arrival, base choice, and an easy bay", "Settle into Santa Cruz, Chahué, or Tangolunda. Do not chase a remote beach after airport arrival.", "Use the first afternoon for Santa Cruz or your hotel beach, then dinner in La Crucecita if energy allows.", "Keep the evening simple: town dinner, cash stop, and confirm tomorrow's water plan.", "Taxi from HUX to your base; compare hotel/private transfer options before arrival."),
        ("Day 2", "Boat route through the bays", "Take the earliest good-weather boat route from Santa Cruz. Ask where snorkeling is realistic today.", "Use the main swim/lunch stop for actual downtime instead of trying to count every bay.", "Return, shower, and choose a low-effort dinner near your base.", "Book with hotel pickup or a clear pier meeting point; keep a backup morning if weather shifts."),
        ("Day 3", "La Crucecita, Copalita, or one more beach", "Choose La Crucecita market if you want town/food, Copalita if you want culture, or Maguey if you want one more easy beach.", "Protect departure logistics. Do not put a remote beach or long lunch too close to airport time.", "If staying another night, use Chahué/Santa Cruz for a relaxed final evening.", "Use taxis for short hops; arrange pickup for Copalita or remote beaches.")
    ],
    "pairs":[("/things-to-do/boat-tours/","Boat tours"),("/travel-guide/airport-arrival/","Airport arrival"),("/food-culture/","Food guide")]
},
"4-days-relax-snorkel": {
    "title":"4 Days in Huatulco for Relaxing and Snorkeling",
    "desc":"A practical four-day route for travelers who want calm water, a boat day, town food, and enough downtime to avoid over-scheduling Huatulco.",
    "fit":"Best for couples, families, and first-timers who want Huatulco to feel easy: one arrival day, one true water day, one flexible town/culture day, and one final bay day. Choose Santa Cruz for boat access, Chahué for central movement, or Tangolunda for resort calm.",
    "avoid":"Avoid this plan if your priority is surfing, nightlife, or a long west-coast loop. This route intentionally keeps Mazunte and Puerto Ángel out unless you add a fifth day.",
    "days":[
        ("Day 1", "Arrive and choose your easiest water", "Check in, unpack, and use Santa Cruz, Chahué, or your resort beach as the easy first swim/look-around.", "Do a short grocery/cash run in La Crucecita if your hotel location makes that practical.", "Eat in town or near your base, then confirm tomorrow's snorkel/boat conditions.", "Pre-arrange airport transfer or taxi; do not negotiate your whole trip plan tired at arrival."),
        ("Day 2", "Protected bay snorkeling or boat day", "Use the morning for your best water conditions. Pick a Santa Cruz boat route or Maguey-style easy snorkel depending on your group.", "Take the long lunch/swim stop seriously; this is the day to be in the water, not in taxis.", "Keep dinner simple after sun exposure. La Crucecita works if everyone still has energy.", "Ask about snorkel gear, shade, lunch, fees, and return time before paying."),
        ("Day 3", "Town, market, Copalita, or recovery day", "If everyone wants a dry day, go to Mercado 3 de Mayo in La Crucecita or Copalita early. If the water was poor yesterday, use this as your backup snorkel morning.", "Return to a hotel pool, Chahué, or Santa Cruz. Avoid stacking another long excursion unless the group wants it.", "Plan a better dinner: Terra-Cotta, El Sabor de Oaxaca, Mercader, or a bay seafood spot depending on your base.", "Use taxis for La Crucecita; arrange wait/return for Copalita."),
        ("Day 4", "Final bay and departure-friendly plan", "Choose the easiest bay near your base: Maguey for beach lunch, Santa Cruz for logistics, or Tangolunda for resort calm.", "Pack before lunch if departing. If staying overnight, this can be your second water attempt.", "One last town walk or early night before travel.", "Do not put Cacaluta, Chachacual, or a west-coast drive on departure day.")
    ],
    "pairs":[("/things-to-do/snorkeling/","Snorkeling"),("/things-to-do/boat-tours/","Boat tours"),("/travel-guide/getting-around/","Getting around")]
},
"5-days-oaxaca-coast": {
    "title":"5 Days in Huatulco and the Oaxaca Coast",
    "desc":"A five-day route that adds one wider Oaxaca coast day without sacrificing Huatulco's bays, town food, Copalita, and easy beach recovery time.",
    "fit":"Best for travelers who want Huatulco as the base but still want one look west toward Mazunte, San Agustinillo, or Puerto Ángel. The key is to protect the boat day and treat the west-coast loop as one focused day, not three rushed towns.",
    "avoid":"Avoid if your group hates long drives or if water days are the only priority. Use the four-day relax/snorkel route instead and keep the extra day for weather backup.",
    "days":[
        ("Day 1", "Arrival and central bay orientation", "Settle near Santa Cruz, Chahué, or Tangolunda and do the easiest nearby beach first.", "Use La Crucecita for cash, snacks, and a simple first town dinner.", "Confirm boat/weather plans for Day 2 or 3.", "Airport transfer first; short taxis only after check-in."),
        ("Day 2", "Nine-bay style boat route", "Use the best morning for the classic bay route from Santa Cruz.", "Swim/snorkel where conditions are actually good, not where the brochure promised.", "Eat near your base and rest.", "Choose an operator with clear pickup, lunch, gear, and fee terms."),
        ("Day 3", "Copalita and town context", "Visit Copalita early, or use La Crucecita market if the site/status does not fit your group.", "Pair with Bocana/Tangolunda lunch or a resort pool afternoon.", "Use this as your nicer dinner night in town.", "Agree on taxi wait/pickup for Copalita before entering."),
        ("Day 4", "Mazunte, San Agustinillo, or Puerto Ángel", "Leave early and choose one main west-coast anchor. Mazunte works best when the town and turtle-center context are the focus.", "Add San Agustinillo or Puerto Ángel only if the day still feels relaxed.", "Return before everyone is exhausted; dinner should be simple.", "Private driver or reputable tour is easier than improvising the return."),
        ("Day 5", "Easy final beach or backup water day", "Use Maguey, Santa Cruz, Chahué, or your resort beach depending on departure time.", "If a previous water day failed, this is your backup window.", "Pack, settle bills, and keep the airport plan boring.", "No remote beaches on departure day unless you are staying another night.")
    ],
    "pairs":[("/towns-cities/mazunte/","Mazunte"),("/things-to-do/copalita-archaeology/","Copalita"),("/travel-guide/best-time-to-visit/","Best time")]
},
"snorkel-boat-day": {
    "title":"One-Day Huatulco Snorkel and Boat Plan",
    "desc":"A one-day Huatulco water plan that protects the morning, asks the right operator questions, and gives you a useful backup if the sea is not cooperating.",
    "fit":"Best for visitors with one dedicated water day. This is not a full vacation itinerary; it is the safest way to structure the boat/snorkel decision inside a longer trip.",
    "avoid":"Avoid promising this day to kids or nervous swimmers until you have checked conditions. If the water is rough, switch to a bay-view lunch and town/culture plan.",
    "days":[
        ("Day plan", "Morning conditions and operator check", "Check sea conditions and meet at Santa Cruz or your pickup point. Confirm snorkel gear, shade, lunch, fees, and exact return time.", "Use the best swim/snorkel stop while visibility is good. Do not force a second snorkel if everyone is tired or cold.", "Return, shower, hydrate, and eat close to your base or in La Crucecita.", "Keep hotel pickup or taxi return simple; sun and boat days make people slower than expected."),
        ("Backup plan", "If water is poor", "Switch to Copalita, La Crucecita market, or a protected beach lunch where swimming is optional.", "Use the afternoon for hotel pool time, Chahué walk, or Santa Cruz bay-front restaurants.", "Rebook the water attempt for the next calm morning if your itinerary allows.", "Do not let a cancelled snorkel day become a random overpriced replacement tour."),
    ],
    "pairs":[("/things-to-do/snorkeling/","Snorkeling"),("/things-to-do/boat-tours/","Boat tours"),("/travel-guide/safety/","Safety")]
}
}

GUIDES = {
"airport-arrival": {
    "title":"Huatulco Airport Arrival Guide",
    "desc":"What to do after landing at HUX: transfer choices, first-hour priorities, cash, groceries, hotel-zone timing, and what not to schedule on arrival day.",
    "verdict":"Make arrival day boring on purpose. Land, get to your base, settle cash/food basics, and choose an easy bay or dinner. Do not schedule a remote beach, west-coast drive, or condition-dependent snorkel plan for the same day.",
    "steps":["Before flying, decide whether your hotel includes pickup, whether you want a private transfer, or whether you will use airport taxi service.","Send your flight number and hotel/base area to the transfer provider when possible.","On arrival, prioritize water, cash, check-in, and a simple first meal over sightseeing.","Confirm the next morning's boat/snorkel plan only after you know weather and group energy."],
    "local":"HUX sits outside the main bays, so La Crucecita, Santa Cruz, Chahué, and Tangolunda all require a real transfer rather than a casual walk. Tangolunda and Conejos feel calmer after arrival; Santa Cruz and Chahué are easier if you want marina/town movement.",
    "mistake":"The common mistake is treating arrival day as a full vacation day. Flight delays, heat, luggage, and unfamiliar taxi logistics make big plans fragile.",
    "table":[("Hotel pickup","Easiest if included","Confirm flight number, waiting policy, and whether it is private or shared."),("Private transfer","Best for families or late arrivals","Confirm vehicle size, child seats if needed, and total price before arrival."),("Airport taxi","Good if you want simple point-to-point","Know your base area name: La Crucecita, Santa Cruz, Chahué, Tangolunda, Conejos, or Bocana.")],
    "pairs":[("/travel-guide/getting-around/","Getting around"),("/itineraries/3-days-huatulco/","3-day itinerary"),("/food-culture/","Food guide")],
    "sources":["infrastructure"]
},
"getting-around": {
    "title":"Getting Around Huatulco",
    "desc":"How to move between Huatulco airport, La Crucecita, Santa Cruz, Chahué, Tangolunda, Maguey, Copalita, and farther Oaxaca coast day trips.",
    "verdict":"Use taxis and planned pickups for most short hops. Rent a car only if you are comfortable with parking, remote beach access, and longer west-coast drives. The biggest mistake is assuming every bay is equally easy to reach and return from.",
    "steps":["Choose your base first: Santa Cruz for boat access, Chahué for central movement, Tangolunda for resort calm, La Crucecita for food/errands.","Use taxis for La Crucecita, Santa Cruz, Chahué, Tangolunda, and Maguey-style short hops.","Pre-arrange pickup or wait time for Copalita, Bocana, remote beaches, and late dinners.","Use a private driver or tour for Mazunte, Puerto Ángel, or multi-stop west-coast days."],
    "local":"Huatulco is spread across bays, not one walkable beach strip. A map can make Santa Cruz, Chahué, and La Crucecita look close, but heat, luggage, hills, and road design decide whether walking makes sense. Tangolunda is resort-comfortable but less spontaneous for town evenings.",
    "mistake":"The common mistake is taking a taxi out to a quiet place without a return plan. Remote beaches and Copalita-style stops need pickup clarity before you relax.",
    "table":[("Short taxi hop","La Crucecita, Santa Cruz, Chahué, Tangolunda","Best default for dinners, errands, marina starts, and easy beach moves."),("Planned taxi wait/pickup","Copalita, Bocana, late dinners, quiet beaches","Agree on timing before entering a site or starting dinner."),("Private driver/tour","Mazunte, Puerto Ángel, multi-stop coast day","Better when distance, heat, and return fatigue matter."),("Rental car","Independent travelers with several remote stops","Useful, but only if you accept parking, road, insurance, and designated-driver realities.")],
    "pairs":[("/travel-guide/airport-arrival/","Airport arrival"),("/towns-cities/","Towns"),("/destinations/","Bay comparison")],
    "sources":["infrastructure"]
},
"best-time-to-visit": {
    "title":"Best Time to Visit Huatulco",
    "desc":"How to choose Huatulco dates around heat, dry season, water visibility, crowds, rain, and the kind of trip you actually want.",
    "verdict":"The best time is not one universal month. Dry-season trips are easier for beach planning; shoulder periods can feel quieter; rainy months require more flexible mornings and backup plans. Match dates to your tolerance for heat, crowds, and weather risk.",
    "steps":["If this is your first trip, prioritize easier beach conditions over chasing the cheapest dates.","Protect water activities early in the trip so you can move them if wind, swell, or rain changes conditions.","Plan Copalita, La Crucecita, food, and town time as weather backups, not filler.","For holiday periods, book transfers and boat days earlier and expect less spontaneity."],
    "local":"Huatulco's bays can feel protected compared with exposed Pacific coast, but visibility and comfort still change. Heat affects archaeology, markets, and walking as much as it affects beach days. A good itinerary leaves the hottest or wettest window for meals, pool time, or low-effort errands.",
    "mistake":"The common mistake is asking only, 'Will it rain?' Better question: can you move your snorkel or boat morning if the first option is not ideal?",
    "table":[("Dry-season beach trip","Best for first-timers and families","Easier planning, stronger demand around holidays, book key logistics early."),("Shoulder trip","Best for flexible travelers","Can feel calmer, but keep backup mornings for water plans."),("Rainier/warmer period","Best for price-tolerant repeat visitors","Use mornings well, keep afternoons flexible, and do not overpromise remote water days.")],
    "pairs":[("/itineraries/4-days-relax-snorkel/","4-day snorkel plan"),("/things-to-do/snorkeling/","Snorkeling"),("/travel-guide/packing-list/","Packing list")],
    "sources":["infrastructure"]
},
"first-time-visitors": {
    "title":"First-Time Huatulco Visitor Guide",
    "desc":"The simplest way to plan a first Huatulco trip: choose your base, protect one boat day, add La Crucecita, and avoid overloading remote beach logistics.",
    "verdict":"For a first trip, do less and understand the bays better. Choose a base, do one boat or snorkel day, use La Crucecita for food/town context, and add Copalita or Maguey only when the schedule still feels easy.",
    "steps":["Pick your base by trip style: Santa Cruz for boat access, Chahué for central balance, Tangolunda for resort calm, La Crucecita for town/food.","Reserve one good-weather morning for boat/snorkel plans.","Use one non-water block for La Crucecita market or Copalita so the trip does not become only sand.","Keep a backup plan for rough water: town, food, archaeology, pool, or an easier bay."],
    "local":"Huatulco is a bay system. Visitors who expect one Cancun-style strip often overplan. The best first trip has a rhythm: easy arrival, real water day, town/culture context, flexible final beach.",
    "mistake":"The common mistake is trying to visit every named bay, Mazunte, Puerto Ángel, Copalita, and all the restaurants in a short trip. That creates car time, not a better vacation.",
    "table":[("3 nights","One boat day + La Crucecita + easy final bay","Skip Mazunte and long west-coast loops."),("4 nights","Boat/snorkel + town/culture + backup beach","Best first-trip rhythm for most visitors."),("5+ nights","Add Mazunte/Puerto Ángel or a second water attempt","Still keep one recovery day after long drives.")],
    "pairs":[("/itineraries/3-days-huatulco/","3-day itinerary"),("/itineraries/4-days-relax-snorkel/","4-day itinerary"),("/things-to-do/boat-tours/","Boat tours")],
    "sources":["infrastructure"]
},
"money-tipping": {
    "title":"Money and Tipping in Huatulco",
    "desc":"How to handle cash, cards, tips, market purchases, taxis, tours, and small beach expenses in Huatulco without making every stop awkward.",
    "verdict":"Carry more small cash than you think you need, especially for taxis, markets, beach palapas, tips, and remote stops. Cards are useful at hotels and many restaurants, but cash keeps Huatulco logistics smoother.",
    "steps":["Get small bills early in La Crucecita or through your hotel/ATM routine.","Ask tour operators what is included and what is cash-only before departure.","Keep tip money separate for drivers, boat crews, guides, and restaurant staff.","Do not rely on one card or one ATM visit for the whole trip."],
    "local":"La Crucecita is the easiest place to solve cash, pharmacy, small purchases, and errands. Remote beaches, market counters, taxis, and smaller operators are where cash matters most. For high-value tours, verify payment method and cancellation terms before handing over money.",
    "mistake":"The common mistake is arriving with large bills and expecting every beach restaurant or taxi to make change. Small denominations reduce friction.",
    "table":[("Taxis","Cash is safest","Ask approximate fare before starting if there is no posted rate."),("Boat/tours","Mixed payment methods","Confirm deposit, balance, inclusions, fees, and cancellation terms."),("Markets/small food","Cash preferred","Bring small bills and coins for quick purchases."),("Hotels/larger restaurants","Cards often useful","Still keep cash for tips and transport.")],
    "pairs":[("/things-to-do/la-crucecita-market/","La Crucecita market"),("/travel-guide/getting-around/","Getting around"),("/food-culture/","Food guide")],
    "sources":["infrastructure"]
},
"packing-list": {
    "title":"Huatulco Packing List",
    "desc":"What to pack for Huatulco's sun, boats, markets, dry walks, remote beaches, and airport-to-hotel logistics without overpacking resort extras.",
    "verdict":"Pack for sun, salt, heat, and short practical moves between bays. The useful items are not fancy: reef-safe sun protection, sandals plus walking shoes, dry bag, light layers, cash system, and backup swimwear.",
    "steps":["Pack one boat-day kit: dry bag, sun shirt, hat, water, motion-sickness help if needed, and cash.","Pack one town/culture kit: comfortable shoes, light shirt, small cash, and refillable water.","Bring more sun protection than your resort shop budget wants you to buy.","Leave room for market purchases if La Crucecita is on your list."],
    "local":"Huatulco days often combine beach, taxi, town, and dinner. Clothes that work only for a resort pool are less useful than light pieces you can wear from boat to lunch to La Crucecita. Copalita and market walks need better footwear than flip-flops.",
    "mistake":"The common mistake is underestimating sun exposure on boat days. Shade may be limited, and water reflection makes a casual swim day feel much stronger.",
    "table":[("Boat/snorkel day","Dry bag, rash guard, hat, sunglasses, cash, towel","Protects valuables and skin during long sun exposure."),("Town/market day","Walking sandals/shoes, small bills, light bag","Makes La Crucecita and errands easier."),("Copalita/culture stop","Closed or stable shoes, water, breathable clothing","Paths and heat matter more than dressy resort wear."),("Departure day","Separate dry/dirty bag, easy airport outfit","Avoids packing wet swimwear into everything else.")],
    "pairs":[("/things-to-do/boat-tours/","Boat tours"),("/things-to-do/copalita-archaeology/","Copalita"),("/travel-guide/best-time-to-visit/","Best time")],
    "sources":["infrastructure"]
},
"safety": {
    "title":"Huatulco Safety Guide",
    "desc":"How to think about Huatulco safety through water conditions, remote beaches, heat, transport, valuables, and practical family decisions.",
    "verdict":"Most visitor safety decisions in Huatulco are practical, not dramatic: water conditions, heat, return transport, remote beach services, and valuables. Treat each bay by access and conditions, not by how calm it looks in photos.",
    "steps":["Choose water by the day's conditions and your weakest swimmer, not by the prettiest photo.","Use planned transport for late returns, remote beaches, Copalita, and west-coast trips.","Carry water, sun protection, and cash when leaving resort zones.","Keep valuables out of sight in cars and do not leave phones/wallets unattended on quiet beaches."],
    "local":"Santa Cruz and Maguey are easier for services. Cacaluta, Chachacual, and quiet open-coast areas require more self-sufficiency. Chahué can be a pleasant evening walk but not always the easiest swim. Copalita is close enough to feel simple but still needs a return plan.",
    "mistake":"The common mistake is calling a beach 'safe' or 'unsafe' as a permanent label. Conditions, access, services, and group ability decide the answer that day.",
    "table":[("Easy-service bays","Santa Cruz, Maguey, resort beaches","Better for families, short visits, and backup plans."),("Remote/scenic beaches","Cacaluta, Chachacual, quiet coves","Go with boat/transport clarity, water, sun protection, and realistic swim expectations."),("Town/culture stops","La Crucecita, Copalita","Watch heat, cash, return timing, and footwear."),("Long coast days","Mazunte, Puerto Ángel","Use a reliable driver/tour and do not return exhausted after dark if avoidable.")],
    "pairs":[("/things-to-do/snorkeling/","Snorkeling"),("/travel-guide/getting-around/","Getting around"),("/destinations/","Bay guide")],
    "sources":["infrastructure"]
}
}


def render_activity(slug, d):
    entity_attrs = {
        'boat-tours': " data-entity-depth='boat-tours' data-approved-route-media='true'",
        'snorkeling': " data-entity-depth='snorkeling' data-approved-route-media='true'",
        'copalita-archaeology': " data-entity-depth='copalita'",
        'la-crucecita-market': " data-entity-depth='la-crucecita-market'",
    }
    media = {
        'boat-tours': ("/images/photos/huatulco-maguey-bay-jpg-mosaic.webp", "Maguey Bay boat-day water near Huatulco"),
        'snorkeling': ("/images/photos/huatulco-playa-riscalillo-bah-as-de-huatulco-1-jpg-mosaic.webp", "Playa Riscalillo snorkeling-style coastline near Huatulco"),
    }
    media_html = ""
    if slug in media:
        src, alt = media[slug]
        media_html = f"<figure class='mt-8 overflow-hidden rounded-[1.75rem] border border-border bg-white shadow-card'><img class='h-72 w-full object-cover' src='{src}' alt='{e(alt)}' loading='lazy'><figcaption class='px-5 py-3 text-sm text-ink/65'>{e(alt)}</figcaption></figure>"
    rows = [("Choose", "<br>".join(d["choose"])), ("Avoid", "<br>".join(d["avoid"])), ("Pair with", "<br>".join(f"<a class='font-bold text-primary' href='{href}'>{e(label)}</a>" for href,label in d["pairs"]))]
    directory = "".join(card(name, e(text)) for name, text in d["directory"])
    body = f"""
<section class='section-pad'><div class='container-xl max-w-6xl'>
  <nav class='guide-toc card p-5' aria-label='On-page guide sections'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>On this page</p><div class='mt-3 grid gap-3 sm:grid-cols-4'><a data-guide-nav-link href='#verdict' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Quick verdict</a><a data-guide-nav-link href='#decision' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Choose or avoid</a><a data-guide-nav-link href='#logistics' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Logistics</a><a data-guide-nav-link href='#directory' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Local options</a></div></nav>
  <div id='verdict' class='mt-8 grid gap-6 lg:grid-cols-[1.1fr_.9fr]'><div class='card p-7'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>Quick verdict</p><h2 class='mt-2'>Should you put this in your Huatulco plan?</h2><p class='mt-3 leading-8 text-ink/75'>{e(d['verdict'])}</p></div><div class='card bg-surface p-7'><h2>Route logic</h2><p class='mt-3 leading-8 text-ink/75'>{e(d['route'])}</p></div></div>
  {media_html}
  <section id='decision' class='mt-8'><h2 class='font-heading text-3xl font-semibold'>Choose it, skip it, or pair it correctly</h2>{table(['Decision','Visitor guidance'], rows)}</section>
  <section id='logistics' class='mt-10'><h2 class='font-heading text-3xl font-semibold'>Practical logistics and common mistakes</h2><div class='mt-6 grid gap-6 lg:grid-cols-2'>{card('How to plan it', ul(d['logistics']))}{card('Better backup idea', 'If conditions, timing, or group energy do not fit, switch to one of the paired guides below rather than forcing the original plan. Huatulco works best when water days, town time, and easy beach meals can trade places.')}</div></section>
  <section class='mt-10' data-visitor-scenario-rules='activity'><h2 class='font-heading text-3xl font-semibold'>How this usually fits into a real trip</h2>{table(['Trip situation','Use this activity this way','What to check first'], [('Arrival or first full day','Keep it easy unless this is a confirmed morning water plan. Use the activity to learn the bays, not to prove you can see everything.','Pickup point, return time, cash needs, and whether the group has recovered from travel.'),('Family or mixed-energy group','Prioritize shade, bathrooms, short transfers, and a clear way to stop early if someone is done.','Services nearby, cancellation rules, and whether the plan still works if the youngest or oldest traveler opts out.'),('Couples or active travelers','Use the activity as the anchor of the day, then add one relaxed meal or beach stop nearby instead of another big excursion.','Weather, heat, water visibility, and whether dinner transport is still simple.')])}</section>
  <section id='directory' class='mt-10'><h2 class='font-heading text-3xl font-semibold'>Local options to check</h2><p class='mt-3 max-w-3xl leading-7 text-ink/75'>These are planning anchors, not paid placements. Use them to compare current details, location fit, and whether the activity really suits your group.</p><div class='mt-6 grid gap-6 md:grid-cols-2'>{directory}</div></section>
  <section class='mt-10'><h2 class='font-heading text-3xl font-semibold'>Use these next</h2><div class='mt-5 flex flex-wrap gap-3'>{''.join(f"<a class='rounded-full bg-primary px-5 py-3 text-sm font-bold text-white shadow-soft' href='{href}'>{e(label)}</a>" for href,label in d['pairs'])}</div></section>
</div></section>
{source_box(d['sources'])}
"""
    write_page(f"things-to-do/{slug}/index.html", page_html(d['title'], d['desc'], f"/things-to-do/{slug}/", "Things to do", body, marker="data-section-depth-reset='true' data-subject-led-guide='true' data-priority-guide-depth='visitor-reference'" + entity_attrs.get(slug, "")))


def render_itin(slug, d):
    itin_marker = "data-section-depth-reset='true' data-subject-led-guide='true' data-priority-guide-depth='visitor-reference'"
    media_html = ""
    if slug == '5-days-oaxaca-coast':
        itin_marker += " data-approved-route-media='true'"
        media_html = "<figure class='mt-8 overflow-hidden rounded-[1.75rem] border border-border bg-white shadow-card'><img class='h-72 w-full object-cover' src='/images/photos/huatulco-bahia-san-agustin-huatulco-camping-webp.webp' alt='Bahia San Agustin Huatulco camping beach context' loading='lazy'><figcaption class='px-5 py-3 text-sm text-ink/65'>Bahia San Agustin Huatulco camping beach context for longer Oaxaca coast plans.</figcaption></figure>"
    days = "".join(f"""<article class='card p-7' data-itinerary-day='{e(day)}'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>{e(day)}</p><h3 class='mt-2 font-heading text-2xl font-semibold'>{e(title)}</h3><div class='mt-5 grid gap-4 md:grid-cols-2'><p><strong>Morning:</strong> {e(morning)}</p><p><strong>Afternoon:</strong> {e(afternoon)}</p><p><strong>Evening:</strong> {e(evening)}</p><p><strong>Getting around:</strong> {e(transport)}</p></div></article>""" for day,title,morning,afternoon,evening,transport in d['days'])
    body = f"""
<section class='section-pad'><div class='container-xl max-w-6xl'>
  <nav class='guide-toc card p-5' aria-label='On-page guide sections'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>On this page</p><div class='mt-3 grid gap-3 sm:grid-cols-4'><a data-guide-nav-link href='#fit' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Who it fits</a><a data-guide-nav-link href='#days' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Day-by-day plan</a><a data-guide-nav-link href='#backup' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Backups</a><a data-guide-nav-link href='#next' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Next guides</a></div></nav>
  <section id='fit' class='mt-8 grid gap-6 lg:grid-cols-2'>{card('Who this route fits', e(d['fit']))}{card('Who should avoid it', e(d['avoid']))}</section>
  {media_html}
  <section id='days' class='mt-10'><h2 class='font-heading text-3xl font-semibold'>Day-by-day plan</h2><p class='mt-3 max-w-3xl leading-7 text-ink/75'>Each day has a job. Keep the route clustered so the trip feels like Huatulco, not a series of transfers.</p><div class='mt-6 grid gap-6'>{days}</div></section>
  <section id='backup' class='mt-10'><h2 class='font-heading text-3xl font-semibold'>Backup logic</h2>{table(['If this changes','Switch to this'], [('Rough water or poor visibility','Move the boat/snorkel morning to the next calm day. Use La Crucecita, Copalita, or a hotel-pool afternoon instead.'),('Everyone is tired after sun or travel','Cancel the extra excursion first, not the easy meal or transfer plan.'),('Departure timing is tight','Use Santa Cruz, Chahué, Tangolunda, or La Crucecita. Do not choose remote beaches or west-coast drives.')])}</section>
  <section class='mt-10' data-itinerary-base-strategy='true'><h2 class='font-heading text-3xl font-semibold'>Base, meals, and pacing rules</h2>{table(['Decision','Best rule','Why it matters'], [('Base area','Choose Santa Cruz for boat access, Chahué for central movement, Tangolunda for resort calm, or La Crucecita for town food and errands.','The same itinerary feels very different if every dinner, pier start, or market stop requires a taxi.'),('Food rhythm','Put better dinners after lighter days and keep boat-day dinners close to your base.','Sun, salt water, and transfers make ambitious evening plans less appealing.'),('Backup morning','Keep at least one morning movable for boat or snorkel conditions.','Huatulco rewards flexible water planning more than rigid reservations.'),('Departure day','Use nearby bays, town errands, or hotel pool time.','Remote beaches and long lunches create avoidable airport stress.')])}</section>
  <section id='next' class='mt-10'><h2 class='font-heading text-3xl font-semibold'>Use these guides with this itinerary</h2><div class='mt-5 flex flex-wrap gap-3'>{''.join(f"<a class='rounded-full bg-primary px-5 py-3 text-sm font-bold text-white shadow-soft' href='{href}'>{e(label)}</a>" for href,label in d['pairs'])}</div></section>
</div></section>
{source_box(['infrastructure','operators','regional'])}
"""
    write_page(f"itineraries/{slug}/index.html", page_html(d['title'], d['desc'], f"/itineraries/{slug}/", "Itinerary", body, marker=itin_marker))


def render_guide(slug, d):
    body = f"""
<section class='section-pad'><div class='container-xl max-w-6xl'>
  <nav class='guide-toc card p-5' aria-label='On-page guide sections'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>On this page</p><div class='mt-3 grid gap-3 sm:grid-cols-4'><a data-guide-nav-link href='#verdict' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Quick verdict</a><a data-guide-nav-link href='#steps' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>What to do</a><a data-guide-nav-link href='#local' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Local logic</a><a data-guide-nav-link href='#next' class='rounded-2xl bg-secondary px-4 py-3 text-sm font-bold text-ink'>Next guides</a></div></nav>
  <section id='verdict' class='mt-8 grid gap-6 lg:grid-cols-[1.1fr_.9fr]'>{card('Quick verdict', e(d['verdict']))}{card('Common mistake', e(d['mistake']))}</section>
  <section id='steps' class='mt-10'><h2 class='font-heading text-3xl font-semibold'>What to do first</h2><div class='mt-6 grid gap-6 md:grid-cols-2'>{card('Step-by-step', ul(d['steps']))}{card('Same-week check', 'Before you lock this in, check current conditions, operating days, transfer details, and payment expectations. Huatulco planning is easiest when the changeable details are checked close to the date.')}</div></section>
  <section id='local' class='mt-10'><h2 class='font-heading text-3xl font-semibold'>How this works in Huatulco</h2><p class='mt-3 max-w-4xl leading-8 text-ink/75'>{e(d['local'])}</p>{table(['Situation','Best use','What to verify'], d['table'])}</section>
  <section class='mt-10' data-local-decision-rules='travel-guide'><h2 class='font-heading text-3xl font-semibold'>Decision rules that prevent friction</h2>{table(['Rule','Apply it this way','Why it helps'], [('Make the flexible thing the water day','Boat tours, snorkeling, and open-coast plans should move when conditions are wrong.','This prevents a pretty itinerary from becoming unsafe or disappointing.'),('Keep the boring logistics boring','Transfers, cash, return taxis, and departure timing should be solved before the fun part starts.','Most Huatulco stress comes from practical gaps, not from lack of attractions.'),('Use La Crucecita as the reset valve','Town errands, market food, pharmacies, cash, and simple dinners are easiest there.','It gives you a useful backup when heat, rain, rough water, or tired kids change the plan.'),('Do not overvalue distance on a map','Heat, road layout, luggage, and return taxis matter as much as kilometers.','This keeps base choice and day plans honest.')])}</section>
  <section id='next' class='mt-10'><h2 class='font-heading text-3xl font-semibold'>Use these next</h2><div class='mt-5 flex flex-wrap gap-3'>{''.join(f"<a class='rounded-full bg-primary px-5 py-3 text-sm font-bold text-white shadow-soft' href='{href}'>{e(label)}</a>" for href,label in d['pairs'])}</div></section>
</div></section>
{source_box(d['sources'])}
"""
    write_page(f"travel-guide/{slug}/index.html", page_html(d['title'], d['desc'], f"/travel-guide/{slug}/", "Travel guide", body))


def render_hubs():
    act_cards = "".join(card(d['title'], e(d['desc']) + f"<a class='mt-5 inline-flex min-h-11 items-center rounded-full bg-primary px-5 py-2.5 text-sm font-bold text-white hover:brightness-110' href='/things-to-do/{slug}/'>Open guide</a>") for slug,d in ACTIVITIES.items())
    body = f"""
<section class='section-pad'><div class='container-xl max-w-6xl'>
  <div class='card p-7' data-hub-child-cta='things-to-do-depth'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>Start here</p><h2 class='mt-2 font-heading text-3xl font-semibold'>Choose activities by the kind of day you want</h2><p class='mt-3 leading-8 text-ink/75'>Huatulco activities are not interchangeable. A boat day depends on sea conditions, Copalita depends on heat and access, Mazunte depends on drive tolerance, and La Crucecita works best as practical town time. Use this hub to choose the right type of day before choosing a vendor.</p>{table(['If you want','Start with','Avoid if'], [('Classic first-trip water day','Boat tours or snorkeling','The sea is rough or the group needs a short day'),('Culture without a long drive','Copalita or La Crucecita market','You are going at peak heat with tired kids'),('Wider Oaxaca coast context','Mazunte day trip','You only have three nights'),('Easy evening','Chahué sunset and dinner','You expect a remote viewpoint or big nightlife')])}</div>
  <div class='mt-8 grid gap-6 md:grid-cols-2 lg:grid-cols-3'>{act_cards}</div>
</div></section>
{source_box(['infrastructure','operators','regional'])}
"""
    write_page("things-to-do/index.html", page_html("Things to Do in Huatulco", "Choose Huatulco activities by water conditions, drive time, group energy, booking reality, and what each day should accomplish.", "/things-to-do/", "Activities", body))

    itin_cards = "".join(card(d['title'], e(d['desc']) + f"<a class='mt-5 inline-flex min-h-11 items-center rounded-full bg-primary px-5 py-2.5 text-sm font-bold text-white hover:brightness-110' href='/itineraries/{slug}/'>Open itinerary</a>") for slug,d in ITINS.items())
    body = f"""
<section class='section-pad'><div class='container-xl max-w-6xl'>
  <div class='card p-7' data-hub-child-cta='itinerary-depth'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>Start here</p><h2 class='mt-2 font-heading text-3xl font-semibold'>Choose the itinerary by how much movement your group wants</h2><p class='mt-3 leading-8 text-ink/75'>The best Huatulco itinerary protects one good water morning, gives La Crucecita or Copalita real space, and does not force Mazunte unless you have enough nights. Start with the day count, then choose the base and backup plan.</p>{table(['Trip length','Best route','What to skip'], [('3 nights','One boat day, one town/culture choice, one easy bay','Mazunte and multi-stop west coast loops'),('4 nights','Relax/snorkel rhythm with backup water morning','Overloading every afternoon'),('5+ nights','Add one Oaxaca coast day if the group wants the drive','Multiple remote stops on departure day'),('One water day','Snorkel/boat day plan','Pretending poor conditions will not matter')])}</div>
  <div class='mt-8 grid gap-6 md:grid-cols-2'>{itin_cards}</div>
</div></section>
{source_box(['infrastructure','operators','regional'])}
"""
    write_page("itineraries/index.html", page_html("Huatulco Itineraries", "Day-by-day Huatulco itinerary plans for 3 days, 4 relaxed snorkel days, 5 Oaxaca coast days, and one focused boat/snorkel day.", "/itineraries/", "Itineraries", body))

    guide_cards = "".join(card(d['title'], e(d['desc']) + f"<a class='mt-5 inline-flex min-h-11 items-center rounded-full bg-primary px-5 py-2.5 text-sm font-bold text-white hover:brightness-110' href='/travel-guide/{slug}/'>Open guide</a>") for slug,d in GUIDES.items())
    body = f"""
<section class='section-pad'><div class='container-xl max-w-6xl'>
  <div class='card p-7' data-hub-child-cta='travel-guide-depth'><p class='text-sm font-bold uppercase tracking-[.16em] text-primary'>Start here</p><h2 class='mt-2 font-heading text-3xl font-semibold'>Solve the practical questions before you choose beaches</h2><p class='mt-3 leading-8 text-ink/75'>Huatulco gets easier when you make a few decisions early: airport transfer, base area, cash habits, boat-day timing, and backup ideas for heat or rough water. These guides are written as decisions, not generic travel tips.</p>{table(['Question','Read first','Why it matters'], [('How do we arrive smoothly?','Airport arrival','The airport is outside the bays, so transfer choices shape your first hour.'),('Can we move around easily?','Getting around','The bays are spread out; return logistics matter.'),('When should we come?','Best time to visit','Weather affects boats, snorkeling, heat, and crowds.'),('What can go wrong?','Safety, money, packing','Small practical mistakes create most visitor friction.')])}</div>
  <div class='mt-8 grid gap-6 md:grid-cols-2 lg:grid-cols-3'>{guide_cards}</div>
</div></section>
{source_box(['infrastructure'])}
"""
    write_page("travel-guide/index.html", page_html("Huatulco Travel Guide", "Practical Huatulco travel guides for arrival, transport, timing, money, packing, first visits, and safety decisions.", "/travel-guide/", "Travel guide", body))


def write_page(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')

for slug, data in ACTIVITIES.items():
    render_activity(slug, data)
for slug, data in ITINS.items():
    render_itin(slug, data)
for slug, data in GUIDES.items():
    render_guide(slug, data)
render_hubs()
print(f"section depth reset wrote {len(ACTIVITIES)+len(ITINS)+len(GUIDES)+3} pages")
