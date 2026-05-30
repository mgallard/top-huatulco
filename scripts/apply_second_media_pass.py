#!/usr/bin/env python3
"""Apply the second Huatulco media sourcing pass.

This pass promotes only source-checkable, open-license assets with enough
confidence for public preview use. It intentionally leaves routes without a safe
route-specific image unfilled rather than using misleading generic scenery.
"""
from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import unquote
from urllib.request import Request, urlopen

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
REVIEW_PATH = Path("/home/osohermes/.hermes/projects/tophuatulco/top-huatulco-media-review-2026-05-30.json")
PHOTO_DIR = ROOT / "public/images/photos"
MANIFEST_PATH = ROOT / "public/images/photos/media-sources.json"
SOURCE_REPORT = ROOT / "MEDIA_SECOND_PASS.md"

DIRECT_WINNERS = [
    {
        "id": "second-pass-chahue-huatulco-jpg",
        "route": "/destinations/chahue/",
        "title": "Huatulco.jpg",
        "creator": "Laura Elena Mendez M.",
        "license": "CC BY-SA 4.0",
        "licenseUrl": "https://creativecommons.org/licenses/by-sa/4.0/",
        "landing_page": "https://commons.wikimedia.org/wiki/File:Huatulco.jpg",
        "original_url": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Huatulco.jpg",
        "alt": "Playa Chahué and Bahía de Chahué in Huatulco",
        "routeNote": "Route-specific Commons image; file description identifies Playa Chahué / Bahía de Chahué.",
    },
    {
        "id": "second-pass-cacaluta-playa-jpg",
        "route": "/destinations/cacaluta/",
        "title": "CacalutaPlaya.JPG",
        "creator": "Danielllerandi",
        "license": "CC BY-SA 3.0",
        "licenseUrl": "https://creativecommons.org/licenses/by-sa/3.0/",
        "landing_page": "https://commons.wikimedia.org/wiki/File:CacalutaPlaya.JPG",
        "original_url": "https://upload.wikimedia.org/wikipedia/commons/3/37/CacalutaPlaya.JPG",
        "alt": "Wide view of Cacaluta beach in Huatulco National Park",
        "routeNote": "Route-specific Commons image; file description is Vista de la playa Cacaluta.",
    },
]

REVIEW_WINNERS = [
    {
        "candidateId": "candidate-005-005-candidate-playa-riscalillo-bah-as-de-huatulco-1-jpg-jpg",
        "route": "/things-to-do/snorkeling/",
        "alt": "Clear protected water at Playa Riscalillo, a useful Huatulco snorkeling context image",
        "routeNote": "Approved first-pass image used as protected-bay snorkeling context, not as a promise of exact conditions.",
    },
    {
        "candidateId": "candidate-002-002-candidate-maguey-bay-jpg-jpg",
        "route": "/things-to-do/boat-tours/",
        "alt": "Maguey Bay, a common Huatulco boat-day stop with calm water and green hills",
        "routeNote": "Approved first-pass bay image used for boat-day context because Maguey is a common stop on bay routes.",
    },
    {
        "candidateId": "candidate-021-La-Crucecita-Oaxaca-Mexico-jpg",
        "route": "/food-culture/",
        "alt": "La Crucecita town center context for Huatulco food and culture planning",
        "routeNote": "Approved first-pass town image used for the food/culture hub because most named restaurants and markets cluster in La Crucecita.",
    },
    {
        "candidateId": "candidate-012-012-destinations-san-agustin-bahia-san-agustin-huatulco-camping-webp-webp",
        "route": "/itineraries/5-days-oaxaca-coast/",
        "alt": "San Agustín Bay on the Oaxaca coast, suitable for a longer Huatulco coast itinerary",
        "routeNote": "Approved first-pass western-bay image used for the 5-day Oaxaca coast itinerary context.",
    },
]

UNFILLED_ROUTES = {
    "/destinations/organo/": "No confident open-license Órgano-specific image found. Do not substitute El Maguey unless labeled as adjacent context.",
    "/destinations/chachacual/": "No confident open-license Chachacual-specific image found in Commons/Openverse searches.",
    "/destinations/conejos/": "No confident open-license Conejos-specific image found in Commons/Openverse searches.",
    "/things-to-do/copalita-archaeology/": "No confident open-license Bocana del Río Copalita archaeological-site image found; keep as owned-photo priority.",
}

DESTINATION_IMAGE_NAMES = {
    "/destinations/chahue/": "Chahué",
    "/destinations/cacaluta/": "Cacaluta",
}

@dataclass
class Asset:
    id: str
    route: str
    title: str
    creator: str
    license: str
    landing_page: str
    original_url: str
    site_path: str
    alt: str
    width: int
    height: int
    sourceType: str
    derivative: str
    routeNote: str
    licenseUrl: str | None = None


def slugify(value: str) -> str:
    value = unquote(value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:90] or "huatulco-photo"


def html_escape(value: str) -> str:
    return (value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                 .replace('"', "&quot;").replace("'", "&#039;"))


