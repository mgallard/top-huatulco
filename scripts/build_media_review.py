#!/usr/bin/env python3
from __future__ import annotations

import html
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "src/data/visual-candidates.json"
OUT = ROOT / "media-review/index.html"


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def candidate_id(index: int, item: dict) -> str:
    preview = item.get("localPreview") or item.get("originalUrl") or item.get("landingPage") or item.get("title") or str(index)
    return f"candidate-{index + 1:03d}-{preview.rsplit('/', 1)[-1].replace('.', '-').replace('_', '-')}"


def main() -> None:
    data = json.loads(CANDIDATES.read_text()) if CANDIDATES.exists() else []
    by_route = defaultdict(list)
    for index, item in enumerate(data):
        item["_reviewId"] = candidate_id(index, item)
        by_route[item.get("route", "unassigned")].append(item)
    status_counts = Counter(item.get("reviewStatus", "unknown") for item in data)
    preview_count = sum(1 for item in data if item.get("localPreview"))
    sections = []
    for route in sorted(by_route):
        route_label = 'Homepage / root' if route == '/' else route
        cards = []
        for item in by_route[route]:
            img = item.get("localPreview") or item.get("imageUrl") or ""
            img_html = f"<img src='{esc(img)}' alt='{esc(item.get('draftAlt') or item.get('title'))}' loading='eager'>" if img else "<div class='missing'>No preview downloaded</div>"
            cards.append(f"""
<article class='candidate-card' data-review-card data-id='{esc(item.get('_reviewId'))}' data-route='{esc(item.get('route'))}' data-title='{esc(item.get('title'))}' data-provider='{esc(item.get('provider'))}' data-review-status='{esc(item.get('reviewStatus'))}'>
  <div class='thumb'>{img_html}</div>
  <div class='card-body'>
    <p class='badge'>{esc(item.get('provider'))} · {esc(item.get('license'))}</p>
    <h3>{esc(item.get('title'))}</h3>
    <p><strong>Target:</strong> {esc(item.get('targetTitle'))}</p>
    <p><strong>Creator:</strong> {esc(item.get('creator'))}</p>
    <p><strong>Use:</strong> commercial {esc(item.get('commercialUseAllowed'))}; derivatives {esc(item.get('derivativesAllowed'))}</p>
    <p><strong>Initial review:</strong> {esc(item.get('reviewStatus'))} — {esc(item.get('licenseReview'))}</p>
    <p class='notes'>{esc(item.get('notes'))}</p>
    <fieldset class='review-row' aria-label='Manual review choices for {esc(item.get('title'))}'>
      <legend>Decision</legend>
      <button type='button' data-choice='approved'>Approve</button>
      <button type='button' data-choice='maybe'>Maybe</button>
      <button type='button' data-choice='rejected'>Reject</button>
    </fieldset>
    <label class='note-label'>Review note
      <textarea data-note rows='3' aria-label='Optional note: place-match concerns, best page use, crop notes'></textarea>
    </label>
    <p class='saved-state' data-saved-state>Not reviewed yet</p>
    <div class='links'>
      <a href='{esc(item.get('landingPage'))}' target='_blank' rel='noopener'>Source page</a>
      <a href='{esc(item.get('originalUrl'))}' target='_blank' rel='noopener'>Original file</a>
    </div>
  </div>
</article>""")
        sections.append(f"<section><h2>{esc(route_label)} <span>{len(by_route[route])} candidates</span></h2><div class='grid'>{''.join(cards)}</div></section>")
    status_summary = ', '.join(f"{count} {status}" for status, count in sorted(status_counts.items()))
    candidates_json = json.dumps([
        {
            "id": item.get("_reviewId"),
            "route": item.get("route"),
            "title": item.get("title"),
            "targetTitle": item.get("targetTitle"),
            "landingPage": item.get("landingPage"),
            "originalUrl": item.get("originalUrl"),
            "localPreview": item.get("localPreview"),
            "provider": item.get("provider"),
            "license": item.get("license"),
            "creator": item.get("creator"),
        }
        for item in data
    ], ensure_ascii=False).replace("</", "<\\/")
    html_doc = f"""<!doctype html>
<html lang='en'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <meta name='robots' content='noindex,nofollow'>
  <meta name='description' content='Review-only board for Top Huatulco visual candidates, source metadata, licenses, and route targets.'>
  <link rel='canonical' href='https://tophuatulco.com/media-review/'>
  <title>Top Huatulco Media Review Board</title>
  <style>
    :root {{ color-scheme: light; --ink:#17313A; --muted:#5B727A; --line:#D9E9ED; --bg:#F5FBFC; --primary:#2C9AB7; --sand:#FFF7E8; --ok:#237A57; --maybe:#B27616; --bad:#B64242; }}
    body {{ margin:0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; color:var(--ink); background:var(--bg); }}
    header {{ padding:3rem clamp(1rem,4vw,4rem); background:linear-gradient(135deg,#E7F7F9,#FFF7E8); border-bottom:1px solid var(--line); }}
    main {{ padding:2rem clamp(1rem,4vw,4rem) 4rem; }}
    h1 {{ margin:0; font-size:clamp(2rem,5vw,4rem); line-height:.95; letter-spacing:-.04em; }}
    h2 {{ margin:3rem 0 1rem; font-size:1.35rem; }}
    h2 span {{ color:var(--muted); font-size:.9rem; font-weight:600; }}
    p {{ line-height:1.55; }}
    button, textarea {{ font:inherit; }}
    .summary {{ display:grid; gap:1rem; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); margin-top:1.5rem; max-width:900px; }}
    .summary div {{ background:white; border:1px solid var(--line); border-radius:1.25rem; padding:1rem; box-shadow:0 12px 30px rgba(23,49,58,.06); }}
    .summary strong {{ display:block; font-size:1.7rem; }}
    .toolbar {{ display:flex; flex-wrap:wrap; gap:.75rem; align-items:center; margin-top:1.25rem; }}
    .toolbar button {{ border:0; border-radius:999px; padding:.75rem 1rem; background:var(--ink); color:white; font-weight:900; cursor:pointer; }}
    .toolbar button.secondary {{ background:white; color:var(--ink); border:1px solid var(--line); }}
    .toolbar output {{ font-weight:800; color:var(--muted); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(270px,1fr)); gap:1rem; }}
    .candidate-card {{ background:white; border:2px solid var(--line); border-radius:1.25rem; overflow:hidden; box-shadow:0 12px 30px rgba(23,49,58,.06); display:flex; flex-direction:column; }}
    .candidate-card[data-decision='approved'] {{ border-color:var(--ok); box-shadow:0 14px 34px rgba(35,122,87,.16); }}
    .candidate-card[data-decision='maybe'] {{ border-color:var(--maybe); box-shadow:0 14px 34px rgba(178,118,22,.16); }}
    .candidate-card[data-decision='rejected'] {{ border-color:var(--bad); opacity:.72; }}
    .thumb {{ aspect-ratio:4/3; background:#d9e9ed; display:grid; place-items:center; color:var(--muted); }}
    .thumb img {{ width:100%; height:100%; object-fit:cover; display:block; }}
    .card-body {{ padding:1rem; display:grid; gap:.45rem; }}
    .card-body p, .card-body h3 {{ margin:0; }}
    .card-body h3 {{ font-size:1rem; line-height:1.25; }}
    .badge {{ color:var(--primary); text-transform:uppercase; letter-spacing:.09em; font-size:.72rem; font-weight:800; }}
    .notes {{ color:var(--muted); font-size:.88rem; }}
    .links {{ display:flex; flex-wrap:wrap; gap:.5rem; margin-top:.5rem; }}
    .review-row {{ display:flex; flex-wrap:wrap; gap:.45rem; margin:.35rem 0 0; padding:0; border:0; font-size:.82rem; font-weight:900; color:var(--ink); }}
    .review-row legend {{ width:100%; font-size:.72rem; color:var(--muted); text-transform:uppercase; letter-spacing:.08em; }}
    .review-row button {{ border:1px solid var(--line); border-radius:999px; padding:.5rem .7rem; background:#fff; cursor:pointer; font-weight:900; }}
    .review-row button[aria-pressed='true'] {{ color:white; }}
    .review-row button[data-choice='approved'][aria-pressed='true'] {{ background:var(--ok); border-color:var(--ok); }}
    .review-row button[data-choice='maybe'][aria-pressed='true'] {{ background:var(--maybe); border-color:var(--maybe); }}
    .review-row button[data-choice='rejected'][aria-pressed='true'] {{ background:var(--bad); border-color:var(--bad); }}
    .note-label {{ display:grid; gap:.25rem; color:var(--muted); font-size:.8rem; font-weight:800; }}
    textarea {{ width:100%; box-sizing:border-box; border:1px solid var(--line); border-radius:.85rem; padding:.6rem; color:var(--ink); resize:vertical; }}
    .saved-state {{ color:var(--muted); font-size:.82rem; font-weight:800; }}
    a {{ color:var(--primary); font-weight:800; }}
    .links a {{ border:1px solid var(--line); border-radius:999px; padding:.5rem .75rem; text-decoration:none; background:var(--sand); }}
    .warning {{ max-width:900px; padding:1rem; margin-top:1.5rem; border-radius:1rem; background:#fff; border:1px solid #f2c97d; }}
  </style>
</head>
<body>
<header>
  <p class='badge'>Review-only · noindex</p>
  <h1>Top Huatulco media candidates</h1>
  <p>This board is for selecting real, license-safe Huatulco visuals before wiring them into public pages. Your decisions are saved in this browser and can be exported as JSON for implementation.</p>
  <div class='summary'>
    <div><strong>{len(data)}</strong> candidates</div>
    <div><strong>{preview_count}</strong> local previews</div>
    <div><strong>{len(by_route)}</strong> routes covered</div>
    <div><strong>{esc(status_summary)}</strong> review status</div>
  </div>
  <div class='warning'><strong>Important:</strong> approve only after visual place-match and license review. Do not use images with uncertain subject, watermarks, people/privacy concerns, or source restrictions.</div>
  <div class='toolbar' aria-label='Review export tools'>
    <button type='button' id='exportReview'>Download review JSON</button>
    <button type='button' id='copyReview' class='secondary'>Copy review JSON</button>
    <button type='button' id='clearReview' class='secondary'>Clear local decisions</button>
    <output id='reviewSummary'>0 reviewed</output>
  </div>
</header>
<main>
{''.join(sections)}
</main>
<script id='candidateData' type='application/json'>{candidates_json}</script>
<script>
(() => {{
  const storageKey = 'top-huatulco-media-review-v1';
  const candidates = JSON.parse(document.getElementById('candidateData').textContent || '[]');
  const cards = Array.from(document.querySelectorAll('[data-review-card]'));
  const summary = document.getElementById('reviewSummary');

  const load = () => {{
    try {{ return JSON.parse(localStorage.getItem(storageKey) || '{{}}'); }}
    catch (error) {{ return {{}}; }}
  }};
  const save = (state) => localStorage.setItem(storageKey, JSON.stringify(state));
  let state = load();

  const setCardDecision = (card, decision, note) => {{
    const id = card.dataset.id;
    const text = card.querySelector('[data-saved-state]');
    const textarea = card.querySelector('[data-note]');
    if (typeof note === 'string') textarea.value = note;
    card.dataset.decision = decision || '';
    card.querySelectorAll('[data-choice]').forEach((button) => {{
      button.setAttribute('aria-pressed', button.dataset.choice === decision ? 'true' : 'false');
    }});
    text.textContent = decision ? `Saved: ${{decision}}` : 'Not reviewed yet';
    if (!decision && !textarea.value.trim()) delete state[id];
  }};

  const updateSummary = () => {{
    const values = Object.values(state);
    const counts = values.reduce((acc, item) => {{
      if (item.decision) acc[item.decision] = (acc[item.decision] || 0) + 1;
      return acc;
    }}, {{}});
    const reviewed = values.filter(item => item.decision || item.note).length;
    summary.textContent = `${{reviewed}} reviewed · ${{counts.approved || 0}} approved · ${{counts.maybe || 0}} maybe · ${{counts.rejected || 0}} rejected`;
  }};

  cards.forEach((card) => {{
    const id = card.dataset.id;
    const existing = state[id] || {{}};
    setCardDecision(card, existing.decision || '', existing.note || '');
    card.querySelectorAll('[data-choice]').forEach((button) => {{
      const choose = () => {{
        const next = button.dataset.choice;
        const note = card.querySelector('[data-note]').value.trim();
        if (next || note) state[id] = {{ ...(state[id] || {{}}), decision: next, note, updatedAt: new Date().toISOString() }};
        else delete state[id];
        save(state);
        setCardDecision(card, next, note);
        updateSummary();
      }};
      button.addEventListener('click', choose);
      button.addEventListener('pointerup', choose);
    }});
    card.querySelector('[data-note]').addEventListener('input', (event) => {{
      const note = event.target.value.trim();
      const decision = state[id]?.decision || '';
      if (decision || note) state[id] = {{ ...(state[id] || {{}}), decision, note, updatedAt: new Date().toISOString() }};
      else delete state[id];
      save(state);
      updateSummary();
    }});
  }});

  const exportPayload = () => {{
    const decisions = candidates.map((candidate) => ({{
      ...candidate,
      decision: state[candidate.id]?.decision || '',
      reviewNote: state[candidate.id]?.note || '',
      updatedAt: state[candidate.id]?.updatedAt || '',
    }}));
    return {{
      exportedAt: new Date().toISOString(),
      storageKey,
      totals: {{
        candidates: decisions.length,
        approved: decisions.filter(item => item.decision === 'approved').length,
        maybe: decisions.filter(item => item.decision === 'maybe').length,
        rejected: decisions.filter(item => item.decision === 'rejected').length,
        reviewed: decisions.filter(item => item.decision || item.reviewNote).length,
      }},
      decisions,
    }};
  }};

  document.getElementById('exportReview').addEventListener('click', () => {{
    const blob = new Blob([JSON.stringify(exportPayload(), null, 2)], {{ type: 'application/json' }});
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `top-huatulco-media-review-${{new Date().toISOString().slice(0, 10)}}.json`;
    document.body.append(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(url);
  }});

  document.getElementById('copyReview').addEventListener('click', async () => {{
    await navigator.clipboard.writeText(JSON.stringify(exportPayload(), null, 2));
    summary.textContent = 'Review JSON copied to clipboard';
    setTimeout(updateSummary, 1800);
  }});

  document.getElementById('clearReview').addEventListener('click', () => {{
    if (!confirm('Clear saved decisions in this browser?')) return;
    state = {{}};
    localStorage.removeItem(storageKey);
    cards.forEach(card => setCardDecision(card, '', ''));
    updateSummary();
  }});

  updateSummary();
}})();
</script>
</body>
</html>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html_doc, encoding="utf-8")
    print(f"wrote {OUT} with {len(data)} candidates")

if __name__ == "__main__":
    main()
