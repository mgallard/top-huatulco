#!/usr/bin/env python3
"""Apply approved Huatulco media-review decisions to public pages.

This script is deterministic: it reads the exported review JSON, downloads only
approved source images, creates optimized WebP site assets, writes a provenance
manifest, updates visible image credits, and wires route-matched images into
public pages without using rejected candidates.
"""
from __future__ import annotations

import json
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote
from urllib.request import Request, urlopen

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
REVIEW_PATH = Path("/home/osohermes/.hermes/projects/tophuatulco/top-huatulco-media-review-2026-05-30.json")
PHOTO_DIR = ROOT / "public/images/photos"
MANIFEST_PATH = ROOT / "public/images/photos/media-sources.json"

ROUTE_WINNERS = {
    "/": "candidate-001-001-candidate-bah-a-tangolunda-jpg-jpg",
    "/destinations/tangolunda/": "candidate-007-007-destinations-tangolunda-bah-a-tangolunda-jpg-jpg",
    "/destinations/santa-cruz/": "candidate-010-010-destinations-santa-cruz-bah-a-santa-cruz-en-huatulco-jpg-jpg",
    "/destinations/el-maguey/": "candidate-011-011-destinations-el-maguey-playa-el-maguey-panoramio-jpg-jpg",
    "/destinations/san-agustin/": "candidate-012-012-destinations-san-agustin-bahia-san-agustin-huatulco-camping-webp-webp",
    "/itineraries/3-days-huatulco/": "candidate-015-015-itineraries-3-days-huatulco-monumental-letters-in-huatulco-jpg-jpg",
    "/things-to-do/la-crucecita-market/": "candidate-022-022-things-to-do-la-crucecita-market-iglesia-de-la-crucecita-02-jpg-jpg",
}

MOSAIC_IDS = [
    "candidate-002-002-candidate-maguey-bay-jpg-jpg",
    "candidate-004-004-candidate-playa-la-cruz-bah-as-de-huatulco-jpg-jpg",
    "candidate-005-005-candidate-playa-riscalillo-bah-as-de-huatulco-1-jpg-jpg",
]

ALT_BY_ID = {
    "candidate-001-001-candidate-bah-a-tangolunda-jpg-jpg": "Tangolunda Bay and the Huatulco coastline from above",
    "candidate-002-002-candidate-maguey-bay-jpg-jpg": "Maguey Bay with calm water and green hills in Huatulco",
    "candidate-004-004-candidate-playa-la-cruz-bah-as-de-huatulco-jpg-jpg": "Playa La Cruz on the Huatulco coast",
    "candidate-005-005-candidate-playa-riscalillo-bah-as-de-huatulco-1-jpg-jpg": "Riscalillo beach and protected Huatulco water",
    "candidate-007-007-destinations-tangolunda-bah-a-tangolunda-jpg-jpg": "Tangolunda Bay water, beach, and rocky headlands in Huatulco",
    "candidate-010-010-destinations-santa-cruz-bah-a-santa-cruz-en-huatulco-jpg-jpg": "Santa Cruz Bay and harbor beach in Huatulco",
    "candidate-011-011-destinations-el-maguey-playa-el-maguey-panoramio-jpg-jpg": "El Maguey beach with calm bay water in Huatulco",
    "candidate-012-012-destinations-san-agustin-bahia-san-agustin-huatulco-camping-webp-webp": "San Agustín Bay beach and palapas in Huatulco",
    "candidate-015-015-itineraries-3-days-huatulco-monumental-letters-in-huatulco-jpg-jpg": "Huatulco landmark letters for a three-day trip plan",
    "candidate-022-022-things-to-do-la-crucecita-market-iglesia-de-la-crucecita-02-jpg-jpg": "Church of La Crucecita near Huatulco's town center",
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


def slugify(value: str) -> str:
    value = unquote(value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:90] or "huatulco-photo"


def route_to_file(route: str) -> Path:
    if route == "/":
        return ROOT / "index.html"
    return ROOT / route.strip("/") / "index.html"


def download(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "TopHuatulco media integration/1.0 (editorial image crediting)"})
    with urlopen(req, timeout=45) as response:
        return response.read()