def display_title(title: str) -> str:
    cleaned = re.sub(r"\.(jpg|jpeg|webp|png)$", "", title, flags=re.I)
    return cleaned.replace("_", " ")


def route_to_file(route: str) -> Path:
    return ROOT / "index.html" if route == "/" else ROOT / route.strip("/") / "index.html"


def download(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "TopHuatulco second media pass/1.0 (open-license attribution)"})
    with urlopen(req, timeout=60) as response:
        return response.read()


def make_asset(meta: dict, suffix: str) -> Asset:
    PHOTO_DIR.mkdir(parents=True, exist_ok=True)
    existing_site_path = meta.get("existing_site_path")
    if existing_site_path:
        out_path = ROOT / "public" / existing_site_path.lstrip("/")
        site_path = existing_site_path
    else:
        filename = f"huatulco-{slugify(meta['title'])}-{suffix}.webp"
        out_path = PHOTO_DIR / filename
        site_path = f"/images/photos/{filename}"
    if not out_path.exists():
        raw = download(meta["original_url"])
        tmp = PHOTO_DIR / f".{out_path.name}.source"
        tmp.write_bytes(raw)
        try:
            with Image.open(tmp) as img:
                img = ImageOps.exif_transpose(img).convert("RGB")
                img.thumbnail((1800, 1200), Image.Resampling.LANCZOS)
                img.save(out_path, "WEBP", quality=82, method=6)
        finally:
            tmp.unlink(missing_ok=True)
        time.sleep(0.4)
    with Image.open(out_path) as img:
        width, height = img.size
    return Asset(
        id=meta["id"],
        route=meta["route"],
        title=meta["title"],
        creator=meta.get("creator") or "Unknown creator",
        license=meta.get("license") or "License not listed",
        landing_page=meta["landing_page"],
        original_url=meta["original_url"],
        site_path=site_path,
        alt=meta["alt"],
        width=width,
        height=height,
        sourceType=meta.get("sourceType", "open-license second-pass source checked"),
        derivative="Resized WebP derivative from original source",
        routeNote=meta.get("routeNote", "Second-pass promoted route image."),
        licenseUrl=meta.get("licenseUrl"),
    )


def existing_site_path_for_candidate(candidate_id: str) -> str | None:
    if not MANIFEST_PATH.exists():
        return None
    data = json.loads(MANIFEST_PATH.read_text())
    for asset in data.get("assets", []):
        if asset.get("id") == candidate_id and asset.get("site_path"):
            local = ROOT / "public" / asset["site_path"].lstrip("/")
            if local.exists():
                return asset["site_path"]
    return None


def review_meta(candidate: dict, route: str, alt: str, route_note: str) -> dict:
    return {
        "id": f"second-pass-{candidate['id']}-{slugify(route)}",
        "route": route,
        "title": candidate["title"],
        "creator": candidate.get("creator") or "Unknown creator",
        "license": candidate.get("license") or "License not listed",
        "licenseUrl": candidate.get("licenseUrl"),
        "landing_page": candidate["landingPage"],
        "original_url": candidate["originalUrl"],
        "existing_site_path": existing_site_path_for_candidate(candidate["id"]),
        "alt": alt,
        "routeNote": route_note,
        "sourceType": "approved first-pass image reused in second-pass route context",
    }


def img_tag(asset: Asset, classes: str, loading: str = "eager") -> str:
    return (
        f"<img src='{asset.site_path}' alt='{html_escape(asset.alt)}' "
        f"class='{classes}' loading='{loading}' decoding='async' width='{asset.width}' height='{asset.height}'>"
    )


def apply_route_media(asset: Asset) -> None:
    path = route_to_file(asset.route)
    if not path.exists():
        raise FileNotFoundError(path)
    html = path.read_text()
    if "data-approved-route-media" in html:
        return
    figure = (
        "\n<section class='bg-background pb-2' data-approved-route-media='true' data-media-pass='second'>"
        "<div class='container-xl'>"
        "<figure class='overflow-hidden rounded-[2rem] border border-white bg-white shadow-card'>"
        f"{img_tag(asset, 'h-72 w-full object-cover sm:h-96')}"
        f"<figcaption class='px-5 py-3 text-xs font-semibold text-ink/60'>Reviewed image: {html_escape(display_title(asset.title))}. {html_escape(asset.routeNote)} Full credit on the Sources & credits page.</figcaption>"
        "</figure></div></section>\n"
    )
    new_html, n = re.subn(r"(</section>\n<section class='section-pad'>)", "</section>" + figure + "<section class='section-pad'>", html, count=1)
    if n == 0:
        new_html = html.replace("</main>", figure + "\n</main>", 1)
    path.write_text(new_html)


def update_destinations_js(assets: list[Asset]) -> None:
    path = ROOT / "src/data/destinations.js"
    text = path.read_text()
    by_route = {a.route: a for a in assets}
    for route, name in DESTINATION_IMAGE_NAMES.items():
        asset = by_route.get(route)
        if not asset:
            continue
        pattern = rf"(\{{ name: '{re.escape(name)}'.*?image: )'[^']+'(, imageAlt: )'[^']+'"
        repl = rf"\1'{asset.site_path}'\2'{html_escape(asset.alt)}'"
        text = re.sub(pattern, repl, text)
    path.write_text(text)


