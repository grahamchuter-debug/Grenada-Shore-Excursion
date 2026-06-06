#!/usr/bin/env python3
"""Generate Grenada Shore Excursion static site files."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://grenadashoreexcursion.com"
SITE = "Grenada Shore Excursion"
DATE = "2026-06-06"
FONTS = (
    "https://fonts.googleapis.com/css2?family=Lora:wght@400;600;700"
    "&family=Work+Sans:wght@400;500;600;700&display=swap"
)
HERO_GRADIENT = (
    "linear-gradient(135deg, rgba(6, 78, 59, 0.82) 0%, "
    "rgba(5, 150, 105, 0.72) 45%, rgba(146, 64, 14, 0.58) 100%)"
)
ACCENT = "text-amber-200"

HOME_HERO = "images/hero-grenada.png"
HOME_HERO_ALT = "Aerial view of Grand Anse Beach with lush green hills and turquoise water in Grenada"
BEST_IMG = "images/best-grenada-excursions.png"
BEST_ALT = "Best Grenada shore excursions including beaches waterfalls and spice island tours"
PORT_IMG = "images/grenada-cruise-port.png"
PORT_ALT = "Cruise ship visiting St George's Grenada cruise port"
ONE_DAY_IMG = "images/one-day-grenada.png"
ONE_DAY_ALT = "One day in Grenada for cruise passengers visiting St George's"
GRAND_ANSE_IMG = "images/grand-anse-beach-hero.png"
GRAND_ANSE_ALT = "Grand Anse Beach in Grenada with white sand and Caribbean water"
WATERFALL_IMG = "images/grenada-waterfalls.png"
WATERFALL_ALT = "Waterfall tour in Grenada rainforest"
SPICE_IMG = "images/grenada-spice-island.png"
SPICE_ALT = "Spice island tour in Grenada with nutmeg and cocoa"
RAINFOREST_IMG = "images/grenada-rainforest.png"
RAINFOREST_ALT = "Rainforest excursion in Grenada"
CHOC_RUM_IMG = "images/grenada-chocolate-rum.png"
CHOC_RUM_ALT = "Grenada chocolate and rum shore excursion"
ISLAND_IMG = "images/grenada-island-sightseeing.png"
ISLAND_ALT = "Grenada island sightseeing tour from the cruise port"
SNORKEL_IMG = "images/grenada-snorkelling.png"
SNORKEL_ALT = "Snorkelling excursion in Grenada Caribbean waters"
PRIVATE_IMG = "images/grenada-private-tours.png"
PRIVATE_ALT = "Private Grenada shore excursion with flexible island sightseeing"
FAMILY_IMG = "images/grenada-family.png"
FAMILY_ALT = "Family friendly shore excursion in Grenada"
BEACHES_IMG = "images/grenada-beaches.png"
BEACHES_ALT = "Best beaches in Grenada for cruise passengers"
FAQ_IMG = "images/grenada-faq.png"
FAQ_ALT = "Cruise passengers exploring St George's Grenada"
INTRO_IMG = "images/grenada-intro.png"
INTRO_ALT = (
    "Grenada shore excursions with Grand Anse Beach, rainforest waterfalls, "
    "spice plantations and St George's harbour"
)


def page_shell(
    *,
    title: str,
    description: str,
    keywords: str,
    canonical_path: str,
    data_page: str,
    hero: str,
    content: str,
    preload: str = HOME_HERO,
    schema: dict | None = None,
    trust: bool = True,
) -> str:
    canon = f"{DOMAIN}/" if not canonical_path else f"{DOMAIN}/{canonical_path}"
    schema_block = ""
    if schema:
        schema_block = (
            f'  <script type="application/ld+json">\n'
            f"{json.dumps(schema, indent=2)}\n"
            f"  </script>\n"
        )
    trust_attr = '\n  data-trust-strip="partials/trust-strip.html"' if trust else ""
    content_file = content if content.startswith("content/") else f"content/{content}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="{canon}" />
  <link rel="preload" as="image" href="{preload}" fetchpriority="high" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{DOMAIN}/{preload}" />
  <meta property="og:site_name" content="{SITE}" />
  <meta name="twitter:card" content="summary_large_image" />

{schema_block}
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="js/tailwind-config.js"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="{FONTS}" rel="stylesheet" />
  <link rel="stylesheet" href="css/site.css" />
</head>
<body
  class="bg-white text-gray-800 antialiased"
  data-page="{data_page}"
  data-base=""
  data-hero="{hero}"
  data-content="{content_file}"{trust_attr}
>

  <div id="site-nav"></div>
  <div id="page-hero"></div>
  <div id="page-trust-strip"></div>
  <main id="page-content"></main>
  <div id="site-footer"></div>

  <script src="js/site.js"></script>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print(f"  wrote {path}")


def cruise_snapshot(
    *,
    time_in_port: str,
    best_for: str,
    activity_level: str,
    family: str,
    return_ship: str,
    popular: str,
) -> str:
    return f"""<aside class="cruise-snapshot mb-10 px-4 sm:px-0" aria-label="Cruise passenger snapshot">
  <h3 class="font-display font-bold text-lg text-gray-900 mb-4">Cruise Passenger Snapshot</h3>
  <dl class="cruise-snapshot__grid">
    <div class="cruise-snapshot__item"><dt>Typical Time In Port</dt><dd>{time_in_port}</dd></div>
    <div class="cruise-snapshot__item"><dt>Best For</dt><dd>{best_for}</dd></div>
    <div class="cruise-snapshot__item"><dt>Activity Level</dt><dd>{activity_level}</dd></div>
    <div class="cruise-snapshot__item"><dt>Family Friendly</dt><dd>{family}</dd></div>
    <div class="cruise-snapshot__item"><dt>Return To Ship Friendly</dt><dd>{return_ship}</dd></div>
    <div class="cruise-snapshot__item"><dt>Popular Excursion Types</dt><dd>{popular}</dd></div>
  </dl>
</aside>"""


def _hero_wave() -> str:
    return '<div class="absolute bottom-0 left-0 right-0"><svg viewBox="0 0 1440 48" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none" class="site-hero__wave" aria-hidden="true"><path d="M0 24 C360 48 1080 0 1440 24 L1440 48 L0 48 Z" fill="white"/></svg></div>'


def _hero_inner(
    eyebrow: str,
    title: str,
    lead: str,
    image: str,
    aria: str,
    breadcrumb: str = "",
    cta: tuple[str, str] | None = None,
    tags: list[str] | None = None,
) -> str:
    bc = ""
    if breadcrumb:
        bc = f"""<nav class="site-hero__breadcrumb flex items-center gap-2 mb-4 text-xs text-white/60" aria-label="Breadcrumb">
        <a href="index.html" class="hover:text-white transition-colors">Home</a>
        <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        <span class="text-white/80">{breadcrumb}</span>
      </nav>"""
    cta_html = ""
    if cta:
        cta_html = f'<a href="{cta[0]}" class="btn-ocean inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{cta[1]}</a>'
    tags_html = ""
    if tags:
        tags_html = '<div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">' + "".join(
            f'<span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">{t}</span>'
            for t in tags
        ) + "</div>"
    return f"""<section class="site-hero">
  <div class="absolute inset-0 hero-bg-custom" style="background-image: {HERO_GRADIENT}, url('{image}');" role="img" aria-label="{aria}"></div>
  <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl">
      {bc}
      <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
        <span class="w-2 h-2 rounded-full bg-amber-300 animate-pulse"></span>
        <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">{eyebrow}</span>
      </div>
      <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">{title}</h1>
      <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">{lead}</p>
      <div class="site-hero__actions flex flex-col sm:flex-row gap-3">{cta_html}</div>
      {tags_html}
    </div>
  </div>
  {_hero_wave()}
