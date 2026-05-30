from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = {
    'food-culture/index.html': """
<section class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='food-culture'>
  <div class='container-xl max-w-6xl'>
    <div class='grid gap-6 lg:grid-cols-[1.1fr_.9fr]'>
      <article class='card p-7 sm:p-8'>
        <p class='eyebrow'>Quick verdict</p>
        <h2 class='mt-2 text-3xl'>Use La Crucecita for serious eating; use the bays for seafood lunches.</h2>
        <p class='mt-4 leading-8 text-ink/75'>Huatulco eating works best when you split the day: market or cafe breakfast in town, a simple seafood lunch on the bay you are actually visiting, then a La Crucecita dinner where Oaxacan cooking, mezcal, coffee, and casual local restaurants are concentrated. Resort restaurants are convenient, but they should not be your whole food plan.</p>
        <div class='mt-6 grid gap-4 md:grid-cols-3'>
          <div class='rounded-[1.25rem] bg-secondary p-4'><strong>Choose</strong><p class='mt-2 text-sm leading-6 text-ink/70'>La Crucecita when you want mole, tlayudas, mezcal, coffee, bakeries, and non-resort dinner options.</p></div>
          <div class='rounded-[1.25rem] bg-secondary p-4'><strong>Avoid</strong><p class='mt-2 text-sm leading-6 text-ink/70'>Driving out to a beach palapa at night unless you have confirmed it is open and have return transport arranged.</p></div>
          <div class='rounded-[1.25rem] bg-secondary p-4'><strong>Pair with</strong><p class='mt-2 text-sm leading-6 text-ink/70'>La Crucecita church/plaza, Mercado 3 de Mayo, Santa Cruz pier, or a sunset stop at Chahué.</p></div>
        </div>
      </article>
      <aside class='card p-7 sm:p-8'>
        <p class='eyebrow'>How to use this page</p>
        <h2 class='mt-2 text-2xl'>Do not treat this as a fixed ranking.</h2>
        <p class='mt-3 text-sm leading-7 text-ink/70'>Restaurants change hours, menus, ownership, and quality faster than bay geography changes. Use the named places below as starting points, then verify current hours, reservation needs, and recent reviews before building a night around one place.</p>
        <a class='mt-5 inline-flex min-h-11 items-center rounded-full bg-primary px-5 py-2.5 text-sm font-bold text-white hover:bg-primaryDark' href='/things-to-do/la-crucecita-market/'>Plan the market stop</a>
      </aside>
    </div>

    <section class='mt-10' data-named-entity-directory='huatulco-food'>
      <p class='eyebrow'>Named places to check</p>
      <h2 class='mt-2 text-3xl'>A practical Huatulco food shortlist</h2>
      <div class='mt-6 grid gap-5 md:grid-cols-2'>
        <div class='card p-6'><h3>Terra-Cotta — La Crucecita square</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Strong first-night choice for Oaxacan plates, mole negro, Pluma Hidalgo coffee, mezcal, breakfast, and an easy town-square location at Misión de los Arcos.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.terracotta.com.mx/'>Check Terra-Cotta directly</a></div>
        <div class='card p-6'><h3>El Sabor de Oaxaca — traditional Oaxacan food</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Useful when the goal is regional cooking rather than a view: moles, tamales, platters, and a more Oaxaca-first dinner plan in La Crucecita.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.facebook.com/elsabordeoaxacahuatulco/'>Check current page</a></div>
        <div class='card p-6'><h3>Mercader — small international dinner option</h3><p class='mt-2 text-sm leading-6 text-ink/70'>A compact Santa Cruz / La Crucecita-area restaurant to check when your group wants something beyond seafood and Oaxacan classics.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.facebook.com/mercaderhuatulco/'>Check current page</a></div>
        <div class='card p-6'><h3>Casa Bocana — coastal dinner near Copalita</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Best saved for a Bocana/Copalita evening rather than a casual town meal. Verify whether you need a reservation and whether your hotel transfer is easy after dark.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.casabocana.mx/en-gb/restaurante'>Check Casa Bocana</a></div>
        <div class='card p-6'><h3>Mercado 3 de Mayo — breakfast, snacks, supplies</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Use the market for fruit, simple breakfasts, chocolate, mezcal, textiles, beach supplies, and a less polished but more local town stop.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/things-to-do/la-crucecita-market/'>Use the market guide</a></div>
        <div class='card p-6'><h3>Bay palapas — lunch, not your only food plan</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Maguey, Santa Cruz, San Agustín, and Chahué are better for daytime grilled fish, shrimp, ceviche, shade, and cold drinks than for a special dinner.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/destinations/el-maguey/'>Compare beach lunch bays</a></div>
      </div>
    </section>

    <section class='mt-10 grid gap-6 lg:grid-cols-3'>
      <div class='card p-6'><h3>Breakfast strategy</h3><p class='mt-2 text-sm leading-6 text-ink/70'>If you are staying in Tangolunda, breakfast at the hotel can save friction. If you are staying near town, make La Crucecita your morning base and buy beach snacks before taxis or boat departures.</p></div>
      <div class='card p-6'><h3>Lunch strategy</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Eat where you are swimming. Moving from a bay back to town just for lunch usually wastes the best water hours. Confirm cash/card before ordering at small palapas.</p></div>
      <div class='card p-6'><h3>Dinner strategy</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Return to La Crucecita or your hotel zone before dark, especially if you spent the day at San Agustín, Cacaluta, Chachacual, or another less-serviced beach.</p></div>
    </section>

    <section class='mt-10 rounded-[2rem] border border-border bg-white p-7' data-visible-sources='true'>
      <h2 class='text-2xl'>Current details to verify</h2>
      <ul class='mt-4 list-disc space-y-3 pl-5 text-sm leading-7 text-ink/70'>
        <li>Restaurant hours, reservation needs, and holiday closures before taking a taxi across town.</li>
        <li>Whether beach palapas accept cards, have fresh fish available, or close early after slow days.</li>
        <li>Recent reviews for service consistency; use official pages first, then recent maps/review signals.</li>
      </ul>
    </section>
  </div>
</section>
""",
    'tours/index.html': """
<section class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='tours'>
  <div class='container-xl max-w-6xl'>
    <div class='grid gap-6 lg:grid-cols-[1fr_1fr]'>
      <article class='card p-7 sm:p-8'>
        <p class='eyebrow'>Quick verdict</p>
        <h2 class='mt-2 text-3xl'>Pick tours by route and operator fit, not by the cheapest headline price.</h2>
        <p class='mt-4 leading-8 text-ink/75'>Most Huatulco visitors should do one bay boat day from Santa Cruz. The upgrade is not always a bigger boat; it is a clearer route, smaller group, better snorkeling timing, honest park-fee/inclusion details, and a guide who knows when water or wind makes a bay less worthwhile.</p>
      </article>
      <aside class='card p-7 sm:p-8'>
        <p class='eyebrow'>Booking filter</p>
        <h2 class='mt-2 text-2xl'>Ask these five questions.</h2>
        <ol class='mt-4 list-decimal space-y-3 pl-5 text-sm leading-7 text-ink/70'>
          <li>Which bays are actually included, and can the route change for conditions?</li>
          <li>Is snorkel gear included, rented separately, or expected to be brought?</li>
          <li>What happens if wind, swell, or visibility is poor?</li>
          <li>Are food, drinks, towels, shade, dock fees, and park fees included?</li>
          <li>Where exactly do we meet: Santa Cruz pier, Chahué Marina, hotel lobby, or office?</li>
        </ol>
      </aside>
    </div>

    <section class='mt-10' data-named-entity-directory='huatulco-tour-operators'>
      <p class='eyebrow'>Operators and booking channels to compare</p>
      <h2 class='mt-2 text-3xl'>Use named options as a comparison set</h2>
      <div class='mt-5 overflow-hidden rounded-[1.5rem] border border-border bg-white' data-tour-comparison-matrix='true'>
        <div class='grid gap-px bg-border text-sm md:grid-cols-4'>
          <div class='bg-secondary p-4 font-bold'>If your priority is…</div><div class='bg-secondary p-4 font-bold'>Start by comparing</div><div class='bg-secondary p-4 font-bold'>Likely format</div><div class='bg-secondary p-4 font-bold'>Verify before booking</div>
          <div class='bg-white p-4'>Classic first-trip bay day</div><div class='bg-white p-4'>Tours en Huatulco or a similar Santa Cruz operator</div><div class='bg-white p-4'>Shared panga / multi-bay route</div><div class='bg-white p-4'>Exact bays, lunch stop, snorkel gear, park fees</div>
          <div class='bg-white p-4'>Wildlife and reef interpretation</div><div class='bg-white p-4'>Oceanico Huatulco</div><div class='bg-white p-4'>Small-group naturalist boat</div><div class='bg-white p-4'>Seasonality, wildlife caveats, snorkeling conditions</div>
          <div class='bg-white p-4'>Control, kids, or mobility needs</div><div class='bg-white p-4'>Huatulco Watersports, Pilo Vázquez, private boats</div><div class='bg-white p-4'>Private/custom charter</div><div class='bg-white p-4'>Boat shade, ladder, bathroom, return flexibility</div>
          <div class='bg-white p-4'>Hotel convenience</div><div class='bg-white p-4'>Amstar or your hotel desk</div><div class='bg-white p-4'>Booked excursion/channel</div><div class='bg-white p-4'>Actual operator, pickup time, cancellation rules</div>
        </div>
      </div>
      <p class='mt-4 text-xs font-semibold uppercase tracking-[.18em] text-ink/45'>Operator examples checked May 2026; always verify current route, inclusions, fees, and weather/sea conditions directly.</p>
      <div class='mt-6 grid gap-5 md:grid-cols-2'>
        <div class='card p-6'><p class='mb-3 text-xs font-bold uppercase tracking-[.16em] text-primary'>Direct operator / small group</p><h3>Oceanico Huatulco — marine focus</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Best fit if your priority is wildlife, reef education, smaller groups, naturalist guidance, or seasonal whale/dolphin context. Verify seasonality and sighting caveats directly.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://oceanico.org/'>Visit Oceanico site</a></div>
        <div class='card p-6'><p class='mb-3 text-xs font-bold uppercase tracking-[.16em] text-primary'>Direct operator / private</p><h3>Huatulco Watersports — private boats and jet skis</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Good comparison point for private charters, jet ski tours, family groups, and customized bay days when you want more control than a shared panga.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.huatulcowatersports.com/'>Visit Huatulco Watersports</a></div>
        <div class='card p-6'><p class='mb-3 text-xs font-bold uppercase tracking-[.16em] text-primary'>Shared tour baseline</p><h3>Tours en Huatulco — classic five-bay boat tour</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Useful baseline for a traditional Santa Cruz departure, multi-bay route, swimming stops, and easy all-ages structure.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.toursenhuatulco.com/en/itinerary-5-bays-boat.html'>See 5-bay tour reference</a></div>
        <div class='card p-6'><p class='mb-3 text-xs font-bold uppercase tracking-[.16em] text-primary'>Local guide / private-style</p><h3>Pilo Vázquez — local guide planning</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Worth checking if you prefer a locally guided private or semi-private day where the route can be explained rather than simply sold as a package.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://pilovazquez.com/huatulco-bay-tours.php'>Visit Pilo Vázquez site</a></div>
        <div class='card p-6'><p class='mb-3 text-xs font-bold uppercase tracking-[.16em] text-primary'>Larger boat / listing</p><h3>Marinautica Huatulco — catamaran-style option</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Compare for larger-boat comfort, catamaran atmosphere, and group-friendly bay experiences. Confirm group size, music/noise level, and swim-stop timing.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.tripadvisor.com/Attraction_Review-g12517534-d26500570-Reviews-Marinautica_Huatulco-Santa_Cruz_Huatulco_Huatulco_Southern_Mexico.html'>View Marinautica listing</a></div>
        <div class='card p-6'><p class='mb-3 text-xs font-bold uppercase tracking-[.16em] text-primary'>Booking channel / hotel desk</p><h3>Amstar / hotel desks — easy but compare carefully</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Hotel desks are convenient for pickup and support. They may not be the cheapest or most flexible. Compare inclusions and actual operator details before booking.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.amstardmc.com/en/excursions/sea-and-sun-bays/'>Compare Amstar example</a></div>
      </div>
    </section>

    <section class='mt-10 grid gap-6 lg:grid-cols-3'>
      <div class='card p-6'><h3>Choose shared boat</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Best for first-timers, budget control, easy logistics, and seeing multiple bays without designing the day yourself.</p></div>
      <div class='card p-6'><h3>Choose private boat</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Best for families, photographers, serious snorkelers, mobility needs, or anyone who wants to leave early and avoid crowded swim stops.</p></div>
      <div class='card p-6'><h3>Skip the boat day</h3><p class='mt-2 text-sm leading-6 text-ink/70'>If anyone is seasick, heat-sensitive, or uninterested in snorkeling, build a land day around La Crucecita, Copalita, Chahué, and a resort pool instead.</p></div>
    </section>

    <section class='mt-10 rounded-[2rem] border border-border bg-white p-7' data-visible-sources='true'>
      <h2 class='text-2xl'>Current details to verify</h2>
      <p class='mt-3 text-sm leading-7 text-ink/70'>Confirm route, inclusions, conservation/park fees, cancellation policy, exact meeting point, group size, and whether wildlife sightings or snorkeling visibility are presented as possibilities rather than guarantees.</p>
    </section>
  </div>
</section>
""",
    'things-to-do/snorkeling/index.html': """
<section class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='snorkeling'>
  <div class='container-xl max-w-6xl'>
    <article class='card p-7 sm:p-8'>
      <p class='eyebrow'>Quick verdict</p>
      <h2 class='mt-2 text-3xl'>Snorkeling is condition-dependent. Choose the bay and the morning, not just the brochure.</h2>
      <p class='mt-4 leading-8 text-ink/75'>Huatulco can be excellent for casual snorkeling, but visibility changes with swell, wind, recent rain, boat traffic, and the exact rocky edge you use. Maguey and San Agustín are easiest for food and beach time. Chachacual and Cacaluta feel wilder and usually need a boat. La Entrega is popular because it is easy, not because it is always quiet.</p>
    </article>

    <section class='mt-8 grid gap-5 md:grid-cols-2 lg:grid-cols-4' data-named-snorkel-spots='true'>
      <div class='card p-6'><h3>Maguey / La Entrega</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Most practical for first-timers who want restaurants, shade, and easier access. Expect more people and boat activity.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/destinations/el-maguey/'>Use Maguey guide</a></div>
      <div class='card p-6'><h3>San Agustín</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Best blend of coral, beach restaurants, and a longer beach day if you accept the rougher road or boat approach.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/destinations/san-agustin/'>Use San Agustín guide</a></div>
      <div class='card p-6'><h3>Chachacual</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Better for boat-day travelers who want a quieter protected bay and can be flexible if visibility is off.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/destinations/chachacual/'>Use Chachacual guide</a></div>
      <div class='card p-6'><h3>Cacaluta</h3><p class='mt-2 text-sm leading-6 text-ink/70'>More about wild scenery and national-park feeling than guaranteed easy snorkeling. Plan water, shade, and return logistics.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/destinations/cacaluta/'>Use Cacaluta guide</a></div>
    </section>

    <section class='mt-10 grid gap-6 lg:grid-cols-3'>
      <div class='card p-6'><h3>Best setup</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Go in the morning, ask about current visibility before paying, wear a rash guard, use reef-safe sun protection practices, and keep fins under control near coral.</p></div>
      <div class='card p-6'><h3>Who should book a guide</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Book guided if you have kids, nervous swimmers, poor swimmers, prescription-mask needs, or want someone watching boat traffic and entry points.</p></div>
      <div class='card p-6'><h3>Common mistake</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Assuming every bay has reef right off the sand. The useful snorkel zone is often a rocky edge, point, or specific stop your captain should explain.</p></div>
    </section>

    <section class='mt-10 rounded-[2rem] border border-border bg-white p-7' data-visible-sources='true'>
      <h2 class='text-2xl'>Good operators to compare for snorkel-first days</h2>
      <p class='mt-3 text-sm leading-7 text-ink/70'>For guided snorkel days, compare <a class='font-bold text-primary' href='https://oceanico.org/'>Oceanico Huatulco</a> for small-group marine interpretation, <a class='font-bold text-primary' href='https://www.huatulcowatersports.com/'>Huatulco Watersports</a> for private/custom boat days, and a classic Santa Cruz five-bay operator such as <a class='font-bold text-primary' href='https://www.toursenhuatulco.com/en/itinerary-5-bays-boat.html'>Tours en Huatulco</a>. Ask all of them what is realistic this week.</p>
    </section>
  </div>
</section>
""",
    'things-to-do/boat-tours/index.html': """
<section class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='boat-tours'>
  <div class='container-xl max-w-6xl'>
    <article class='card p-7 sm:p-8'>
      <p class='eyebrow'>Quick verdict</p>
      <h2 class='mt-2 text-3xl'>A bay boat tour is worth doing once, but only if the route matches your group.</h2>
      <p class='mt-4 leading-8 text-ink/75'>The classic tour leaves from Santa Cruz, strings together several bays, pauses for swimming or snorkeling, and usually ends with a lunch stop or return to town. The best version is not the one with the longest bay count; it is the one that leaves early, avoids rushed swim stops, and has a clear plan for shade, seasickness, kids, and food.</p>
    </article>

    <section class='mt-8 grid gap-5 md:grid-cols-2 lg:grid-cols-4'>
      <div class='card p-6'><h3>Start at Santa Cruz</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Most shared bay tours and pangas use Santa Cruz pier/marina. Build extra time for parking, bathrooms, cash, and finding the right captain or desk.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/destinations/santa-cruz/'>Use Santa Cruz guide</a></div>
      <div class='card p-6'><h3>Snorkel stop</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Ask where the snorkel stop will be today, not only what the brochure says. Visibility and safety can change by morning.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/things-to-do/snorkeling/'>Use snorkel guide</a></div>
      <div class='card p-6'><h3>Lunch stop</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Maguey, San Agustín, and Santa Cruz are the simplest lunch bays. Confirm whether lunch is included or just a restaurant stop.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/food-culture/'>Plan food</a></div>
      <div class='card p-6'><h3>Protected bays</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Cacaluta, Chachacual, and Órgano feel more natural. Treat them gently, pack water, and follow national-park guidance.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/destinations/cacaluta/'>Compare wild bays</a></div>
    </section>

    <section class='mt-10' data-named-entity-directory='huatulco-boat-tour-operators'>
      <p class='eyebrow'>Operator fit</p>
      <h2 class='mt-2 text-3xl'>Three different ways to book the same coastline</h2>
      <div class='mt-6 grid gap-5 md:grid-cols-3'>
        <div class='card p-6'><h3>Classic shared panga</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Use Tours en Huatulco or similar Santa Cruz operators as your baseline: 5-bay style route, easy difficulty, all-ages structure, and clear inclusions.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.toursenhuatulco.com/en/itinerary-5-bays-boat.html'>Check baseline tour</a></div>
        <div class='card p-6'><h3>Small-group nature boat</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Use Oceanico if wildlife, marine interpretation, smaller groups, and responsible observation matter more than beach-party energy.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://oceanico.org/'>Check Oceanico</a></div>
        <div class='card p-6'><h3>Private/custom boat</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Use Huatulco Watersports, Pilo Vázquez, or another private operator if your group wants a custom route, longer swim time, or a more controlled family day.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.huatulcowatersports.com/'>Check private options</a></div>
      </div>
    </section>

    <section class='mt-10 rounded-[2rem] border border-border bg-white p-7' data-visible-sources='true'>
      <h2 class='text-2xl'>Current details to verify</h2>
      <p class='mt-3 text-sm leading-7 text-ink/70'>Before paying, confirm the exact meeting point, final route, food/drink plan, snorkeling gear, park/conservation fees, cancellation policy, shade, bathroom situation, and whether your group can skip a stop if conditions are not good.</p>
    </section>
  </div>
</section>
""",
    'things-to-do/copalita-archaeology/index.html': """
<section class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='copalita'>
  <div class='container-xl max-w-6xl'>
    <article class='card p-7 sm:p-8'>
      <p class='eyebrow'>Quick verdict</p>
      <h2 class='mt-2 text-3xl'>Copalita is the best half-day culture break from the bays.</h2>
      <p class='mt-4 leading-8 text-ink/75'>Bocana del Río Copalita is not a giant ruins complex. Its value is the mix: coastal cliffs, river-mouth landscape, museum/context, trails, and archaeological remains close enough to Huatulco that you can pair it with La Bocana, Tangolunda, or a quiet dinner instead of losing a whole vacation day.</p>
    </article>

    <section class='mt-8 grid gap-5 md:grid-cols-2 lg:grid-cols-4'>
      <div class='card p-6'><h3>What you are seeing</h3><p class='mt-2 text-sm leading-6 text-ink/70'>INAH describes the site as a ceremonial center near the cliffs and Copalita River mouth, with civic-ceremonial buildings, residential terraces, temples, and a ballcourt.</p></div>
      <div class='card p-6'><h3>Best fit</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Travelers who want history, viewpoint walking, nature context, and a break from resort/beach rhythm without a long transfer.</p></div>
      <div class='card p-6'><h3>Pair with</h3><p class='mt-2 text-sm leading-6 text-ink/70'>La Bocana beach, Casa Bocana restaurant, Tangolunda, or a late afternoon return to La Crucecita.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='https://www.casabocana.mx/en-gb/restaurante'>Check Casa Bocana</a></div>
      <div class='card p-6'><h3>Avoid if</h3><p class='mt-2 text-sm leading-6 text-ink/70'>You want large pyramids, a full-day archaeology deep dive, or a stroller-friendly/shade-heavy attraction in midday heat.</p></div>
    </section>

    <section class='mt-10 grid gap-6 lg:grid-cols-3'>
      <div class='card p-6'><h3>How to plan it</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Go early, carry water, wear walking shoes, and treat opening status as something to confirm before you hire transport.</p></div>
      <div class='card p-6'><h3>Guide decision</h3><p class='mt-2 text-sm leading-6 text-ink/70'>A guide is worthwhile if you want the site to mean more than stones and viewpoints. Otherwise, pair a shorter visit with La Bocana/Copalita coast time.</p></div>
      <div class='card p-6'><h3>Transport logic</h3><p class='mt-2 text-sm leading-6 text-ink/70'>This is simplest by taxi/private driver or a tour that explicitly includes Copalita. Confirm wait time or pickup time so you are not stranded at the exit.</p></div>
    </section>

    <section class='mt-10 rounded-[2rem] border border-border bg-white p-7' data-visible-sources='true'>
      <h2 class='text-2xl'>Current details to verify</h2>
      <p class='mt-3 text-sm leading-7 text-ink/70'>Use the official INAH listing for background and current access context before you go: <a class='font-bold text-primary' href='https://lugares.inah.gob.mx/en/node/4487'>Bocana del Río Copalita — INAH</a>. Recent visitor reports have sometimes mentioned access limitations, so verify opening status directly before building a day around it.</p>
    </section>
  </div>
</section>
""",
    'things-to-do/la-crucecita-market/index.html': """
<section class='section-pad' data-priority-guide-depth='visitor-reference' data-entity-depth='la-crucecita-market'>
  <div class='container-xl max-w-6xl'>
    <article class='card p-7 sm:p-8'>
      <p class='eyebrow'>Quick verdict</p>
      <h2 class='mt-2 text-3xl'>Use La Crucecita market as a practical town stop, not a polished attraction.</h2>
      <p class='mt-4 leading-8 text-ink/75'>Mercado 3 de Mayo and the surrounding La Crucecita blocks are useful for breakfast, fruit, coffee, chocolate, mezcal, beach supplies, souvenirs, and a normal-town reset between resort days. It works best in the morning or early evening, paired with the plaza and church rather than treated as a standalone half-day.</p>
    </article>

    <section class='mt-8 grid gap-5 md:grid-cols-2 lg:grid-cols-4'>
      <div class='card p-6'><h3>Start at the plaza</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Use the central square and Iglesia de La Crucecita as your orientation point, then walk the nearby market and restaurant blocks.</p></div>
      <div class='card p-6'><h3>What to buy</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Fruit, snacks, coffee, chocolate, mezcal, beach shirts, hats, basic supplies, and low-stakes souvenirs.</p></div>
      <div class='card p-6'><h3>When to go</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Morning for breakfast and errands; early evening for plaza life before dinner. Midday can feel hot and less rewarding.</p></div>
      <div class='card p-6'><h3>Pair with dinner</h3><p class='mt-2 text-sm leading-6 text-ink/70'>After the market, check Terra-Cotta, El Sabor de Oaxaca, Mercader, La Chicatana, or another town restaurant that fits your group.</p><a class='mt-4 inline-flex text-sm font-bold text-primary' href='/food-culture/'>Use food guide</a></div>
    </section>

    <section class='mt-10 grid gap-6 lg:grid-cols-3'>
      <div class='card p-6'><h3>Cash and bargaining</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Carry pesos in small bills. Bargain respectfully on souvenirs if it feels expected, but do not haggle hard over food or small everyday purchases.</p></div>
      <div class='card p-6'><h3>Family use</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Good for a short, shaded break from resort rhythm. Keep expectations realistic: narrow aisles, heat, uneven sidewalks, and limited stroller comfort.</p></div>
      <div class='card p-6'><h3>Common mistake</h3><p class='mt-2 text-sm leading-6 text-ink/70'>Going only for souvenirs. The better use is practical: supplies before a beach day, breakfast before a boat tour, or a low-key town evening before dinner.</p></div>
    </section>

    <section class='mt-10 rounded-[2rem] border border-border bg-white p-7' data-visible-sources='true'>
      <h2 class='text-2xl'>Current details to verify</h2>
      <p class='mt-3 text-sm leading-7 text-ink/70'>Check current maps/reviews for Mercado 3 de Mayo and any restaurant you plan to use afterward. Market stalls and restaurant hours can shift around holidays, low season, and family closures.</p>
    </section>
  </div>
</section>
""",
}


def replace_last_section(path: Path, new_section: str) -> None:
    txt = path.read_text(encoding='utf-8')
    end = txt.index('\n</main>')
    # Replace the last public content section before </main>. This preserves any approved media section above it.
    start = txt.rfind("<section class='section-pad'", 0, end)
    if start == -1:
        raise RuntimeError(f'No section-pad block found in {path}')
    updated = txt[:start] + new_section.strip() + txt[end:]
    path.write_text(updated, encoding='utf-8')

for rel, section in PAGES.items():
    replace_last_section(ROOT / rel, section)

print(f'Updated {len(PAGES)} entity-depth pages')