def create_asset(decision: dict, suffix: str = "") -> Asset:
    PHOTO_DIR.mkdir(parents=True, exist_ok=True)
    base = slugify(decision["title"])
    filename = f"huatulco-{base}{suffix}.webp"
    out_path = PHOTO_DIR / filename

    if not out_path.exists():
        local_preview = decision.get("localPreview")
        if local_preview:
            tmp = ROOT / "public" / local_preview.lstrip("/")
            if not tmp.exists():
                tmp = None
        else:
            tmp = None

        if tmp is None:
            raw = download(decision["originalUrl"])
            tmp = PHOTO_DIR / f".{filename}.source"
            tmp.write_bytes(raw)
            remove_tmp = True
            time.sleep(0.6)
        else:
            remove_tmp = False

        with Image.open(tmp) as img:
            img = ImageOps.exif_transpose(img).convert("RGB")
            img.thumbnail((1800, 1200), Image.Resampling.LANCZOS)
            img.save(out_path, "WEBP", quality=82, method=6)
        if remove_tmp:
            tmp.unlink(missing_ok=True)

    with Image.open(out_path) as img:
        width, height = img.size
    return Asset(
        id=decision["id"],
        route=decision["route"],
        title=decision["title"],
        creator=decision.get("creator") or "Unknown creator",
        license=decision.get("license") or "License not listed",
        landing_page=decision["landingPage"],
        original_url=decision["originalUrl"],
        site_path=f"/images/photos/{filename}",
        alt=ALT_BY_ID.get(decision["id"], decision.get("targetTitle") or decision["title"]),
        width=width,
        height=height,
    )


def img_tag(asset: Asset, classes: str, loading: str = "lazy") -> str:
    return (
        f"<img src='{asset.site_path}' alt='{html_escape(asset.alt)}' "
        f"class='{classes}' loading='{loading}' decoding='async' width='{asset.width}' height='{asset.height}'>"
    )


def html_escape(value: str) -> str:
    return (value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                 .replace('"', "&quot;").replace("'", "&#039;"))


def display_title(title: str) -> str:
    cleaned = re.sub(r"\.(jpg|jpeg|webp|png)$", "", title, flags=re.I)
    cleaned = re.sub(r"\s+1$", "", cleaned)
    return cleaned


def apply_homepage(hero: Asset, mosaic: list[Asset]) -> None:
    path = ROOT / "index.html"
    html = path.read_text()
    html = re.sub(
        r"<img src='/images/lovable/hero-traveler\.jpg' alt='Pacific coast and bays near Huatulco' class='absolute inset-0 -z-20 h-full w-full object-cover opacity-65' width='1920' height='1080'>",
        img_tag(hero, "absolute inset-0 -z-20 h-full w-full object-cover opacity-70", "eager"),
        html,
    )
    if "data-approved-media-mosaic='huatulco'" not in html:
        cards = "".join(
            f"<figure class='overflow-hidden rounded-[1.75rem] border border-white/50 bg-white shadow-card'>"
            f"{img_tag(asset, 'h-56 w-full object-cover transition duration-700 hover:scale-105', 'lazy')}"
            f"<figcaption class='px-4 py-3 text-xs font-bold text-ink/65'>{html_escape(display_title(asset.title))}</figcaption>"
            f"</figure>"
            for asset in mosaic
        )
        section = (
            "\n<section class='section-pad bg-white' data-approved-media-mosaic='huatulco'>"
            "<div class='container-xl'>"
            "<div class='max-w-3xl'><p class='eyebrow'>Reviewed visuals</p>"
            "<h2 class='mt-2 text-3xl'>Real Huatulco bay photos now anchor the preview</h2>"
            "<p class='mt-3 text-sm leading-7 text-ink/70'>These approved open-license images are place-matched starting points for the public preview. Remaining uncovered bays still need a second sourcing pass before the real domain is connected.</p></div>"
            f"<div class='mt-8 grid gap-5 md:grid-cols-3'>{cards}</div>"
            "</div></section>\n"
        )
        html = html.replace("<section class='section-pad bg-surface'>", section + "<section class='section-pad bg-surface'>", 1)
    path.write_text(html)


def apply_route_media(asset: Asset) -> None:
    path = route_to_file(asset.route)
    if not path.exists():
        raise FileNotFoundError(path)
    html = path.read_text()
    if "data-approved-route-media" in html:
        return
    figure = (
        "\n<section class='bg-background pb-2' data-approved-route-media='true'>"
        "<div class='container-xl'>"
        "<figure class='overflow-hidden rounded-[2rem] border border-white bg-white shadow-card'>"
        f"{img_tag(asset, 'h-72 w-full object-cover sm:h-96', 'eager')}"
        f"<figcaption class='px-5 py-3 text-xs font-semibold text-ink/60'>Reviewed image: {html_escape(display_title(asset.title))}. Full credit on the Sources & credits page.</figcaption>"
        "</figure></div></section>\n"
    )
    html = re.sub(r"(</section>\n<section class='section-pad'>)", "</section>" + figure + "<section class='section-pad'>", html, count=1)
    path.write_text(html)