</section>"""


def _internal_links() -> str:
    return """<nav class="mt-10 pt-8 border-t border-gray-100" aria-label="Related Grenada guides">
  <p class="text-sm font-semibold text-gray-900 mb-3">Plan your port day</p>
  <div class="flex flex-wrap gap-3 text-sm">
    <a href="grenada-cruise-port-guide.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Port Guide</a>
    <span class="text-gray-300">·</span>
    <a href="best-grenada-shore-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Best Excursions</a>
    <span class="text-gray-300">·</span>
    <a href="grand-anse-beach-excursions.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Grand Anse Beach</a>
    <span class="text-gray-300">·</span>
    <a href="grenada-waterfall-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Waterfalls</a>
    <span class="text-gray-300">·</span>
    <a href="grenada-spice-island-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Spice Island Tours</a>
    <span class="text-gray-300">·</span>
    <a href="grenada-rainforest-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Rainforest Tours</a>
    <span class="text-gray-300">·</span>
    <a href="grenada-chocolate-rum-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Chocolate &amp; Rum</a>
    <span class="text-gray-300">·</span>
    <a href="grenada-private-tours.html" class="text-ocean-600 hover:text-ocean-800 font-medium">Private Tours</a>
    <span class="text-gray-300">·</span>
    <a href="grenada-faq.html" class="text-ocean-600 hover:text-ocean-800 font-medium">FAQ</a>
  </div>
</nav>"""


def _comparison_section() -> str:
    rows = [
        ("Grand Anse Beach", "3–5 hrs", "White sand &amp; calm swim", "Low — beach time", "grand-anse-beach-excursions.html"),
        ("Waterfall Tour", "3–4 hrs", "Rainforest falls &amp; pools", "Moderate — walking", "grenada-waterfall-tours.html"),
        ("Spice Island Tour", "3–4 hrs", "Nutmeg, cocoa &amp; plantations", "Low to moderate", "grenada-spice-island-tours.html"),
        ("Rainforest Tour", "4–5 hrs", "Grand Etang &amp; lush interior", "Moderate — trails", "grenada-rainforest-tours.html"),
        ("Chocolate &amp; Rum Tour", "4–5 hrs", "Cocoa, chocolate &amp; distillery", "Low — tastings", "grenada-chocolate-rum-tours.html"),
        ("Snorkelling", "3–4 hrs", "Reef &amp; sculpture park", "Moderate — swim", "grenada-snorkelling-tours.html"),
        ("Private Tour", "4–6 hrs", "Custom pacing for groups", "Varies", "grenada-private-tours.html"),
    ]
    body = ""
    for name, dur, best, activity, link in rows:
        body += f"""<tr class="border-b border-gren-50 hover:bg-sand-50/80">
      <td class="py-4 pr-4 font-semibold text-gray-900"><a href="{link}" class="text-ocean-600 hover:text-ocean-800">{name}</a></td>
      <td class="py-4 px-3 text-gray-600">{dur}</td>
      <td class="py-4 px-3 text-gray-600">{best}</td>
      <td class="py-4 px-3 text-gray-600">{activity}</td>
      <td class="py-4 pl-3"><a href="{link}" class="text-gren-600 font-medium text-xs whitespace-nowrap">Guide →</a></td>
    </tr>"""
    return f"""<section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 text-center mb-4">Which Grenada Excursion Is Right for Me?</h2>
  <p class="text-center text-gray-600 text-sm max-w-2xl mx-auto mb-10">Match your St George's port day to Grand Anse Beach, rainforest waterfalls, spice plantations, chocolate tastings or snorkel reefs — all timed for typical cruise schedules.</p>
  <div class="overflow-x-auto rounded-3xl border border-gren-100 shadow-sm">
    <table class="w-full text-sm text-left min-w-[720px]">
      <thead class="bg-ocean-800 text-white">
        <tr>
          <th class="py-4 px-4 font-semibold rounded-tl-3xl">Excursion</th>
          <th class="py-4 px-3 font-semibold">Duration</th>
          <th class="py-4 px-3 font-semibold">Best For</th>
          <th class="py-4 px-3 font-semibold">Activity Level</th>
          <th class="py-4 px-4 font-semibold rounded-tr-3xl">Details</th>
        </tr>
      </thead>
      <tbody class="bg-white">{body}</tbody>
    </table>
  </div>
