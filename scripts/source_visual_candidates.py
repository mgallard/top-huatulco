#!/usr/bin/env python3
"""Source review-only open-license visual candidates for Top Huatulco.

This script intentionally downloads only thumbnails/review previews, not production assets.
"""
from __future__ import annotations

import json
import re
import time
import urllib.parse
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
NEEDS_PATH = ROOT / "src/data/visual-needs.json"
OUT_PATH = ROOT / "src/data/visual-candidates.json"
PREVIEW_DIR = ROOT / "public/images/visual-candidates"
UA = "TopHuatulcoMediaReview/0.1 (https://top-huatulco.vercel.app; contact: editorial review)"
ALLOWED_LICENSE_HINTS = ("cc-by", "cc by", "cc-by-sa", "cc by-sa", "cc0", "public domain")
REJECT_LICENSE_HINTS = ("noncommercial", "non-commercial", "no derivatives", "no-derivatives", "all rights reserved")


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")[:80] or "candidate"


def is_bad_media(record: dict) -> bool:
    blob = " ".join(str(record.get(k, "")) for k in ("title", "landingPage", "imageUrl", "originalUrl", "mime"))
    low = blob.lower()
    return any(x in low for x in [".pdf", "application/pdf", "logo", "map.svg", "seal", "escudo"])


def license_ok(license_name: str, license_url: str = "") -> tuple[bool, str]:
    text = f"{license_name} {license_url}".lower()
    if any(h in text for h in REJECT_LICENSE_HINTS):
        return False, "rejected license restriction"
    if any(h in text for h in ALLOWED_LICENSE_HINTS):
        return True, "allowed open license"
    return False, "unknown license"


