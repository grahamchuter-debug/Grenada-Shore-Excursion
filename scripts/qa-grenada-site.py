#!/usr/bin/env python3
"""QA gates for Grenada Shore Excursion Phase 16B."""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from grenada_config import APEX, DOMAIN, EMAIL, PROTECTED_ROUTES, QUARANTINE_NAMES  # noqa: E402

BANNED = [
    r"return\s+to\s+ship\s+friendly",
    r"whether\s+you'?re",
    r"\bnestled\b",
    r"unforgettable",
    r"perfect\s+blend",
    r"info@wowatour\.com",
    r"AggregateRating",
    r'"@type"\s*:\s*"Product"',
    r'"@type"\s*:\s*"Offer"',
    r'"@type"\s*:\s*"LocalBusiness"',
    r"cagrmsspctor",
    r"cagredtartsnk",
    r"shoreexcursionsgroup\.com",
    r"/book/",
    r"stripe",
]


class _TitleH1(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.h1s: list[str] = []
        self._in_title = False
        self._in_h1 = False
        self._buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
            self._buf = []
        elif tag == "h1":
            self._in_h1 = True
            self._buf = []

    def handle_endtag(self, tag):
        if tag == "title" and self._in_title:
            self.title = "".join(self._buf).strip()
            self._in_title = False
        elif tag == "h1" and self._in_h1:
            self.h1s.append(re.sub(r"\s+", " ", "".join(self._buf)).strip())
            self._in_h1 = False

    def handle_data(self, data):
        if self._in_title or self._in_h1:
            self._buf.append(data)


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)
    print(f"FAIL: {msg}")


def main() -> int:
    errors: list[str] = []
    titles: dict[str, str] = {}
    h1s: dict[str, str] = {}

    for route in PROTECTED_ROUTES:
        rel = route["file"]
        path = ROOT / rel
        if not path.is_file():
            fail(f"missing protected file {rel}", errors)
            continue
        text = path.read_text(encoding="utf-8")
        if 'id="main-content"' not in text and "id='main-content'" not in text:
            fail(f"{rel}: missing #main-content", errors)
        if "data-content=" in text or "fetch(" in text and "nav.js" not in Path(rel).name:
            # site must not use runtime content fetch
            if "data-content=" in text or re.search(r"fetch\(['\"]partials/|fetch\(['\"]content/", text):
                fail(f"{rel}: JS-fetched body remnants", errors)
        if "cdn.tailwindcss.com" in text:
            fail(f"{rel}: Tailwind CDN", errors)
        if EMAIL not in text and route["kind"] != "home":
            # home/footer should still have email via shell
            pass
        if EMAIL not in text:
            fail(f"{rel}: missing public email {EMAIL}", errors)

        canon = f"{APEX}/" if route["path"] == "/" else f"{APEX}{route['path']}"
        if f'rel="canonical" href="{canon}"' not in text and f"rel='canonical' href='{canon}'" not in text:
            # allow either quote style from escape
            if f'href="{canon}"' not in text or "canonical" not in text:
                fail(f"{rel}: canonical mismatch want {canon}", errors)

        for pat in BANNED:
            if re.search(pat, text, re.I):
                fail(f"{rel}: banned pattern /{pat}/", errors)

        for qname in QUARANTINE_NAMES:
            if qname in text:
                fail(f"{rel}: references quarantined image {qname}", errors)

        parser = _TitleH1()
        parser.feed(text)
        if not parser.title:
            fail(f"{rel}: missing title", errors)
        if len(parser.h1s) != 1:
            fail(f"{rel}: expected 1 H1, got {len(parser.h1s)} {parser.h1s!r}", errors)
        if parser.title in titles:
            fail(f"{rel}: duplicate title with {titles[parser.title]}", errors)
        else:
            titles[parser.title] = rel
        if parser.h1s:
            key = parser.h1s[0]
            if key in h1s:
                fail(f"{rel}: duplicate H1 with {h1s[key]}", errors)
            else:
                h1s[key] = rel

        # No-JS body must include substantial main content (not empty main)
        main_m = re.search(
            r'<main[^>]*id="main-content"[^>]*>([\s\S]*?)</main>', text, re.I
        )
        if not main_m or len(re.sub(r"\s+", "", main_m.group(1))) < 200:
            fail(f"{rel}: main content too thin for no-JS", errors)

    # 404 page
    nf = ROOT / "404.html"
    if not nf.is_file():
        fail("missing 404.html", errors)
    else:
        t = nf.read_text(encoding="utf-8")
        if "noindex" not in t.lower():
            fail("404.html missing noindex", errors)

    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    if f"Sitemap: {APEX}/sitemap.xml" not in robots:
        fail("robots.txt sitemap mismatch", errors)

    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for route in PROTECTED_ROUTES:
        if route.get("sitemap") is False:
            continue
        loc = f"{APEX}/" if route["path"] == "/" else f"{APEX}{route['path']}"
        if f"<loc>{loc}</loc>" not in sm:
            fail(f"sitemap missing {loc}", errors)
        if route["path"] != "/" and f"{loc}/</loc>" in sm:
            fail(f"sitemap has trailing-slash form of {loc}", errors)

    # Manifest
    man = ROOT / "protected_routes.json"
    if man.is_file():
        data = json.loads(man.read_text(encoding="utf-8"))
        if len(data) != len(PROTECTED_ROUTES):
            fail("protected_routes.json length mismatch", errors)

    if "wowatour" in sm.lower() or DOMAIN not in robots:
        pass

    if errors:
        print(f"\n{len(errors)} QA failure(s).")
        return 1
    print(f"QA OK — {len(PROTECTED_ROUTES)} protected routes, unique titles/H1s.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