</div></section>"""


def _card_grid(cards: list[tuple]) -> str:
    items = []
    for img, alt, title, desc, link, label in cards:
        items.append(f"""<div class="card-hover bg-white rounded-3xl overflow-hidden shadow-md border border-gren-50 flex flex-col">
      <div class="card-media h-44 relative overflow-hidden">
        <img src="{img}" alt="{alt}" width="600" height="352" loading="lazy" decoding="async" />
      </div>
      <div class="p-6 flex flex-col flex-1">
        <h3 class="text-lg font-display font-semibold text-gray-900 mb-2">{title}</h3>
        <p class="text-sm text-gray-500 leading-relaxed flex-1">{desc}</p>
        <a href="{link}" class="mt-5 btn-ocean inline-flex items-center justify-center text-white text-xs font-semibold px-5 py-2.5 rounded-full">{label}</a>
      </div>
    </div>""")
    return '<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">' + "".join(items) + "</div>"


def _snapshot_default(**overrides: str) -> str:
    defaults = dict(
        time_in_port="7–9 hours (typical)",
        best_for="Grand Anse Beach, waterfalls, spice tours, rainforest",
        activity_level="Varies — see comparison",
        family="Excellent with age-appropriate picks",
        return_ship="Operators usually allow 60–90 min buffer",
        popular="Grand Anse Beach, waterfalls, spice island, snorkelling",
    )
    defaults.update(overrides)
    return cruise_snapshot(**defaults)


def _content_excursion_page(
    intro: str,
    bullets: list[str],
    snapshot_kwargs: dict,
    img: str,
    alt: str,
) -> str:
    bl = "".join(
        f'<li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span>{b}</li>'
        for b in bullets
    )
    snap = _snapshot_default(**snapshot_kwargs)
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">{intro}</p>
        <ul class="space-y-3 mb-6">{bl}</ul>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{img}" alt="{alt}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _hero_home() -> str:
    return f"""  <section class="site-hero">
    <div class="absolute inset-0 hero-bg" style="background-image: {HERO_GRADIENT}, url('{HOME_HERO}');" role="img" aria-label="{HOME_HERO_ALT}"></div>
    <div class="site-hero__inner max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="max-w-3xl">
        <div class="site-hero__eyebrow inline-flex items-center gap-2 bg-white/15 backdrop-blur-sm border border-white/30 rounded-full px-4 py-1.5 mb-3">
          <span class="w-2 h-2 rounded-full bg-amber-300 animate-pulse"></span>
          <span class="text-white/90 text-xs font-semibold tracking-widest uppercase">St George's · Spice Island</span>
        </div>
        <h1 class="site-hero__title text-4xl sm:text-5xl lg:text-[3.25rem] font-display font-bold text-white leading-tight mb-3">
          Grenada Shore<br/><span class="{ACCENT}">Excursions</span><br/>from the Cruise Port
        </h1>
        <p class="site-hero__lead text-base sm:text-lg text-white/85 font-light leading-relaxed mb-5 max-w-2xl">
          Grand Anse Beach, lush rainforest waterfalls, spice plantations, chocolate and rum tastings — the shore experiences cruise passengers book most in Grenada.
        </p>
        <div class="site-hero__actions flex flex-col sm:flex-row gap-3">
          <a href="best-grenada-shore-excursions.html" class="btn-primary inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">Compare Excursions</a>
          <a href="grand-anse-beach-excursions.html" class="btn-outline inline-flex items-center justify-center gap-2 text-white font-semibold px-7 py-3 rounded-full text-sm">Grand Anse Beach</a>
        </div>
        <div class="site-hero__tags flex flex-wrap gap-2 mt-5 pt-4 border-t border-white/20">
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Grand Anse Beach</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Rainforest</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Waterfalls</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">Spice Island</span>
          <span class="inline-flex items-center bg-white/10 border border-white/25 rounded-full px-3.5 py-1.5 text-xs font-semibold text-white">St George's Harbour</span>
        </div>
      </div>
    </div>
    {_hero_wave()}
  </section>"""


def _content_home() -> str:
    cards = _card_grid([
        (GRAND_ANSE_IMG, GRAND_ANSE_ALT, "Grand Anse Beach", "Two miles of white sand and calm turquoise water — Grenada's signature beach day from St George's.", "grand-anse-beach-excursions.html", "Grand Anse"),
        (WATERFALL_IMG, WATERFALL_ALT, "Waterfall Tours", "Annandale Falls and rainforest cascades within easy reach of the cruise port.", "grenada-waterfall-tours.html", "Waterfalls"),
        (SPICE_IMG, SPICE_ALT, "Spice Island Tours", "Nutmeg, cinnamon and cocoa at working plantations — Grenada earned its Spice Island name.", "grenada-spice-island-tours.html", "Spice Tours"),
        (RAINFOREST_IMG, RAINFOREST_ALT, "Rainforest Tours", "Grand Etang National Park, crater lake views and lush green interior drives.", "grenada-rainforest-tours.html", "Rainforest"),
    ])
    snap = _snapshot_default()
    return f"""<section class="pt-8 pb-8 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <div class="inline-flex items-center gap-2 text-ocean-600 text-xs font-semibold tracking-widest uppercase mb-3"><div class="w-8 h-px bg-ocean-400"></div>St George's Cruise Port</div>
        <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-5">Why Cruise Guests<br/><span class="text-ocean-600">Choose Grenada</span></h2>
        <p class="text-gray-600 leading-relaxed mb-5">Grenada blends harbour-side St George's with rainforest interior and Grand Anse Beach — waterfalls, spice estates and chocolate tastings fit a typical <strong>7–9 hour</strong> port call.</p>
        <a href="best-grenada-shore-excursions.html" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Browse All Excursions</a>
      </div>
      <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
        <img src="{INTRO_IMG}" alt="{INTRO_ALT}" width="800" height="600" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-16 bg-sand-50"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-12"><h2 class="text-3xl font-display font-bold text-gray-900">Top Grenada Experiences</h2></div>
      {cards}
    </div></section>
    {_comparison_section()}
    <section class="py-16 cta-gradient"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-white mb-4">Plan Your Grenada Port Day</h2>
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <a href="grenada-cruise-port-guide.html" class="btn-primary inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">Port Guide</a>
        <a href="grenada-faq.html" class="btn-outline inline-flex items-center justify-center text-white font-semibold px-8 py-4 rounded-full">FAQ</a>
      </div>
    </div></section>"""


def _content_best() -> str:
    cards = _card_grid([
        (GRAND_ANSE_IMG, GRAND_ANSE_ALT, "Grand Anse Beach", "Beach transfers with chair options and cruise-timed returns.", "grand-anse-beach-excursions.html", "Grand Anse"),
        (WATERFALL_IMG, WATERFALL_ALT, "Waterfall Tours", "Rainforest falls with guided walks and photo stops.", "grenada-waterfall-tours.html", "Waterfalls"),
        (SPICE_IMG, SPICE_ALT, "Spice Island Tours", "Plantation visits with nutmeg, cinnamon and cocoa.", "grenada-spice-island-tours.html", "Spice Tours"),
        (PRIVATE_IMG, PRIVATE_ALT, "Private Tours", "Custom island routes for your group.", "grenada-private-tours.html", "Private"),
    ])
    snap = _snapshot_default(best_for="Comparing all excursion types", popular="See comparison table below")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <h2 class="text-3xl font-display font-bold text-gray-900 mb-4">Best Grenada Shore Excursions</h2>
      <p class="text-gray-600 leading-relaxed text-sm">Operators meet at <strong>St George's cruise terminals</strong> and plan returns with buffer before all aboard.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    {_comparison_section()}
    <section class="py-16 bg-white"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Excursion Guides</h2>
      {cards}
      <div class="mt-12 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_port() -> str:
    snap = _snapshot_default(
        activity_level="Low at terminal; moderate on tours",
        popular="Walk-on port, taxis, tour pickups",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 leading-relaxed text-sm">Ships dock in <strong>St George's harbour</strong> — colourful Carenage waterfront, Grand Anse Beach and rainforest tours are minutes away on a typical <strong>7–9 hour</strong> call.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-7xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Where Ships Arrive</h2>
      <div class="info-image rounded-3xl aspect-[21/9] shadow-xl overflow-hidden mb-8 max-w-5xl mx-auto">
        <img src="{PORT_IMG}" alt="{PORT_ALT}" width="1200" height="514" loading="lazy" decoding="async" />
      </div>
      <div class="grid lg:grid-cols-2 gap-6 text-sm">
        <div class="bg-white rounded-3xl p-6 border border-gren-100"><h3 class="font-display font-bold text-lg mb-2">St George's Cruise Pier</h3><p class="text-gray-600">The Melville Street Cruise Terminal places you at the Carenage — waterfront cafés, spice market stalls and tour desks are steps from the gangway.</p></div>
        <div class="bg-white rounded-3xl p-6 border border-gren-100"><h3 class="font-display font-bold text-lg mb-2">Getting To Grand Anse</h3><p class="text-gray-600">Grand Anse Beach is 10–15 minutes by taxi or organised transfer. Waterfall and spice tours head inland from the same pier pickups.</p></div>
      </div>
    </div></section>
    <section class="py-12 bg-white"><div class="max-w-7xl mx-auto px-4">
      <div class="grid sm:grid-cols-3 gap-6 text-sm">
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Currency</strong><p class="mt-2 text-gray-600">Eastern Caribbean dollar (XCD). <strong>US dollars</strong> widely accepted at the port and on tours.</p></div>
        <div class="bg-ocean-50 rounded-2xl p-6"><strong class="text-gray-900">Language</strong><p class="mt-2 text-gray-600">English is the official language. Local Grenadian Creole is common — guides speak clear English for cruise guests.</p></div>
        <div class="bg-sand-50 rounded-2xl p-6"><strong class="text-gray-900">Getting Around</strong><p class="mt-2 text-gray-600">Taxis at the pier; island tours and snorkel boats include port or marina pickup.</p></div>
      </div>
      <p class="text-center mt-8"><a href="one-day-in-grenada.html" class="text-ocean-600 font-semibold text-sm">One-day itinerary →</a></p>
      <div class="mt-10 max-w-3xl mx-auto">{_internal_links()}</div>
    </div></section>"""