def commons_search(query: str, route: str, limit: int = 8) -> list[dict]:
    session = requests.Session()
    session.headers.update({"User-Agent": UA})
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": f"file:{query}",
        "gsrnamespace": 6,
        "gsrlimit": limit,
        "prop": "imageinfo",
        "iiprop": "url|mime|size|extmetadata",
        "iiurlwidth": 640,
        "format": "json",
        "formatversion": 2,
    }
    try:
        res = session.get("https://commons.wikimedia.org/w/api.php", params=params, timeout=25)
        res.raise_for_status()
        data = res.json()
    except Exception as exc:
        print(f"commons error {query}: {exc}")
        return []
    out = []
    for page in data.get("query", {}).get("pages", []):
        info = (page.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata") or {}
        title = page.get("title", "").replace("File:", "")
        license_name = (meta.get("LicenseShortName") or {}).get("value", "")
        license_url = (meta.get("LicenseUrl") or {}).get("value", "")
        ok, reason = license_ok(license_name, license_url)
        creator = re.sub(r"<[^>]+>", "", (meta.get("Artist") or {}).get("value", "")).strip()
        credit = re.sub(r"<[^>]+>", "", (meta.get("Credit") or {}).get("value", "")).strip()
        rec = {
            "provider": "wikimedia_commons",
            "route": route,
            "query": query,
            "title": title,
            "landingPage": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(page.get("title", "").replace(" ", "_")),
            "imageUrl": info.get("thumburl") or info.get("url"),
            "originalUrl": info.get("url"),
            "mime": info.get("mime"),
            "width": info.get("width"),
            "height": info.get("height"),
            "creator": creator or credit or "Unknown",
            "license": license_name,
            "licenseUrl": license_url,
            "commercialUseAllowed": ok,
            "derivativesAllowed": ok,
            "licenseReview": reason,
            "exactPlaceCandidate": True,
            "reviewStatus": "candidate" if ok else "needs-license-review",
            "notes": "Commons candidate; verify place match visually before production use.",
        }
        if not is_bad_media(rec):
            out.append(rec)
    return out


def openverse_search(query: str, route: str, limit: int = 6) -> list[dict]:
    url = "https://api.openverse.engineering/v1/images/"
    params = {"q": query, "page_size": limit, "license_type": "commercial,modification"}
    try:
        res = requests.get(url, params=params, headers={"User-Agent": UA}, timeout=25)
        res.raise_for_status()
        data = res.json()
    except Exception as exc:
        print(f"openverse error {query}: {exc}")
        return []
    out=[]
    for item in data.get("results", []):
        license_name = item.get("license", "")
        license_url = item.get("license_url", "")
        ok, reason = license_ok(license_name, license_url)
        rec={
            "provider":"openverse",
            "route":route,
            "query":query,
            "title":item.get("title") or query,
            "landingPage":item.get("foreign_landing_url") or item.get("url"),
            "imageUrl":item.get("thumbnail") or item.get("url"),
            "originalUrl":item.get("url"),
            "mime": "",
            "width": item.get("width"),
            "height": item.get("height"),
            "creator": item.get("creator") or "Unknown",
            "license": license_name,
            "licenseUrl": license_url,
            "commercialUseAllowed": ok,
            "derivativesAllowed": ok,
            "licenseReview": reason,
            "exactPlaceCandidate": False,
            "reviewStatus": "candidate" if ok else "needs-license-review",
            "notes":"Openverse discovery candidate; verify original source/license and place match before production use.",
        }
        if ok and not is_bad_media(rec):
            out.append(rec)
    return out


def download_preview(candidate: dict, idx: int) -> None:
    url = candidate.get("imageUrl")
    if not url:
        return
    ext = ".jpg"
    if ".png" in url.lower(): ext = ".png"
    if ".webp" in url.lower(): ext = ".webp"
    filename = f"{idx:03d}-{slugify(candidate['route'])}-{slugify(candidate['title'])}{ext}"
    dest = PREVIEW_DIR / filename
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=25)
        r.raise_for_status()
        ctype = r.headers.get("content-type", "")
        if "image" not in ctype.lower() or len(r.content) < 2000:
            candidate["previewDownloadError"] = f"bad content-type/size: {ctype} {len(r.content)}"
            return
        dest.write_bytes(r.content)
        candidate["localPreview"] = "/images/visual-candidates/" + filename
        candidate["previewBytes"] = len(r.content)
    except Exception as exc:
        candidate["previewDownloadError"] = str(exc)[:200]


def main() -> None:
    needs = json.loads(NEEDS_PATH.read_text())
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    candidates=[]
    seen=set()
    for need in needs:
        # keep initial pass scoped and useful: all tier1 + a few tier2 exact contexts
        if need["priority"] not in {"tier1", "tier2"}:
            continue
        for query in need["queries"][:2]:
            for rec in commons_search(query, need["route"], limit=8) + openverse_search(query, need["route"], limit=5):
                key=(rec.get("landingPage"), rec.get("originalUrl"), rec.get("route"))
                if key in seen:
                    continue
                seen.add(key)
                rec["targetTitle"] = need["title"]
                rec["targetPriority"] = need["priority"]
                rec["targetRole"] = need["role"]
                rec["draftAlt"] = need["draftAlt"]
                candidates.append(rec)
            time.sleep(0.4)
    # prefer licensed, image-like, route coverage; cap per route/provider to keep board manageable
    capped=[]
    per_route={}
    for rec in candidates:
        if rec["reviewStatus"] != "candidate":
            continue
        count=per_route.get(rec["route"],0)
        if count >= 5:
            continue
        capped.append(rec)
        per_route[rec["route"]]=count+1
    for i,rec in enumerate(capped,1):
        download_preview(rec,i)
    OUT_PATH.write_text(json.dumps(capped, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(capped)} candidates to {OUT_PATH}")
    print("route coverage:")
    for route,count in sorted(per_route.items()):
        print(f"  {route}: {count}")
    print(f"previews with local files: {sum(1 for c in capped if c.get('localPreview'))}")

if __name__ == "__main__":
    main()
