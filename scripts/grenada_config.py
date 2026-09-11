"""Grenada Shore Excursion — World 2.0 Phase 16B site configuration."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOMAIN = "grenadashoreexcursion.com"
APEX = f"https://{DOMAIN}"
SITE = "Grenada Shore Excursion"
EMAIL = "hello@grenadashoreexcursion.com"
DATE = "2026-09-11"
ACCENT = "text-pr-400"

FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)

HERO_GRADIENT = (
    "linear-gradient(140deg, rgba(15, 23, 42, 0.78) 0%, "
    "rgba(30, 64, 175, 0.62) 42%, rgba(249, 115, 22, 0.38) 72%, "
    "rgba(0, 0, 0, 0.22) 100%)"
)

# Active assets only (see images/ATTRIBUTION.md). Quarantine must not be referenced.
INTRO = "/images/grenada-intro.png"
INTRO_ALT = (
    "St George's Grenada hillside town and harbour with colourful roofs "
    "near the cruise port"
)

HERO_HOME = INTRO
HERO_HOME_ALT = INTRO_ALT

WATERFALLS = "/images/grenada-waterfalls.png"
WATERFALLS_ALT = (
    "Tiered rainforest waterfall and green pool in Grenada's interior"
)

RAINFOREST = "/images/grenada-rainforest.png"
RAINFOREST_ALT = (
    "Wooden rainforest boardwalk with monkeys in Grenada's interior forest"
)

# Coastline stock previously used as home hero — location not independently verified.
# Kept out of active use for Phase 16B; see images/quarantine and review notes.
# Beach / snorkel / spice pages use CSS-only heroes or verified St George's imagery.

QUARANTINE_NAMES = frozenset(
    {
        "best-grenada-excursions.png",
        "grand-anse-beach-hero.png",
        "grenada-beaches.png",
        "grenada-chocolate-rum.png",
        "grenada-cruise-port.png",
        "grenada-family.png",
        "grenada-faq.png",
        "grenada-island-sightseeing.png",
        "grenada-private-tours.png",
        "grenada-snorkelling.png",
        "grenada-spice-island.png",
        "one-day-grenada.png",
        "hero-grenada.png",
    }
)

# Extensionless, NO trailing slash — matches live GSC preferred form.
PROTECTED_ROUTES: list[dict] = [
    {"path": "/", "file": "index.html", "kind": "home"},
    {
        "path": "/best-grenada-shore-excursions",
        "file": "best-grenada-shore-excursions/index.html",
        "kind": "hub",
    },
    {
        "path": "/grenada-cruise-port-guide",
        "file": "grenada-cruise-port-guide/index.html",
        "kind": "guide",
    },
    {
        "path": "/one-day-in-grenada",
        "file": "one-day-in-grenada/index.html",
        "kind": "guide",
    },
    {
        "path": "/grand-anse-beach-excursions",
        "file": "grand-anse-beach-excursions/index.html",
        "kind": "attraction",
    },
    {
        "path": "/best-beaches-in-grenada",
        "file": "best-beaches-in-grenada/index.html",
        "kind": "decision",
    },
    {
        "path": "/grenada-waterfall-tours",
        "file": "grenada-waterfall-tours/index.html",
        "kind": "attraction",
    },
    {
        "path": "/grenada-spice-island-tours",
        "file": "grenada-spice-island-tours/index.html",
        "kind": "attraction",
    },
    {
        "path": "/grenada-rainforest-tours",
        "file": "grenada-rainforest-tours/index.html",
        "kind": "attraction",
    },
    {
        "path": "/grenada-chocolate-rum-tours",
        "file": "grenada-chocolate-rum-tours/index.html",
        "kind": "attraction",
    },
    {
        "path": "/grenada-island-sightseeing-tours",
        "file": "grenada-island-sightseeing-tours/index.html",
        "kind": "attraction",
    },
    {
        "path": "/grenada-snorkelling-tours",
        "file": "grenada-snorkelling-tours/index.html",
        "kind": "attraction",
    },
    {
        "path": "/grenada-private-tours",
        "file": "grenada-private-tours/index.html",
        "kind": "attraction",
    },
    {
        "path": "/grenada-family-excursions",
        "file": "grenada-family-excursions/index.html",
        "kind": "attraction",
    },
    {
        "path": "/grenada-faq",
        "file": "grenada-faq/index.html",
        "kind": "support",
    },
    {"path": "/contact", "file": "contact/index.html", "kind": "trust"},
    {"path": "/about", "file": "about/index.html", "kind": "trust"},
    {"path": "/privacy", "file": "privacy/index.html", "kind": "trust"},
    {"path": "/terms", "file": "terms/index.html", "kind": "trust"},
    {"path": "/methodology", "file": "methodology/index.html", "kind": "trust"},
]