def _content_one_day() -> str:
    snap = _snapshot_default(best_for="Grand Anse morning + spice or waterfall afternoon")
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-3xl mx-auto px-4 text-center">
      <p class="text-gray-600 text-sm">Sample timeline for a <strong>7–9 hour</strong> St George's call. Adjust for your ship's actual times.</p>
    </div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-12 bg-sand-50"><div class="max-w-3xl mx-auto px-4">
      <h2 class="text-2xl font-display font-bold text-center mb-8">Classic Grenada Port Day</h2>
      <ol class="space-y-4 text-sm">
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-gren-100"><span class="font-bold text-ocean-600 shrink-0">08:00</span><div><strong>Depart pier</strong><p class="text-gray-600 mt-1">Meet Grand Anse transfer or waterfall tour — morning slots beat afternoon heat inland.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-gren-100"><span class="font-bold text-ocean-600 shrink-0">09:30</span><div><strong>Grand Anse Beach or Annandale Falls</strong><p class="text-gray-600 mt-1">Choose calm beach swim or a short rainforest waterfall walk — both are cruise favourites.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-gren-100"><span class="font-bold text-ocean-600 shrink-0">13:00</span><div><strong>Spice plantation or Fort Frederick</strong><p class="text-gray-600 mt-1">Dougaldston Estate nutmeg stop or hilltop fort views over St George's harbour.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-gren-100"><span class="font-bold text-ocean-600 shrink-0">15:00</span><div><strong>Carenage stroll</strong><p class="text-gray-600 mt-1">Waterfront spice stalls and harbour views near the pier before return buffer.</p></div></li>
        <li class="flex gap-4 bg-white rounded-2xl p-5 border border-gren-100"><span class="font-bold text-ocean-600 shrink-0">16:30</span><div><strong>Back at ship</strong><p class="text-gray-600 mt-1">Allow margin before published all-aboard.</p></div></li>
      </ol>
      <div class="mt-10">{_internal_links()}</div>
    </div></section>"""


def _content_grand_anse() -> str:
    return _content_excursion_page(
        "Grand Anse Beach stretches two miles along Grenada's southwest coast — white sand, calm turquoise water and beach bars a short drive from St George's cruise port. Organised excursions include transport, often chair rental and cruise-timed returns.",
        [
            "10–15 minute transfer from Melville Street terminal.",
            "Calm morning water suits families and relaxed swimmers.",
            "Beach vendors rent chairs and umbrellas — confirm inclusions.",
            "Pair with afternoon spice tour only on longer port calls.",
        ],
        dict(
            best_for="Beach lovers and first-time visitors",
            activity_level="Low — swimming and walking",
            popular="Grand Anse transfers, beach day packages",
        ),
        GRAND_ANSE_IMG,
        GRAND_ANSE_ALT,
    )


def _content_waterfall() -> str:
    return _content_excursion_page(
        "Grenada's rainforest hides accessible waterfalls minutes from St George's — Annandale Falls is the most popular, with guided walks, natural pools and lush green canopy. Cruise excursions include transport and fixed returns to the pier.",
        [
            "Annandale Falls suits most fitness levels with short paths.",
            "Wear water-friendly shoes — paths can be damp and uneven.",
            "Seven Sisters and Concord Falls need longer drives — check duration.",
            "Morning tours leave afternoon time for Grand Anse Beach.",
        ],
        dict(
            best_for="Nature lovers and photo seekers",
            activity_level="Moderate — walking on trails",
            popular="Annandale Falls tours, rainforest waterfall combos",
        ),
        WATERFALL_IMG,
        WATERFALL_ALT,
    )


def _content_spice() -> str:
    return _content_excursion_page(
        "Grenada is the Spice Island — nutmeg, cinnamon, cloves and cocoa grow across the interior. Spice plantation tours visit working estates like Dougaldston, with demonstrations, tastings and stories of Grenada's agricultural heritage.",
        [
            "3–4 hour tours fit standard port schedules.",
            "Nutmeg and cocoa demonstrations are family-friendly.",
            "Often combined with Belmont Estate chocolate stop.",
            "Great rainy-day alternative to beach time.",
        ],
        dict(
            best_for="Culture curious and food lovers",
            activity_level="Low to moderate — estate walks",
            popular="Spice plantation tours, nutmeg estate visits",
        ),
        SPICE_IMG,
        SPICE_ALT,
    )


def _content_rainforest() -> str:
    return _content_excursion_page(
        "Grand Etang National Park sits in Grenada's mountainous interior — crater lake views, montane rainforest and endemic birdlife on guided drives and short trails. Air-conditioned vans suit guests who want lush green scenery beyond the coast.",
        [
            "4–5 hour loops fit standard port calls.",
            "Cooler temperatures at elevation — bring a light layer.",
            "Less physically demanding than long waterfall hikes.",
            "Private options let you add Fort Frederick viewpoints.",
        ],
        dict(
            best_for="Nature enthusiasts and photographers",
            activity_level="Moderate — trails and van touring",
            popular="Grand Etang tours, rainforest drives",
        ),
        RAINFOREST_IMG,
        RAINFOREST_ALT,
    )


def _content_choc_rum() -> str:
    return _content_excursion_page(
        "Grenada produces organic cocoa and small-batch chocolate at estates like Belmont, while River Antoine Rum Distillery still uses a water-powered cane press. Combined chocolate and rum tours offer tastings, factory walks and cruise-timed returns.",
        [
            "Belmont Estate suits families with chocolate-making demos.",
            "River Antoine tours show traditional rum production.",
            "Age limits may apply at distillery tastings — check operator.",
            "Often paired with a spice plantation on the same route.",
        ],
        dict(
            best_for="Food and drink enthusiasts",
            activity_level="Low — tastings and short walks",
            popular="Belmont Estate chocolate, River Antoine rum tours",
        ),
        CHOC_RUM_IMG,
        CHOC_RUM_ALT,
    )


def _content_island() -> str:
    return _content_excursion_page(
        "Island sightseeing tours cover Grenada's highlights in one loop — St George's Carenage, Fort Frederick viewpoints, Grand Anse Beach photo stops and spice estate visits. Air-conditioned vans suit guests who want an overview on a first visit.",
        [
            "4–5 hour loops fit standard port calls.",
            "Fort Frederick offers panoramic harbour views.",
            "Less physically demanding than rainforest hikes.",
            "Private options let you prioritise fort vs beach stops.",
        ],
        dict(
            best_for="Sightseers and first-time visitors",
            activity_level="Low to moderate — van and short walks",
            popular="Island drives, Fort Frederick tours",
        ),
        ISLAND_IMG,
        ISLAND_ALT,
    )


def _content_snorkelling() -> str:
    return _content_excursion_page(
        "Grenada's west coast and Molinere Underwater Sculpture Park offer clear snorkelling over reef patches, tropical fish and art installations beneath the surface. Tours supply masks, fins and guides from St George's marina pickups.",
        [
            "Half-day trips fit most 7–9 hour port schedules.",
            "Beginners welcome — flotation aids often available.",
            "Use reef-safe sunscreen or a rash guard.",
            "Sculpture park visits need calm sea conditions.",
        ],
        dict(
            best_for="Reef swimmers and underwater art fans",
            activity_level="Moderate — boat and snorkelling",
            popular="Sculpture park snorkel, reef snorkel tours",
        ),
        SNORKEL_IMG,
        SNORKEL_ALT,
    )


def _content_private() -> str:
    return _content_excursion_page(
        "Private SUVs and vans let your group set the pace — Grand Anse Beach first, Annandale Falls, spice estate lunch and Fort Frederick in one custom loop. Drivers serving cruise guests understand all-aboard deadlines.",
        [
            "Split cost across families to rival per-person coach pricing.",
            "Share priorities when booking — routes are flexible.",
            "Ideal for mixed mobility within one group.",
            "Confirm return time in writing before payment.",
        ],
        dict(
            best_for="Groups wanting custom pacing",
            activity_level="Low to moderate — varies by itinerary",
            popular="Private island tours, custom snorkel charters",
        ),
        PRIVATE_IMG,
        PRIVATE_ALT,
    )


def _content_family() -> str:
    return _content_excursion_page(
        "Family excursions in Grenada favour calm Grand Anse Beach time, gentle Annandale Falls walks, spice plantation demos and supervised snorkel trips. Two well-paced stops beat three rushed attractions with children.",
        [
            "Grand Anse suits school-age kids with shade breaks.",
            "Waterfall paths can be slippery — verify age suitability.",
            "Private vans simplify nap timing and snack stops.",
            "Chocolate estate tours often engage younger visitors.",
        ],
        dict(
            best_for="Kids, parents and multi-generational groups",
            family="Excellent with age-appropriate tour choice",
            popular="Beach transfers, family island tours",
        ),
        FAMILY_IMG,
        FAMILY_ALT,
    )


def _content_beaches() -> str:
    snap = _snapshot_default(
        best_for="Choosing Grand Anse vs Morne Rouge",
        popular="Grand Anse Beach, Morne Rouge, Magazine Beach",
    )
    return f"""<section class="pt-8 pb-4 bg-white"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="grid lg:grid-cols-2 gap-12 items-start">
      <div>
        <p class="text-gray-600 leading-relaxed mb-6">Grenada beaches range from the famous Grand Anse strip to quieter coves — <strong>Grand Anse Beach</strong> for calm swim and resorts, <strong>Morne Rouge</strong> for sheltered bay water, and <strong>Magazine Beach</strong> for a local feel south of the port.</p>
        <ul class="space-y-3 mb-6">
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Grand Anse Beach</strong> — two miles of white sand, beach bars, cruise-friendly transfers.</li>
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Morne Rouge</strong> — calm turquoise bay, quieter than Grand Anse.</li>
          <li class="flex gap-2 text-sm text-gray-600"><span class="text-ocean-500">✓</span><strong>Magazine Beach</strong> — local snorkel spot, less crowded on weekdays.</li>
        </ul>
        <a href="grand-anse-beach-excursions.html" class="text-ocean-600 font-semibold text-sm">Grand Anse Beach excursions →</a>
      </div>
      <div class="card-media rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
        <img src="{BEACHES_IMG}" alt="{BEACHES_ALT}" width="600" height="450" loading="lazy" decoding="async" />
      </div>
    </div></div></section>
    <section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="pb-16 bg-white"><div class="max-w-3xl mx-auto px-4">{_internal_links()}</div></section>"""


def _content_faq() -> str:
    snap = _snapshot_default(best_for="Quick planning answers", popular="See FAQ topics below")
    return f"""<section class="pb-8 bg-white"><div class="max-w-7xl mx-auto px-4">{snap}</div></section>
    <section class="py-8 bg-white"><div class="max-w-3xl mx-auto px-4 space-y-4">
      <details class="faq-item rounded-2xl border border-gren-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How long do cruise ships stay in St George's?</summary>
        <p class="mt-4 text-sm text-gray-500">Most St George's calls are 7 to 9 hours. A Grand Anse Beach morning plus spice plantation or waterfall tour fits comfortably with return buffer.</p></details>
      <details class="faq-item rounded-2xl border border-gren-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">How far is Grand Anse Beach from the cruise port?</summary>
        <p class="mt-4 text-sm text-gray-500">Grand Anse Beach is about 10–15 minutes by taxi from Melville Street Cruise Terminal. Organised excursions include round-trip transport and timed returns.</p></details>
      <details class="faq-item rounded-2xl border border-gren-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">What is Grenada famous for?</summary>
        <p class="mt-4 text-sm text-gray-500">Grenada is the Spice Island — nutmeg, cinnamon and cocoa plantations, plus rainforest waterfalls, organic chocolate, rum distilleries and Grand Anse Beach.</p></details>
      <details class="faq-item rounded-2xl border border-gren-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Beach or waterfall for a port day?</summary>
        <p class="mt-4 text-sm text-gray-500">Grand Anse Beach suits relaxed swim and sun; Annandale Falls suits nature lovers who want lush rainforest scenery. Many guests do beach in the morning and a spice or waterfall stop later.</p></details>
      <details class="faq-item rounded-2xl border border-gren-100 p-5"><summary class="font-semibold text-gray-900 cursor-pointer">Ship excursion or book independently?</summary>
        <p class="mt-4 text-sm text-gray-500">Ship tours guarantee the vessel waits if the operator is late. Reputable Grenada operators plan returns with buffer — confirm policies and read reviews before booking ashore.</p></details>
      {_internal_links()}
    </div></section>"""


def _faq_schema() -> dict:
    qa = [
        (
            "How long do cruise ships stay in St George's?",
            "Most St George's calls are 7 to 9 hours.",
        ),
        (
            "How far is Grand Anse Beach from the cruise port?",
            "Grand Anse Beach is about 10–15 minutes by taxi from the cruise terminal.",
        ),
        (
            "What is Grenada famous for?",
            "Nutmeg, cinnamon, cocoa plantations, rainforest waterfalls, chocolate, rum and Grand Anse Beach.",
        ),
        (
            "Beach or waterfall for a port day?",
            "Grand Anse for beach; Annandale Falls for rainforest waterfalls — many guests combine both.",
        ),
        (
            "Ship excursion or book independently?",
            "Ship tours guarantee wait-if-late; reputable locals plan buffer returns.",
        ),
    ]
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }


def main() -> None:
    print("Building Grenada Shore Excursion site…")

    write(
        "partials/nav.html",
        f"""<nav class="fixed top-0 left-0 right-0 z-50 bg-white/90 border-b border-gren-100 shadow-sm">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-12">
      <a href="index.html" class="flex items-center gap-2">
        <div class="w-7 h-7 rounded-full btn-ocean flex items-center justify-center">
          <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"/>
          </svg>
        </div>
        <span class="font-display font-semibold text-ocean-800 text-base leading-tight">Grenada<br/><span class="text-[10px] font-body font-normal text-gren-600 tracking-widest uppercase">Shore Excursion</span></span>
      </a>
      <div class="hidden lg:flex items-center gap-5 text-sm font-medium">
        <a href="index.html" data-nav="home" class="text-gray-600 hover:text-ocean-600 transition-colors">Home</a>
        <a href="best-grenada-shore-excursions.html" data-nav="excursions" class="text-gray-600 hover:text-ocean-600 transition-colors">Excursions</a>
        <a href="grand-anse-beach-excursions.html" data-nav="grand-anse" class="text-gray-600 hover:text-ocean-600 transition-colors">Grand Anse</a>
        <a href="grenada-waterfall-tours.html" data-nav="waterfalls" class="text-gray-600 hover:text-ocean-600 transition-colors">Waterfalls</a>
        <a href="grenada-spice-island-tours.html" data-nav="spice" class="text-gray-600 hover:text-ocean-600 transition-colors">Spice Tours</a>
        <a href="grenada-snorkelling-tours.html" data-nav="snorkelling" class="text-gray-600 hover:text-ocean-600 transition-colors">Snorkelling</a>
        <a href="grenada-cruise-port-guide.html" data-nav="port" class="text-gray-600 hover:text-ocean-600 transition-colors">Port Guide</a>
      </div>
      <a href="best-grenada-shore-excursions.html" class="hidden md:inline-flex items-center gap-2 btn-ocean text-white text-sm font-semibold px-4 py-2 rounded-full shadow-md">
        Compare Tours
      </a>
      <button type="button" class="lg:hidden p-2 rounded-lg text-gray-600 hover:bg-sand-50" aria-label="Open menu">
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
      </button>
    </div>
  </div>