def load_existing_manifest() -> list[dict]:
    if not MANIFEST_PATH.exists():
        return []
    data = json.loads(MANIFEST_PATH.read_text())
    return data.get("assets", [])


def write_manifest(new_assets: list[Asset]) -> None:
    existing = load_existing_manifest()
    by_key = {(a.get("route"), a.get("site_path")): a for a in existing}
    for asset in new_assets:
        by_key[(asset.route, asset.site_path)] = asdict(asset)
    assets = list(by_key.values())
    data = {
        "updatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "reviewExport": str(REVIEW_PATH),
        "secondPassReport": str(SOURCE_REPORT),
        "reviewTotals": json.loads(REVIEW_PATH.read_text()).get("totals", {}) if REVIEW_PATH.exists() else {},
        "dnsGate": "TopHuatulco.com remains gated until final human review and remaining hard-to-source routes are approved.",
        "assets": assets,
    }
    MANIFEST_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def update_credits_page() -> None:
    data = json.loads(MANIFEST_PATH.read_text())
    rows = "".join(
        "<li class='rounded-3xl border border-border bg-white p-5 shadow-soft'>"
        f"<strong>{html_escape(asset['title'])}</strong>"
        f"<p class='mt-2 text-sm leading-6 text-ink/70'>Used on {html_escape(asset['route'])}. Photo by {html_escape(asset.get('creator') or 'Unknown creator')}; license: {html_escape(asset.get('license') or 'License not listed')}. "
        f"<a class='font-bold text-primary hover:underline' href='{html_escape(asset['landing_page'])}'>Source page</a>. "
        f"Local derivative: {html_escape(asset['site_path'])}.</p>"
        "</li>"
        for asset in data["assets"]
    )
    credits = (
        "<section class='section-pad' data-approved-image-credits='huatulco'><div class='container-xl max-w-5xl'>"
        "<div class='card p-7'><p class='eyebrow'>Reviewed media</p>"
        "<h2 class='mt-2 text-3xl'>Approved open-license image credits</h2>"
        "<p class='mt-3 text-sm leading-7 text-ink/70'>These images were source-checked, approved for preview use, and converted to local WebP derivatives. Routes without a confident image remain on the media-gap list rather than using misleading generic scenery.</p>"
        f"<ul class='mt-6 grid gap-4'>{rows}</ul></div></div></section>"
    )
    path = ROOT / "image-credits/index.html"
    html = path.read_text()
    if "data-approved-image-credits='huatulco'" in html:
        html = re.sub(r"<section class='section-pad' data-approved-image-credits='huatulco'>.*?</section>\s*", credits + "\n", html, count=1, flags=re.S)
    else:
        html = html.replace("</main>", credits + "\n</main>", 1)
    path.write_text(html)


def write_report(assets: list[Asset]) -> None:
    promoted = "\n".join(f"- `{a.route}` — {a.title} — {a.routeNote}" for a in assets)
    gaps = "\n".join(f"- `{route}` — {note}" for route, note in UNFILLED_ROUTES.items())
    SOURCE_REPORT.write_text(
        "# Top Huatulco second media pass\n\n"
        "This pass searched/pulled source-checkable open-license media and promoted only images with enough confidence for public preview use.\n\n"
        "## Promoted winners\n\n"
        f"{promoted}\n\n"
        "## Still unfilled / do not fake\n\n"
        f"{gaps}\n\n"
        "## Sourcing rule\n\n"
        "Do not fill Órgano, Chachacual, Conejos, or Copalita archaeology with generic Huatulco scenery unless the page caption clearly states the image is adjacent/contextual. Prefer owned photos or a new review board for those routes before production DNS.\n"
    )


def main() -> int:
    metas = list(DIRECT_WINNERS)
    if REVIEW_PATH.exists():
        review = json.loads(REVIEW_PATH.read_text())
        decisions = {item["id"]: item for item in review["decisions"]}
        for item in REVIEW_WINNERS:
            candidate = decisions[item["candidateId"]]
            if candidate.get("decision") != "approved":
                raise SystemExit(f"Refusing non-approved candidate {item['candidateId']}")
            metas.append(review_meta(candidate, item["route"], item["alt"], item["routeNote"]))
    else:
        raise SystemExit(f"Missing review JSON {REVIEW_PATH}")

    assets = []
    for meta in metas:
        suffix = slugify(meta["route"].strip("/") or "home")
        asset = make_asset(meta, suffix)
        apply_route_media(asset)
        assets.append(asset)
    update_destinations_js(assets)
    write_manifest(assets)
    update_credits_page()
    write_report(assets)
    print(f"Second media pass promoted {len(assets)} assets; left {len(UNFILLED_ROUTES)} hard gaps documented.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