def update_destinations_js(assets_by_route: dict[str, Asset]) -> None:
    path = ROOT / "src/data/destinations.js"
    text = path.read_text()
    route_to_slug = {
        "/destinations/tangolunda/": "Tangolunda",
        "/destinations/santa-cruz/": "Santa Cruz",
        "/destinations/el-maguey/": "El Maguey",
        "/destinations/san-agustin/": "San Agustín",
    }
    for route, name in route_to_slug.items():
        asset = assets_by_route.get(route)
        if not asset:
            continue
        pattern = rf"(\{{ name: '{re.escape(name)}'.*?image: )'[^']+'(, imageAlt: )'[^']+'"
        repl = rf"\1'{asset.site_path}'\2'{html_escape(asset.alt)}'"
        text = re.sub(pattern, repl, text)
    path.write_text(text)


def update_manifest(assets: list[Asset], review: dict) -> None:
    data = {
        "updatedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "reviewExport": str(REVIEW_PATH),
        "reviewTotals": review.get("totals", {}),
        "dnsGate": "TopHuatulco.com remains gated until remaining uncovered routes and final visual/source QA are complete.",
        "assets": [asset.__dict__ | {"sourceType": "open-license reviewed by human", "derivative": "Resized WebP derivative from original source"} for asset in assets],
    }
    MANIFEST_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def update_credits_page(assets: list[Asset]) -> None:
    path = ROOT / "image-credits/index.html"
    rows = "".join(
        "<li class='rounded-3xl border border-border bg-white p-5 shadow-soft'>"
        f"<strong>{html_escape(asset.title)}</strong>"
        f"<p class='mt-2 text-sm leading-6 text-ink/70'>Used on {html_escape(asset.route)}. Photo by {html_escape(asset.creator)}. License: {html_escape(asset.license)}. "
        f"<a class='font-bold text-primary hover:underline' href='{html_escape(asset.landing_page)}'>Source page</a>. "
        f"Local derivative: {html_escape(asset.site_path)}.</p>"
        "</li>"
        for asset in assets
    )
    credits = (
        "<section class='section-pad' data-approved-image-credits='huatulco'><div class='container-xl max-w-5xl'>"
        "<div class='card p-7'><p class='eyebrow'>Reviewed media</p>"
        "<h2 class='mt-2 text-3xl'>Approved open-license image credits</h2>"
        "<p class='mt-3 text-sm leading-7 text-ink/70'>These images were approved from the Huatulco media-review export and converted to local WebP derivatives for the preview. Rejected candidates are not used on public pages.</p>"
        f"<ul class='mt-6 grid gap-4'>{rows}</ul></div></div></section>"
    )
    html = path.read_text()
    if "data-approved-image-credits='huatulco'" in html:
        html = re.sub(r"<section class='section-pad' data-approved-image-credits='huatulco'>.*?</section>", credits, html, count=1, flags=re.S)
    else:
        html = html.replace("</main>", credits + "\n</main>", 1)
    html = html.replace(
        "Source and media credit page for Top Huatulco. Third-party media and official references will be tracked here before launch.",
        "Source and media credit page for Top Huatulco, including approved open-license image credits and primary editorial references.",
    )
    path.write_text(html)


def main() -> int:
    if not REVIEW_PATH.exists():
        print(f"Missing review JSON: {REVIEW_PATH}", file=sys.stderr)
        return 1
    review = json.loads(REVIEW_PATH.read_text())
    decisions = {item["id"]: item for item in review["decisions"]}
    for cid in ROUTE_WINNERS.values():
        if decisions[cid]["decision"] != "approved":
            raise SystemExit(f"Selected route winner is not approved: {cid}")
    for cid in MOSAIC_IDS:
        if decisions[cid]["decision"] != "approved":
            raise SystemExit(f"Selected mosaic image is not approved: {cid}")

    assets_by_route: dict[str, Asset] = {}
    all_assets: list[Asset] = []
    seen: set[str] = set()
    for route, cid in ROUTE_WINNERS.items():
        asset = create_asset(decisions[cid])
        assets_by_route[route] = asset
        all_assets.append(asset)
        seen.add(cid)
    mosaic_assets = []
    for cid in MOSAIC_IDS:
        asset = create_asset(decisions[cid], suffix="-mosaic")
        mosaic_assets.append(asset)
        if cid not in seen:
            all_assets.append(asset)
            seen.add(cid)

    apply_homepage(assets_by_route["/"], mosaic_assets)
    for route, asset in assets_by_route.items():
        if route != "/":
            apply_route_media(asset)
    update_destinations_js(assets_by_route)
    update_manifest(all_assets, review)
    update_credits_page(all_assets)

    print(f"Applied {len(all_assets)} approved assets from {REVIEW_PATH}")
    print(f"Wrote {MANIFEST_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