</nav>
""",
    )

    write(
        "partials/footer.html",
        f"""  <footer class="bg-gray-900 text-gray-400 py-14">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
        <div class="sm:col-span-2 lg:col-span-1">
          <a href="index.html" class="font-display font-semibold text-white text-lg">{SITE}</a>
          <p class="mt-3 text-sm leading-relaxed">Planning guide for cruise visitors to Grenada from St George's port. Not affiliated with any cruise line.</p>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Excursions</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="best-grenada-shore-excursions.html" class="hover:text-white transition-colors">Best Excursions</a></li>
            <li><a href="grand-anse-beach-excursions.html" class="hover:text-white transition-colors">Grand Anse Beach</a></li>
            <li><a href="grenada-waterfall-tours.html" class="hover:text-white transition-colors">Waterfall Tours</a></li>
            <li><a href="grenada-spice-island-tours.html" class="hover:text-white transition-colors">Spice Island Tours</a></li>
            <li><a href="grenada-rainforest-tours.html" class="hover:text-white transition-colors">Rainforest Tours</a></li>
            <li><a href="grenada-chocolate-rum-tours.html" class="hover:text-white transition-colors">Chocolate &amp; Rum</a></li>
            <li><a href="grenada-snorkelling-tours.html" class="hover:text-white transition-colors">Snorkelling</a></li>
            <li><a href="grenada-private-tours.html" class="hover:text-white transition-colors">Private Tours</a></li>
          </ul>
        </div>
        <div>
          <h3 class="text-white text-sm font-semibold uppercase tracking-wider mb-4">Resources</h3>
          <ul class="space-y-2 text-sm">
            <li><a href="grenada-cruise-port-guide.html" class="hover:text-white transition-colors">Port Guide</a></li>
            <li><a href="one-day-in-grenada.html" class="hover:text-white transition-colors">One Day in Grenada</a></li>
            <li><a href="grenada-island-sightseeing-tours.html" class="hover:text-white transition-colors">Island Sightseeing</a></li>
            <li><a href="best-beaches-in-grenada.html" class="hover:text-white transition-colors">Best Beaches</a></li>
            <li><a href="grenada-family-excursions.html" class="hover:text-white transition-colors">Family Excursions</a></li>
            <li><a href="grenada-faq.html" class="hover:text-white transition-colors">FAQ</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-gray-800 pt-8 text-xs text-center sm:text-left">
        <p>&copy; 2026 {SITE}. Verify times and prices with operators before booking.</p>
      </div>
    </div>
  </footer>
