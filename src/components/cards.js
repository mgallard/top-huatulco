const escapeMap = {
  '&': '&amp;',
  '<': '&lt;',
  '>': '&gt;',
  '"': '&quot;',
  "'": '&#039;',
};

export function escapeHtml(value = '') {
  return String(value).replace(/[&<>"']/g, (char) => escapeMap[char]);
}

function badgeList(items = [], className = 'bg-secondary text-ink') {
  return items.map((item) => `<span class="rounded-full px-3.5 py-1.5 text-[0.78rem] font-bold leading-none ring-1 ring-primary/10 ${className}">${escapeHtml(item)}</span>`).join('');
}

export function destinationCard(destination) {
  return `
    <article class="card group flex h-full flex-col hover:-translate-y-1 hover:border-primary/35 hover:shadow-card">
      <a href="${escapeHtml(destination.href)}" class="relative block h-48 overflow-hidden bg-gradient-to-br from-secondary via-white to-sand sm:h-52" aria-label="Read the ${escapeHtml(destination.name)} guide">
        <img src="${escapeHtml(destination.image)}" alt="${escapeHtml(destination.imageAlt)}" class="h-full w-full object-cover transition duration-700 group-hover:scale-105" loading="eager" decoding="async" width="640" height="420">
        <span class="absolute left-4 top-4 rounded-full bg-white/95 px-3 py-1 text-xs font-bold text-ink shadow-sm backdrop-blur">${escapeHtml(destination.region)}</span>
      </a>
      <div class="flex flex-1 flex-col p-6">
        <h3 class="text-2xl"><a class="hover:text-primary" href="${escapeHtml(destination.href)}">${escapeHtml(destination.name)}</a></h3>
        <p class="mt-3 flex-1 text-sm leading-6 text-ink/75">${escapeHtml(destination.summary)}</p>
        <div class="mt-5 flex flex-wrap gap-2">${badgeList(destination.bestFor)}</div>
        <a href="${escapeHtml(destination.href)}" class="mt-6 inline-flex items-center text-sm font-bold text-primary hover:text-coral">Open guide →</a>
      </div>
    </article>`;
}

export function itineraryCard(itinerary) {
  return `
    <article class="flex h-full flex-col rounded-3xl border border-border bg-white p-6 shadow-card transition duration-300 hover:-translate-y-1 hover:border-primary/60">
      <p class="self-start rounded-full bg-primary/10 px-3 py-1 text-xs font-bold uppercase tracking-[0.18em] text-primary">${escapeHtml(itinerary.duration)}</p>
      <h3 class="mt-4 text-2xl"><a href="${escapeHtml(itinerary.href)}" class="hover:text-primary">${escapeHtml(itinerary.title)}</a></h3>
      <p class="mt-3 flex-1 text-sm leading-6 text-ink/75">${escapeHtml(itinerary.summary)}</p>
      <div class="mt-5 flex flex-wrap gap-2">${badgeList(itinerary.highlights)}</div>
      <a href="${escapeHtml(itinerary.href)}" class="mt-6 inline-flex items-center self-start rounded-full bg-primary/10 px-4 py-2 text-sm font-bold text-primary hover:bg-primary hover:text-white">View itinerary →</a>
    </article>`;
}

export function guideCard(card) {
  return `
    <a href="${escapeHtml(card.href)}" class="rounded-3xl border border-border bg-white p-6 shadow-card transition duration-300 hover:-translate-y-1 hover:border-primary/60">
      <span class="text-xs font-bold uppercase tracking-[0.18em] text-coral">${escapeHtml(card.kicker)}</span>
      <h3 class="mt-4 text-xl">${escapeHtml(card.title)}</h3>
      <p class="mt-3 text-sm leading-6 text-ink/75">${escapeHtml(card.summary)}</p>
      <span class="mt-5 inline-flex text-sm font-bold text-primary">Read guide →</span>
    </a>`;
}

export function thingCard(item) {
  return `
    <a href="${escapeHtml(item.href)}" class="relative overflow-hidden rounded-3xl bg-gradient-to-br from-primary to-[#256B86] p-6 text-white shadow-card transition duration-300 hover:-translate-y-1">
      <span class="absolute -right-8 -top-8 h-32 w-32 rounded-full bg-white/10 blur-2xl"></span>
      <span class="relative inline-flex rounded-full bg-white/15 px-3 py-1 text-xs font-bold text-white backdrop-blur">${escapeHtml(item.label)}</span>
      <h3 class="relative mt-5 text-xl text-white">${escapeHtml(item.title)}</h3>
      <p class="relative mt-3 text-sm leading-6 text-white/85">${escapeHtml(item.summary)}</p>
    </a>`;
}

export function faqItem({ question, answer }) {
  return `
    <div class="border-b border-white/15 py-4" data-faq-item>
      <button class="flex w-full items-center justify-between gap-4 text-left font-bold text-white" aria-expanded="false" data-faq-button>
        <span>${escapeHtml(question)}</span><span aria-hidden="true">+</span>
      </button>
      <p class="mt-3 hidden text-sm leading-6 text-white/75" data-faq-answer>${escapeHtml(answer)}</p>
    </div>`;
}
