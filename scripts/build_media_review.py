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


def main() -> None:
    data = json.loads(CANDIDATES.read_text()) if CANDIDATES.exists() else []
    by_route = defaultdict(list)
    for item in data:
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
<article class='candidate-card' data-provider='{esc(item.get('provider'))}' data-review-status='{esc(item.get('reviewStatus'))}'>
  <div class='thumb'>{img_html}</div>
  <div class='card-body'>
    <p class='badge'>{esc(item.get('provider'))} · {esc(item.get('license'))}</p>
    <h3>{esc(item.get('title'))}</h3>
    <p><strong>Target:</strong> {esc(item.get('targetTitle'))}</p>
    <p><strong>Creator:</strong> {esc(item.get('creator'))}</p>
    <p><strong>Use:</strong> commercial {esc(item.get('commercialUseAllowed'))}; derivatives {esc(item.get('derivativesAllowed'))}</p>
    <p><strong>Review:</strong> {esc(item.get('reviewStatus'))} — {esc(item.get('licenseReview'))}</p>
    <p class='notes'>{esc(item.get('notes'))}</p>
    <div class='review-row' aria-label='Manual review choices'><span>□ Approve</span><span>□ Maybe</span><span>□ Reject</span></div>
    <div class='links'>
      <a href='{esc(item.get('landingPage'))}' target='_blank' rel='noopener'>Source page</a>
      <a href='{esc(item.get('originalUrl'))}' target='_blank' rel='noopener'>Original file</a>
    </div>
  </div>
</article>""")
        sections.append(f"<section><h2>{esc(route_label)} <span>{len(by_route[route])} candidates</span></h2><div class='grid'>{''.join(cards)}</div></section>")
    status_summary = ', '.join(f"{count} {status}" for status, count in sorted(status_counts.items()))
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
    :root {{ color-scheme: light; --ink:#17313A; --muted:#5B727A; --line:#D9E9ED; --bg:#F5FBFC; --primary:#2C9AB7; --sand:#FFF7E8; }}
    body {{ margin:0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; color:var(--ink); background:var(--bg); }}
    header {{ padding:3rem clamp(1rem,4vw,4rem); background:linear-gradient(135deg,#E7F7F9,#FFF7E8); border-bottom:1px solid var(--line); }}
    main {{ padding:2rem clamp(1rem,4vw,4rem) 4rem; }}
    h1 {{ margin:0; font-size:clamp(2rem,5vw,4rem); line-height:.95; letter-spacing:-.04em; }}
    h2 {{ margin:3rem 0 1rem; font-size:1.35rem; }}
    h2 span {{ color:var(--muted); font-size:.9rem; font-weight:600; }}
    p {{ line-height:1.55; }}
    .summary {{ display:grid; gap:1rem; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); margin-top:1.5rem; max-width:900px; }}
    .summary div {{ background:white; border:1px solid var(--line); border-radius:1.25rem; padding:1rem; box-shadow:0 12px 30px rgba(23,49,58,.06); }}
    .summary strong {{ display:block; font-size:1.7rem; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(270px,1fr)); gap:1rem; }}
    .candidate-card {{ background:white; border:1px solid var(--line); border-radius:1.25rem; overflow:hidden; box-shadow:0 12px 30px rgba(23,49,58,.06); display:flex; flex-direction:column; }}
    .thumb {{ aspect-ratio:4/3; background:#d9e9ed; display:grid; place-items:center; color:var(--muted); }}
    .thumb img {{ width:100%; height:100%; object-fit:cover; display:block; }}
    .card-body {{ padding:1rem; display:grid; gap:.45rem; }}
    .card-body p, .card-body h3 {{ margin:0; }}
    .card-body h3 {{ font-size:1rem; line-height:1.25; }}
    .badge {{ color:var(--primary); text-transform:uppercase; letter-spacing:.09em; font-size:.72rem; font-weight:800; }}
    .notes {{ color:var(--muted); font-size:.88rem; }}
    .links {{ display:flex; flex-wrap:wrap; gap:.5rem; margin-top:.5rem; }}
    .review-row {{ display:flex; flex-wrap:wrap; gap:.45rem; margin-top:.35rem; font-size:.82rem; font-weight:800; color:var(--ink); }}
    .review-row span {{ border:1px solid var(--line); border-radius:999px; padding:.35rem .55rem; background:#fff; }}
    a {{ color:var(--primary); font-weight:800; }}
    .links a {{ border:1px solid var(--line); border-radius:999px; padding:.5rem .75rem; text-decoration:none; background:var(--sand); }}
    .warning {{ max-width:900px; padding:1rem; margin-top:1.5rem; border-radius:1rem; background:#fff; border:1px solid #f2c97d; }}
  </style>
</head>
<body>
<header>
  <p class='badge'>Review-only · noindex</p>
  <h1>Top Huatulco media candidates</h1>
  <p>This board is for selecting real, license-safe Huatulco visuals before wiring them into public pages. Candidates are not approved yet.</p>
  <div class='summary'>
    <div><strong>{len(data)}</strong> candidates</div>
    <div><strong>{preview_count}</strong> local previews</div>
    <div><strong>{len(by_route)}</strong> routes covered</div>
    <div><strong>{esc(status_summary)}</strong> review status</div>
  </div>
  <div class='warning'><strong>Important:</strong> approve only after visual place-match and license review. Do not use images with uncertain subject, watermarks, people/privacy concerns, or source restrictions.</div>
</header>
<main>
{''.join(sections)}
</main>
</body>
</html>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html_doc, encoding="utf-8")
    print(f"wrote {OUT} with {len(data)} candidates")

if __name__ == "__main__":
    main()