""",
    )

    write(
        "partials/trust-strip.html",
        f"""<section class="trust-strip" aria-label="Grenada shore excursion highlights">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <ul class="trust-strip__list">
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Grand Anse Beach</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Spice Island Tours</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Rainforest Waterfalls</li>
      <li class="trust-strip__item"><span class="trust-strip__check" aria-hidden="true">✔</span> Cruise-Friendly Returns</li>
    </ul>
  </div>
</section>
""",
    )

    heroes = {
        "hero-home.html": _hero_home(),
        "hero-excursions.html": _hero_inner(
            "St George's · Spice Island",
            f"Best Grenada<br/><span class=\"{ACCENT}\">Shore Excursions</span>",
            "Compare Grand Anse Beach, waterfall tours, spice plantations, rainforest drives, chocolate and rum tastings, snorkelling and private options for your ship schedule.",
            BEST_IMG,
            BEST_ALT,
            breadcrumb="Best Excursions",
        ),
        "hero-port-guide.html": _hero_inner(
            "Cruise Passenger Guide",
            f"Grenada<br/><span class=\"{ACCENT}\">Cruise Port Guide</span>",
            "St George's harbour, Melville Street terminal, taxis, currency and how to plan shore time ashore.",
            PORT_IMG,
            PORT_ALT,
            breadcrumb="Port Guide",
            cta=("best-grenada-shore-excursions.html", "View Shore Excursions →"),
            tags=["🚢 St George's", "🏖️ Grand Anse", "🌿 Rainforest", "🌶️ Spice Island"],
        ),
        "hero-one-day.html": _hero_inner(
            "Port Day Timeline",
            f"One Day in<br/><span class=\"{ACCENT}\">Grenada</span>",
            "Hour-by-hour plan from gangway to departure — Grand Anse Beach, waterfalls or spice tours with return buffer.",
            ONE_DAY_IMG,
            ONE_DAY_ALT,
            breadcrumb="One Day in Grenada",
        ),
        "hero-grand-anse.html": _hero_inner(
            "Southwest Coast · Grenada",
            f"Grand Anse Beach<br/><span class=\"{ACCENT}\">Excursions</span>",
            "Two miles of white sand and calm turquoise water — Grenada's signature beach day for cruise guests.",
            GRAND_ANSE_IMG,
            GRAND_ANSE_ALT,
            breadcrumb="Grand Anse Beach",
        ),
        "hero-waterfalls.html": _hero_inner(
            "Rainforest · Grenada",
            f"Grenada<br/><span class=\"{ACCENT}\">Waterfall</span> Tours",
            "Annandale Falls and rainforest cascades with guided walks and natural pools near St George's.",
            WATERFALL_IMG,
            WATERFALL_ALT,
            breadcrumb="Waterfall Tours",
        ),
        "hero-spice.html": _hero_inner(
            "Spice Island · Grenada",
            f"Grenada Spice Island<br/><span class=\"{ACCENT}\">Tours</span>",
            "Nutmeg, cinnamon, cocoa and working plantations — taste why Grenada earned its Spice Island name.",
            SPICE_IMG,
            SPICE_ALT,
            breadcrumb="Spice Island Tours",
        ),
        "hero-rainforest.html": _hero_inner(
            "Grand Etang · Grenada",
            f"Grenada<br/><span class=\"{ACCENT}\">Rainforest</span> Tours",
            "Crater lake views, montane forest and lush green interior drives from the cruise port.",
            RAINFOREST_IMG,
            RAINFOREST_ALT,
            breadcrumb="Rainforest Tours",
        ),
        "hero-chocolate-rum.html": _hero_inner(
            "Belmont · River Antoine",
            f"Chocolate &amp; Rum<br/><span class=\"{ACCENT}\">Tours</span>",
            "Organic cocoa, bean-to-bar chocolate and traditional rum distillery visits timed for cruise schedules.",
            CHOC_RUM_IMG,
            CHOC_RUM_ALT,
            breadcrumb="Chocolate & Rum Tours",
        ),
        "hero-island.html": _hero_inner(
            "Sightseeing · Grenada",
            f"Grenada Island<br/><span class=\"{ACCENT}\">Sightseeing</span> Tours",
            "Fort Frederick, St George's harbour, Grand Anse viewpoints and spice stops by air-conditioned van.",
            ISLAND_IMG,
            ISLAND_ALT,
            breadcrumb="Island Sightseeing",
        ),
        "hero-snorkelling.html": _hero_inner(
            "West Coast · Grenada",
            f"Grenada<br/><span class=\"{ACCENT}\">Snorkelling</span> Tours",
            "Reef patches, tropical fish and the underwater sculpture park — boat trips with gear from St George's.",
            SNORKEL_IMG,
            SNORKEL_ALT,
            breadcrumb="Snorkelling Tours",
        ),
        "hero-private.html": _hero_inner(
            "Custom Shore Trips",
            f"Grenada<br/><span class=\"{ACCENT}\">Private Tours</span>",
            "Private vans at your group's pace — Grand Anse Beach, waterfalls, spice estates and custom island routes.",
            PRIVATE_IMG,
            PRIVATE_ALT,
            breadcrumb="Private Tours",
        ),
        "hero-family.html": _hero_inner(
            "All Ages Welcome",
            f"Grenada<br/><span class=\"{ACCENT}\">Family</span> Excursions",
            "Calm beaches, gentle waterfall walks, spice demos and relaxed island drives for every generation.",
            FAMILY_IMG,
            FAMILY_ALT,
            breadcrumb="Family Excursions",
        ),
        "hero-beaches.html": _hero_inner(
            "Beach Guide · Grenada",
            f"Best Beaches<br/><span class=\"{ACCENT}\">in Grenada</span>",
            "Grand Anse Beach, Morne Rouge and Magazine Beach — choose the right sand for your St George's port day.",
            BEACHES_IMG,
            BEACHES_ALT,
            breadcrumb="Best Beaches",
        ),
        "hero-faq.html": _hero_inner(
            "Cruise Planning Answers",
            f"Grenada<br/><span class=\"{ACCENT}\">Excursions FAQ</span>",
            "St George's port hours, Grand Anse distance, spice island highlights and booking independent vs ship tours.",
            FAQ_IMG,
            FAQ_ALT,
            breadcrumb="FAQ",
        ),
    }
    for name, html in heroes.items():
        write(f"partials/{name}", html)

    contents = {
        "home.html": _content_home(),
        "best-grenada-shore-excursions.html": _content_best(),
        "grenada-cruise-port-guide.html": _content_port(),
        "one-day-in-grenada.html": _content_one_day(),
        "grand-anse-beach-excursions.html": _content_grand_anse(),
        "grenada-waterfall-tours.html": _content_waterfall(),
        "grenada-spice-island-tours.html": _content_spice(),
        "grenada-rainforest-tours.html": _content_rainforest(),
        "grenada-chocolate-rum-tours.html": _content_choc_rum(),
        "grenada-island-sightseeing-tours.html": _content_island(),
        "grenada-snorkelling-tours.html": _content_snorkelling(),
        "grenada-private-tours.html": _content_private(),
        "grenada-family-excursions.html": _content_family(),
        "best-beaches-in-grenada.html": _content_beaches(),
        "grenada-faq.html": _content_faq(),
    }
    for name, html in contents.items():
        write(f"content/{name}", html)

    pages = [
        dict(
            file="index.html",
            title=f"{SITE} | Grand Anse Beach, Waterfalls &amp; Spice Tours from St George's",
            description="Plan Grenada shore excursions for cruise passengers — Grand Anse Beach, rainforest waterfalls, spice plantations, chocolate and rum tours, snorkelling and private trips from St George's cruise port.",
            keywords="Grenada shore excursions, Grenada cruise excursions, Grand Anse Beach cruise tour, St George's cruise port tours, spice island excursion Grenada",
            path="",
            data_page="home",
            hero="partials/hero-home.html",
            content="home.html",
            schema={
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": SITE,
                "url": f"{DOMAIN}/",
                "description": "Planning guide for Grenada cruise shore excursions from St George's",
            },
        ),
        dict(
            file="best-grenada-shore-excursions.html",
            title="Best Grenada Shore Excursions | Compare St George's Cruise Tours",
            description="Compare the best Grenada shore excursions — Grand Anse Beach, waterfall tours, spice plantations, rainforest drives, chocolate and rum tastings, snorkelling and private options with cruise timing.",
            keywords="best Grenada shore excursions, Grenada cruise port tours, compare Grenada excursions, St George's shore trips",
            path="best-grenada-shore-excursions.html",
            data_page="excursions",
            hero="partials/hero-excursions.html",
            content="best-grenada-shore-excursions.html",
            preload=BEST_IMG,
            schema={
                "@context": "https://schema.org",
                "@type": "WebPage",
                "name": "Best Grenada Shore Excursions",
                "url": f"{DOMAIN}/best-grenada-shore-excursions.html",
            },
        ),
        dict(
            file="grenada-cruise-port-guide.html",
            title="Grenada Cruise Port Guide | St George's for Cruise Passengers",
            description="Grenada cruise port guide — St George's harbour, Melville Street terminal, taxis, XCD and USD, and top shore excursions timed for your ship's schedule.",
            keywords="Grenada cruise port guide, St George's cruise port, Grenada port day, cruise passenger guide Grenada",
            path="grenada-cruise-port-guide.html",
            data_page="port",
            hero="partials/hero-port-guide.html",
            content="grenada-cruise-port-guide.html",
            preload=PORT_IMG,
            schema={
                "@context": "https://schema.org",
                "@type": "Article",
                "headline": "Grenada Cruise Port Guide",
                "url": f"{DOMAIN}/grenada-cruise-port-guide.html",
            },
        ),
        dict(
            file="one-day-in-grenada.html",
            title="One Day in Grenada from a Cruise Ship | Port Itinerary",
            description="How to spend one day in Grenada on a cruise stop — Grand Anse Beach, waterfalls and spice tours sample timeline with return-to-ship buffer.",
            keywords="one day in Grenada cruise, Grenada port day itinerary, St George's cruise stop planning",
            path="one-day-in-grenada.html",
            data_page="port",
            hero="partials/hero-one-day.html",
            content="one-day-in-grenada.html",
            preload=ONE_DAY_IMG,
        ),
        dict(
            file="grand-anse-beach-excursions.html",
            title="Grand Anse Beach Excursions | Grenada Cruise Shore Tours",
            description="Grand Anse Beach excursions from St George's — white sand, calm swim, beach transfers and cruise-friendly returns.",
            keywords="Grand Anse Beach excursion Grenada, Grand Anse cruise port, beach day Grenada shore excursion",
            path="grand-anse-beach-excursions.html",
            data_page="grand-anse",
            hero="partials/hero-grand-anse.html",
            content="grand-anse-beach-excursions.html",
            preload=GRAND_ANSE_IMG,
        ),
        dict(
            file="grenada-waterfall-tours.html",
            title="Grenada Waterfall Tours | Rainforest Cruise Excursions",
            description="Grenada waterfall tours from St George's — Annandale Falls, rainforest walks and natural pools with cruise-friendly returns.",
            keywords="Grenada waterfall tour cruise, Annandale Falls excursion, rainforest waterfall Grenada shore excursion",
            path="grenada-waterfall-tours.html",
            data_page="waterfalls",
            hero="partials/hero-waterfalls.html",
            content="grenada-waterfall-tours.html",
            preload=WATERFALL_IMG,
        ),
        dict(
            file="grenada-spice-island-tours.html",
            title="Grenada Spice Island Tours | Nutmeg &amp; Cocoa Cruise Excursions",
            description="Grenada spice island tours from the cruise port — nutmeg, cinnamon, cocoa plantations and tastings timed for cruise schedules.",
            keywords="Grenada spice tour cruise, nutmeg plantation excursion, spice island shore excursion Grenada",
            path="grenada-spice-island-tours.html",
            data_page="spice",
            hero="partials/hero-spice.html",
            content="grenada-spice-island-tours.html",
            preload=SPICE_IMG,
        ),
        dict(
            file="grenada-rainforest-tours.html",
            title="Grenada Rainforest Tours | Grand Etang Cruise Excursions",
            description="Grenada rainforest tours for cruise passengers — Grand Etang National Park, crater lake views and lush interior drives.",
            keywords="Grenada rainforest tour cruise, Grand Etang excursion, rainforest shore excursion Grenada",
            path="grenada-rainforest-tours.html",
            data_page="rainforest",
            hero="partials/hero-rainforest.html",
            content="grenada-rainforest-tours.html",
            preload=RAINFOREST_IMG,
        ),
        dict(
            file="grenada-chocolate-rum-tours.html",
            title="Grenada Chocolate &amp; Rum Tours | Belmont &amp; Distillery Excursions",
            description="Grenada chocolate and rum tours from St George's — Belmont Estate cocoa, bean-to-bar tastings and River Antoine distillery visits.",
            keywords="Grenada chocolate tour cruise, rum distillery excursion Grenada, Belmont Estate shore excursion",
            path="grenada-chocolate-rum-tours.html",
            data_page="chocolate-rum",
            hero="partials/hero-chocolate-rum.html",
            content="grenada-chocolate-rum-tours.html",
            preload=CHOC_RUM_IMG,
        ),
        dict(
            file="grenada-island-sightseeing-tours.html",
            title="Grenada Island Sightseeing Tours | Fort Frederick &amp; Harbour Views",
            description="Grenada island sightseeing tours for cruise passengers — Fort Frederick, St George's harbour, Grand Anse and spice estate highlights.",
            keywords="Grenada island tour cruise, sightseeing Grenada shore excursion, Fort Frederick cruise tour",
            path="grenada-island-sightseeing-tours.html",
            data_page="island",
            hero="partials/hero-island.html",
            content="grenada-island-sightseeing-tours.html",
            preload=ISLAND_IMG,
        ),
        dict(
            file="grenada-snorkelling-tours.html",
            title="Grenada Snorkelling Tours | Reef &amp; Sculpture Park Excursions",
            description="Grenada snorkelling tours on the west coast — reef sites, tropical fish and Molinere Underwater Sculpture Park with cruise-friendly returns.",
            keywords="Grenada snorkelling tours, sculpture park snorkel cruise, reef snorkel Grenada shore excursion",
            path="grenada-snorkelling-tours.html",
            data_page="snorkelling",
            hero="partials/hero-snorkelling.html",
            content="grenada-snorkelling-tours.html",
            preload=SNORKEL_IMG,
        ),
        dict(
            file="grenada-private-tours.html",
            title="Grenada Private Tours | Custom Cruise Shore Excursions",
            description="Private Grenada tours for cruise passengers — custom vans with flexible Grand Anse Beach, waterfall and spice island itineraries.",
            keywords="Grenada private tours cruise, private shore excursion Grenada, custom St George's tour",
            path="grenada-private-tours.html",
            data_page="private",
            hero="partials/hero-private.html",
            content="grenada-private-tours.html",
            preload=PRIVATE_IMG,
        ),
        dict(
            file="grenada-family-excursions.html",
            title="Grenada Family Excursions | Kid-Friendly St George's Cruise Tours",
            description="Family-friendly Grenada excursions — Grand Anse Beach, gentle waterfall walks, spice demos and relaxed island tours for cruise guests with children.",
            keywords="Grenada family excursions, kid friendly Grenada cruise tours, family shore excursion Grenada",
            path="grenada-family-excursions.html",
            data_page="family",
            hero="partials/hero-family.html",
            content="grenada-family-excursions.html",
            preload=FAMILY_IMG,
        ),
        dict(
            file="best-beaches-in-grenada.html",
            title="Best Beaches in Grenada | Grand Anse &amp; Morne Rouge for Cruise Passengers",
            description="Best beaches in Grenada for cruise visitors — Grand Anse Beach, Morne Rouge and Magazine Beach near St George's on a port day.",
            keywords="best beaches Grenada cruise, Grand Anse Beach Morne Rouge, beach guide Grenada port day",
            path="best-beaches-in-grenada.html",
            data_page="beaches",
            hero="partials/hero-beaches.html",
            content="best-beaches-in-grenada.html",
            preload=BEACHES_IMG,
        ),
        dict(
            file="grenada-faq.html",
            title="Grenada Shore Excursions FAQ | St George's Cruise Planning",
            description="FAQ for Grenada shore excursions — St George's port hours, Grand Anse distance, spice island highlights, beach vs waterfall and independent vs ship booking.",
            keywords="Grenada shore excursions FAQ, Grenada cruise port questions, Grand Anse Beach FAQ cruise",
            path="grenada-faq.html",
            data_page="port",
            hero="partials/hero-faq.html",
            content="grenada-faq.html",
            preload=FAQ_IMG,
            schema=_faq_schema(),
        ),
    ]

    for p in pages:
        write(
            p["file"],
            page_shell(
                title=p["title"],
                description=p["description"],
                keywords=p["keywords"],
                canonical_path=p["path"],
                data_page=p["data_page"],
                hero=p["hero"],
                content=p["content"],
                preload=p.get("preload", HOME_HERO),
                schema=p.get("schema"),
            ),
        )

    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")

    urls = [
        ("", "1.0", "weekly"),
        ("best-grenada-shore-excursions.html", "0.9", "monthly"),
        ("grenada-cruise-port-guide.html", "0.8", "monthly"),
        ("one-day-in-grenada.html", "0.8", "monthly"),
        ("grand-anse-beach-excursions.html", "0.9", "monthly"),
        ("grenada-waterfall-tours.html", "0.9", "monthly"),
        ("grenada-spice-island-tours.html", "0.9", "monthly"),
        ("grenada-rainforest-tours.html", "0.8", "monthly"),
        ("grenada-chocolate-rum-tours.html", "0.8", "monthly"),
        ("grenada-island-sightseeing-tours.html", "0.8", "monthly"),
        ("grenada-snorkelling-tours.html", "0.8", "monthly"),
        ("grenada-private-tours.html", "0.8", "monthly"),
        ("grenada-family-excursions.html", "0.8", "monthly"),
        ("best-beaches-in-grenada.html", "0.8", "monthly"),
        ("grenada-faq.html", "0.7", "monthly"),
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority, freq in urls:
        url = f"{DOMAIN}/{loc}" if loc else f"{DOMAIN}/"
        lines += [
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{DATE}</lastmod>",
            f"    <changefreq>{freq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    write("sitemap.xml", "\n".join(lines) + "\n")

    write(
        "package.json",
        """{
  "name": "grenada-shore-excursion",
  "private": true,
  "scripts": {
    "build": "python3 scripts/build-grenada-site.py",
    "images": "python3 scripts/fetch-grenada-images.py",
    "deploy": "wrangler deploy",
    "preview": "python3 -m http.server 8910"
  },
  "devDependencies": {
    "wrangler": "^4.94.0"
  }
}
""",
    )

    write(
        "wrangler.jsonc",
        """{
  "$schema": "node_modules/wrangler/config-schema.json",
  "name": "grenada-shore-excursion",
  "compatibility_date": "2026-06-06",
  "observability": { "enabled": true },
  "assets": { "directory": "." },
  "routes": [
    {
      "pattern": "grenadashoreexcursion.com",
      "custom_domain": true
    }
  ]
}
""",
    )

    write(
        "deploy.sh",
        f"""#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying {SITE} to Cloudflare..."
