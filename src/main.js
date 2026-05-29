import './input.css';
import { destinations } from './data/destinations.js';
import { guideCards } from './data/guide-cards.js';
import { itineraries } from './data/itineraries.js';
import { thingsToDo } from './data/things-to-do.js';
import { destinationCard, faqItem, guideCard, itineraryCard, thingCard } from './components/cards.js';

function renderList(selector, items, renderer) {
  const target = document.querySelector(selector);
  if (!target) return;
  target.innerHTML = items.map(renderer).join('');
}

function setupMobileMenu() {
  const button = document.querySelector('[data-mobile-menu-button]');
  const menu = document.querySelector('[data-mobile-menu]');
  if (!button || !menu) return;

  const iconUse = button.querySelector('[data-menu-icon] use');

  function setOpen(isOpen) {
    button.setAttribute('aria-expanded', String(isOpen));
    button.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
    menu.classList.toggle('hidden', !isOpen);
    iconUse?.setAttribute('href', `/icons.svg#${isOpen ? 'xmark' : 'bars'}`);
  }

  button.addEventListener('click', () => {
    const isOpen = button.getAttribute('aria-expanded') === 'true';
    setOpen(!isOpen);
  });

  menu.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => setOpen(false));
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') setOpen(false);
  });
}

function searchEntryText(entry) {
  return [
    entry.title,
    entry.name,
    entry.kicker,
    entry.label,
    entry.duration,
    entry.region,
    entry.summary,
    ...(entry.bestFor || []),
    ...(entry.highlights || []),
  ].filter(Boolean).join(' ').toLowerCase();
}

function escapeHtml(value) {
  const node = document.createElement('div');
  node.textContent = value;
  return node.innerHTML;
}

function setupSiteSearch() {
  const form = document.querySelector('[data-site-search]');
  const input = document.querySelector('[data-site-search-input]');
  const results = document.querySelector('[data-site-search-results]');
  if (!form || !input || !results) return;

  const entries = [
    ...destinations.map((entry) => ({ ...entry, type: 'Destination', title: entry.name })),
    ...itineraries.map((entry) => ({ ...entry, type: 'Itinerary' })),
    ...guideCards.map((entry) => ({ ...entry, type: entry.kicker || 'Guide' })),
    ...thingsToDo.map((entry) => ({ ...entry, type: entry.label || 'Things to do' })),
  ];

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const query = input.value.trim().toLowerCase();

    results.classList.remove('hidden');
    if (!query) {
      results.innerHTML = '<p class="font-bold text-ink">Type a bay, activity, or trip length to search.</p><p class="mt-1">Try snorkeling, boat tour, Tangolunda, safety, or 5 days.</p>';
      input.focus();
      return;
    }

    const matches = entries
      .filter((entry) => searchEntryText(entry).includes(query))
      .slice(0, 5);

    if (!matches.length) {
      results.innerHTML = `<p class="font-bold text-ink">No guide found for “${escapeHtml(query)}”.</p><p class="mt-1">Try a broader term such as beach, volcano, food, safety, or itinerary.</p>`;
      return;
    }

    results.innerHTML = `
      <p class="font-bold text-ink">Best matches</p>
      <div class="mt-3 grid gap-2">
        ${matches.map((entry) => `
          <a href="${escapeHtml(entry.href)}" class="block rounded-xl bg-white px-4 py-3 font-bold text-primary hover:bg-secondary">
            ${escapeHtml(entry.title)}
            <span class="block text-xs font-semibold text-ink/55">${escapeHtml(entry.type)}</span>
          </a>`).join('')}
      </div>
    `;
  });
}

function setupFaqs() {
  document.querySelectorAll('[data-faq-button]').forEach((button) => {
    button.addEventListener('click', () => {
      const answer = button.parentElement?.querySelector('[data-faq-answer]');
      const isOpen = button.getAttribute('aria-expanded') === 'true';
      button.setAttribute('aria-expanded', String(!isOpen));
      answer?.classList.toggle('hidden', isOpen);
      button.querySelector('[aria-hidden="true"]').textContent = isOpen ? '+' : '−';
    });
  });

  document.querySelectorAll('[data-standard-faq]').forEach((section) => {
    section.querySelectorAll('details').forEach((item) => {
      item.addEventListener('toggle', () => {
        if (!item.open) return;
        section.querySelectorAll('details[open]').forEach((openItem) => {
          if (openItem !== item) openItem.removeAttribute('open');
        });
      });
    });
  });
}

function setupDestinationFilters() {
  const buttons = document.querySelectorAll('[data-filter]');
  if (!buttons.length) return;

  const activeClasses = ['border-primary', 'bg-primary', 'text-white'];
  const inactiveClasses = ['border-border', 'text-ink', 'hover:border-primary'];

  function setActiveButton(activeButton) {
    buttons.forEach((item) => {
      const isActive = item === activeButton;
      item.setAttribute('aria-pressed', String(isActive));
      item.classList.toggle('border-primary', isActive);
      item.classList.toggle('bg-primary', isActive);
      item.classList.toggle('text-white', isActive);
      inactiveClasses.forEach((className) => item.classList.toggle(className, !isActive));
      activeClasses.forEach((className) => item.classList.toggle(className, isActive));
    });
  }

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      const filter = button.dataset.filter;
      setActiveButton(button);
      const filtered = filter === 'all'
        ? destinations
        : destinations.filter((destination) => destination.bestFor.some((tag) => tag.toLowerCase().includes(filter)) || destination.region.toLowerCase().includes(filter));
      renderList('[data-destination-grid]', filtered, destinationCard);
    });
  });
}

renderList('[data-destination-grid]', destinations, destinationCard);
renderList('[data-itinerary-grid]', itineraries, itineraryCard);
renderList('[data-guide-grid]', guideCards, guideCard);
renderList('[data-things-grid]', thingsToDo, thingCard);
renderList('[data-faq-list]', [
  { question: 'Is Huatulco only for resort travelers?', answer: 'No. Tangolunda is the easiest resort bay, but the wider destination includes town beaches, boat-access national-park bays, La Crucecita, Copalita, seafood palapas, and west-coast day trips.' },
  { question: 'Do I need a car in Huatulco?', answer: 'Not for the central bays. Taxis and boats work for most first trips. A car or driver becomes more useful for Copalita, San Agustín, Mazunte, Puerto Ángel, or a flexible coast day.' },
  { question: 'Which bay should I choose first?', answer: 'Use Tangolunda for easy resort comfort, Santa Cruz for boat logistics, Chahué for a public town beach, El Maguey for seafood and calm-water potential, and the national-park bays for a more natural boat day.' },
], faqItem);

setupMobileMenu();
setupSiteSearch();
setupDestinationFilters();
setupFaqs();