npx wrangler deploy

echo "Done. Check {DOMAIN}/ shortly."
""",
    )

    (ROOT / "deploy.sh").chmod(0o755)

    write(
        "images/ATTRIBUTION.md",
        """# Image attribution

Hero and content images may be sourced from Unsplash (Unsplash License) via `npm run images`.

Replace placeholder images with your own Grenada photography where noted in `scripts/fetch-grenada-images.py` (`CUSTOM_IMAGES`).
""",
    )

    images_dir = ROOT / "images"
    images_dir.mkdir(exist_ok=True)
    placeholders = [
        HOME_HERO,
        BEST_IMG,
        PORT_IMG,
        ONE_DAY_IMG,
        GRAND_ANSE_IMG,
        WATERFALL_IMG,
        SPICE_IMG,
        RAINFOREST_IMG,
        CHOC_RUM_IMG,
        ISLAND_IMG,
        SNORKEL_IMG,
        PRIVATE_IMG,
        FAMILY_IMG,
        BEACHES_IMG,
        FAQ_IMG,
        INTRO_IMG,
    ]
    for img in placeholders:
        p = ROOT / img
        if p.exists() and p.stat().st_size > 5000:
            continue
        if not p.exists() or p.stat().st_size <= 5000:
            p.write_bytes(
                b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
                b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
                b"\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n"
                b"\xdb\x00\x00\x00\x00IEND\xaeB`\x82"
            )

    print("Done.")


if __name__ == "__main__":
    main()
