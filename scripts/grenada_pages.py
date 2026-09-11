"""Grenada Shore Excursion — Phase 16B page content modules.

Each public page function returns:
  (hero_html, main_html, faq_list_or_None, meta)

meta keys: title, description, canonical_path, page_id, og_image
faq_list: list[tuple[str, str]] | None
"""
from __future__ import annotations

from html import escape

from grenada_config import (
    ACCENT,
    APEX,
    EMAIL,
    INTRO,
    INTRO_ALT,
    RAINFOREST,
    RAINFOREST_ALT,
    SITE,
    WATERFALLS,
    WATERFALLS_ALT,
)
from grenada_shell import (
    cruise_snapshot,
    faq_section,
    hero_band,
    related_links,
)

from typing import Any, Dict, List, Optional, Tuple

Meta = Dict[str, Any]
FaqList = List[Tuple[str, str]]
PageTuple = Tuple[str, str, Optional[FaqList], Meta]


def _cta(primary_href: str, primary_label: str, secondary_href: str = "", secondary_label: str = "") -> str:
    parts = [
        f'<a href="{primary_href}" class="btn-primary inline-flex items-center justify-center gap-2 '
        f'text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{primary_label}</a>'
    ]
    if secondary_href:
        parts.append(
            f'<a href="{secondary_href}" class="btn-outline inline-flex items-center justify-center gap-2 '
            f'text-white font-semibold px-7 py-3 rounded-full text-sm">{secondary_label}</a>'
        )
    return "".join(parts)


def _section(inner: str, *, bg: str = "bg-white", pad: str = "pt-8 pb-12") -> str:
    return f'<section class="{pad} {bg}"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">{inner}</div></section>\n'


def _prose(inner: str, *, bg: str = "bg-white", narrow: bool = True) -> str:
    wrap = "max-w-3xl" if narrow else "max-w-7xl"
    return (
        f'<section class="py-14 {bg}"><div class="{wrap} mx-auto px-4 sm:px-6 lg:px-8">'
        f"{inner}</div></section>\n"
    )


def _card(
    href: str,
    title: str,
    blurb: str,
    *,
    image: str | None = None,
    alt: str = "",
    cta: str = "Read more →",
    media_label: str = "",
) -> str:
    if image:
        media = (
            f'<div class="card-media h-36">'
            f'<img src="{image}" alt="{escape(alt)}" width="600" height="288" '
            f'loading="lazy" decoding="async" /></div>'
        )
    else:
        label = media_label or title
        media = (
            f'<div class="card-media h-36 bg-ocean-800 flex items-center justify-center '
            f'text-white/80 text-sm px-4 text-center">{escape(label)}</div>'
        )
    return f"""<a href="{href}" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
  {media}
  <div class="p-5 flex flex-col flex-1">
    <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">{title}</h3>
    <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">{blurb}</p>
    <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">{cta}</span>
  </div>
</a>"""


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------


def home() -> PageTuple:
    hero = hero_band(
        eyebrow="Grenada · St George's cruise port",
        title_html=(
            f'Grenada Shore <br/><span class="{ACCENT}">Excursions</span> '
            "for Cruise Passengers"
        ),
        lead=(
            "A practical guide to what fits a St George's call: Grand Anse beach time, "
            "spice and island loops, waterfall or rainforest interiors, snorkelling, "
            "or a private plan matched to your group's pace."
        ),
        image=INTRO,
        aria_label=INTRO_ALT,
        actions=_cta(
            "/best-grenada-shore-excursions",
            "Compare day styles",
            "/grenada-cruise-port-guide",
            "Read the port guide",
        ),
        tags=["Grand Anse", "Spice Island", "Waterfalls", "Grand Etang"],
    )

    snap = cruise_snapshot(
        [
            ("Typical time ashore", "Often several hours — confirm your ship"),
            ("Near-port strengths", "St George's / Carenage orientation; Grand Anse needs a transfer"),
            ("Inland options", "Waterfalls, spice stops, Grand Etang rainforest"),
            ("Activity level", "Varies by theme — beach low; falls and trails moderate"),
            ("Return window", "Leave margin before all-aboard; confirm operator policy"),
            ("This site", "Editorial planning — no booking checkout here"),
        ],
        label="Grenada cruise passenger snapshot",
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
  <div>
    <div class="section-label">St George's cruise port</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 leading-snug mb-5">
      What Grenada is <br/> <span class="text-ocean-600">actually good for</span>
    </h2>
    <p class="text-gray-600 leading-relaxed mb-5">
      Cruise ships generally dock at <strong>St George's</strong>, with passenger orientation
      around the <strong>Melville Street / Carenage</strong> harbour area — treat that as typical,
      not a guarantee for every call. The waterfront and hillside town reward a short walk;
      <a href="/grand-anse-beach-excursions" class="text-ocean-600 font-medium">Grand Anse</a>
      is the island's signature beach day and usually needs a taxi or organised transfer.
    </p>
    <p class="text-gray-600 leading-relaxed mb-8">
      Eastern Caribbean dollars are official; USD is commonly accepted at tourist-facing points.
      Use this site to pick a coherent theme for the day, then confirm live ship times independently.
      You can request <a href="/book/grenadas-spice-route" class="text-ocean-600 font-medium">Grenada's Spice Route</a>
      online when a spice-focused half-day fits your call.
    </p>
    <p class="flex flex-wrap gap-3 mb-2">
      <a href="/best-grenada-shore-excursions" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">
        Explore decision groups
      </a>
      <a href="/book/grenadas-spice-route" class="inline-flex items-center justify-center font-semibold px-7 py-3.5 rounded-full text-sm border border-ocean-200 text-ocean-700">
        Book Spice Route
      </a>
    </p>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{INTRO}" alt="{escape(INTRO_ALT)}" width="800" height="600" loading="eager" decoding="async" />
  </div>
</div>
''')}
{_section(f'''
<div class="text-center mb-12">
  <div class="section-label justify-center">Decision spine</div>
  <h2 class="text-3xl font-display font-bold text-gray-900">Six useful starting points</h2>
  <p class="mt-4 text-gray-500 max-w-2xl mx-auto">Pick the page that matches your question — not a ranking of “bestsellers”.</p>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
  {_card("/best-beaches-in-grenada", "Beach", "Compare Grand Anse and nearby beach names for a calm swim-focused call.", media_label="Beach day", cta="Beach guide →")}
  {_card("/grenada-spice-island-tours", "Spice / island", "Nutmeg, plantations and west-coast style loops — often combined with scenic inland stops.", image=INTRO, alt=INTRO_ALT, cta="Spice guide →")}
  {_card("/grenada-waterfall-tours", "Waterfall / rainforest", "Annandale and longer-drive falls, or Grand Etang cooler elevation — check duration for your call.", image=WATERFALLS, alt=WATERFALLS_ALT, cta="Waterfall guide →")}
  {_card("/grenada-snorkelling-tours", "Snorkelling", "Molinere / Underwater Sculpture Park context and reef choices — sea conditions matter.", media_label="Snorkel day", cta="Snorkel guide →")}
  {_card("/grenada-private-tours", "Private", "Custom pacing when mobility, ages or timing differ within one group.", media_label="Private plan", cta="Private guide →")}
  {_card("/one-day-in-grenada", "One-day planning", "Short-call vs fuller-day shapes — beach morning or inland theme, with return planning.", image=INTRO, alt=INTRO_ALT, cta="One-day guide →")}
</div>
''', bg="bg-pr-50", pad="py-16")}
{_section(f'''
<div class="text-center mb-10">
  <div class="section-label justify-center">Equity routes</div>
  <h2 class="text-2xl font-display font-bold text-gray-900">All planning guides</h2>
</div>
<div class="flex flex-wrap justify-center gap-3 text-sm">
  <a href="/best-grenada-shore-excursions" class="text-ocean-600 font-medium hover:text-ocean-800">Excursions hub</a>
  <span class="text-gray-300">·</span>
  <a href="/grenada-cruise-port-guide" class="text-ocean-600 font-medium hover:text-ocean-800">Port guide</a>
  <span class="text-gray-300">·</span>
  <a href="/grand-anse-beach-excursions" class="text-ocean-600 font-medium hover:text-ocean-800">Grand Anse</a>
  <span class="text-gray-300">·</span>
  <a href="/grenada-rainforest-tours" class="text-ocean-600 font-medium hover:text-ocean-800">Rainforest</a>
  <span class="text-gray-300">·</span>
  <a href="/grenada-chocolate-rum-tours" class="text-ocean-600 font-medium hover:text-ocean-800">Chocolate &amp; rum</a>
  <span class="text-gray-300">·</span>
  <a href="/grenada-island-sightseeing-tours" class="text-ocean-600 font-medium hover:text-ocean-800">Island sightseeing</a>
  <span class="text-gray-300">·</span>
  <a href="/grenada-family-excursions" class="text-ocean-600 font-medium hover:text-ocean-800">Family</a>
  <span class="text-gray-300">·</span>
  <a href="/grenada-faq" class="text-ocean-600 font-medium hover:text-ocean-800">FAQ</a>
</div>
''', pad="pb-8 pt-4")}
{_section(snap + related_links([
    ("/grenada-cruise-port-guide", "Port guide"),
    ("/one-day-in-grenada", "One day ashore"),
    ("/best-grenada-shore-excursions", "Excursion styles"),
    ("/contact", "Contact"),
]), pad="pb-16 pt-4")}
{faq_section([
    (
        "Where do cruise ships call in Grenada?",
        "Ships generally dock at St George's, with passenger orientation around the Melville Street / "
        "Carenage harbour area. Confirm berth notes for your sailing — arrangements can vary.",
    ),
    (
        "How long do ships usually stay?",
        "Typical Grenada calls often run several hours ashore. Always confirm gangway and all-aboard "
        "times on your sailing — schedules vary by ship and season.",
    ),
    (
        "Is Grand Anse walkable from the pier?",
        "Treat Grand Anse as a short taxi or organised transfer from the St George's port area, not a "
        "casual waterfront stroll. Plan time both ways and leave margin before all-aboard.",
    ),
    (
        "Do you sell tours on this site?",
        "No. This is an independent editorial planning guide. Use the contact page for questions about "
        "the guide itself — we do not process bookings or payments here.",
    ),
], heading="Grenada shore day FAQ")}
"""

    faqs: FaqList = [
        (
            "Where do cruise ships call in Grenada?",
            "Ships generally dock at St George's, with passenger orientation around the Melville Street / "
            "Carenage harbour area. Confirm berth notes for your sailing — arrangements can vary.",
        ),
        (
            "How long do ships usually stay?",
            "Typical Grenada calls often run several hours ashore. Always confirm gangway and all-aboard "
            "times on your sailing — schedules vary by ship and season.",
        ),
        (
            "Is Grand Anse walkable from the pier?",
            "Treat Grand Anse as a short taxi or organised transfer from the St George's port area, not a "
            "casual waterfront stroll. Plan time both ways and leave margin before all-aboard.",
        ),
        (
            "Do you sell tours on this site?",
            "No. This is an independent editorial planning guide. Use the contact page for questions about "
            "the guide itself — we do not process bookings or payments here.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Shore Excursion | Cruise Passenger Planning Guide",
        "description": (
            "Plan Grenada shore excursions from St George's — Grand Anse beach, spice tours, "
            "waterfalls, rainforest, snorkelling and realistic one-day cruise planning."
        ),
        "canonical_path": "/",
        "page_id": "home",
        "og_image": INTRO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# BEST EXCURSIONS (hub)
# ---------------------------------------------------------------------------


def best_excursions() -> PageTuple:
    hero = hero_band(
        eyebrow="Decision hub",
        title_html=f'Compare Grenada <br/> <span class="{ACCENT}">shore day styles</span>',
        lead=(
            "Beach, waterfall, spice, rainforest, chocolate and rum, snorkelling, "
            "and private pacing — grouped by how they fit a cruise call, "
            "not by invented popularity rankings."
        ),
        image=None,
        aria_label="Grenada shore excursion comparison for cruise passengers",
        css_only=True,
        breadcrumb="Excursions",
        actions=_cta(
            "/grenada-cruise-port-guide",
            "Port logistics first",
            "/one-day-in-grenada",
            "One-day scenarios",
        ),
    )

    snap = cruise_snapshot(
        [
            ("How to use this page", "Choose a style, then open the matching guide"),
            ("Beach focus", "Grand Anse — transfer from St George's port area"),
            ("Inland themes", "Waterfalls, spice, Grand Etang rainforest"),
            ("Water days", "Snorkel styles — confirm sea conditions and duration"),
            ("Request option", "Grenada's Spice Route — book from the spice guide"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Grenada shore days become clearer once you decide how far you are willing to travel from
  St George's and how active you want the afternoon. Stay closer for a calm beach day at Grand Anse;
  commit more road time for waterfalls, spice estates or Grand Etang. Mixing every highlight on a
  short call usually produces rushed photography and a tense return window.
</p>
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Prefer a guided spice half-day from the pier?
  <a href="/book/grenadas-spice-route" class="text-ocean-600 font-semibold">Request Grenada's Spice Route</a>
  online — payment creates a booking request; confirmation follows separately.
</p>
''' + snap)}
{_section('''
<div class="overflow-x-auto rounded-3xl border border-ocean-100 shadow-sm mb-12">
  <table class="w-full text-sm text-left min-w-[720px]">
    <thead class="bg-ocean-800 text-white">
      <tr>
        <th class="py-4 px-4 font-semibold rounded-tl-3xl">Day style</th>
        <th class="py-4 px-3 font-semibold">Role on a cruise call</th>
        <th class="py-4 px-3 font-semibold">Activity feel</th>
        <th class="py-4 px-4 font-semibold rounded-tr-3xl">Guide</th>
      </tr>
    </thead>
    <tbody class="bg-white">
      <tr class="border-b border-ocean-50">
        <td class="py-4 px-4 font-semibold text-gray-900">Beach</td>
        <td class="py-4 px-3 text-gray-600">Calm swim and sand time; Grand Anse is the primary cruise beach</td>
        <td class="py-4 px-3 text-gray-600">Low</td>
        <td class="py-4 px-4"><a href="/best-beaches-in-grenada" class="text-ocean-600 font-medium">Beaches →</a></td>
      </tr>
      <tr class="border-b border-ocean-50">
        <td class="py-4 px-4 font-semibold text-gray-900">Waterfall</td>
        <td class="py-4 px-3 text-gray-600">Rainforest pools and wet paths; Annandale often nearer, longer drives for farther falls</td>
        <td class="py-4 px-3 text-gray-600">Moderate</td>
        <td class="py-4 px-4"><a href="/grenada-waterfall-tours" class="text-ocean-600 font-medium">Waterfalls →</a></td>
      </tr>
      <tr class="border-b border-ocean-50">
        <td class="py-4 px-4 font-semibold text-gray-900">Spice</td>
        <td class="py-4 px-3 text-gray-600">Nutmeg and plantation storytelling; often paired with scenic west-coast or inland loops</td>
        <td class="py-4 px-3 text-gray-600">Low–moderate</td>
        <td class="py-4 px-4"><a href="/grenada-spice-island-tours" class="text-ocean-600 font-medium">Spice →</a></td>
      </tr>
      <tr class="border-b border-ocean-50">
        <td class="py-4 px-4 font-semibold text-gray-900">Rainforest</td>
        <td class="py-4 px-3 text-gray-600">Grand Etang crater-lake context and cooler elevation — not a beach substitute</td>
        <td class="py-4 px-3 text-gray-600">Moderate</td>
        <td class="py-4 px-4"><a href="/grenada-rainforest-tours" class="text-ocean-600 font-medium">Rainforest →</a></td>
      </tr>
      <tr class="border-b border-ocean-50">
        <td class="py-4 px-4 font-semibold text-gray-900">Chocolate &amp; rum</td>
        <td class="py-4 px-3 text-gray-600">Calmer cultural tasting day — verify inclusions with the operator</td>
        <td class="py-4 px-3 text-gray-600">Low</td>
        <td class="py-4 px-4"><a href="/grenada-chocolate-rum-tours" class="text-ocean-600 font-medium">Chocolate &amp; rum →</a></td>
      </tr>
      <tr class="border-b border-ocean-50">
        <td class="py-4 px-4 font-semibold text-gray-900">Snorkel</td>
        <td class="py-4 px-3 text-gray-600">Reef or sculpture-park style water time — conditions and transfers matter</td>
        <td class="py-4 px-3 text-gray-600">Low–moderate</td>
        <td class="py-4 px-4"><a href="/grenada-snorkelling-tours" class="text-ocean-600 font-medium">Snorkelling →</a></td>
      </tr>
      <tr>
        <td class="py-4 px-4 font-semibold text-gray-900">Private</td>
        <td class="py-4 px-3 text-gray-600">Custom mix when ages, mobility or timing differ — confirm return time in writing</td>
        <td class="py-4 px-3 text-gray-600">As agreed</td>
        <td class="py-4 px-4"><a href="/grenada-private-tours" class="text-ocean-600 font-medium">Private →</a></td>
      </tr>
    </tbody>
  </table>
</div>
<div class="mb-10">
  <div class="section-label">Beach</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Calm water time near the south-west coast</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Beach days suit shorter calls, mixed groups and anyone who wants swimming ahead of inland roads.
    Start with the beach comparison, then open the Grand Anse cruise page for transfer framing and return planning.
  </p>
  <p class="space-x-4">
    <a href="/best-beaches-in-grenada" class="text-ocean-600 font-semibold">Best beaches →</a>
    <a href="/grand-anse-beach-excursions" class="text-ocean-600 font-semibold">Grand Anse cruise page →</a>
  </p>
</div>
<div class="mb-10">
  <div class="section-label">Inland</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Waterfalls, spice and rainforest without stacking all three</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Inland themes share road time from St George's. Pick one primary story — falls, spice estates,
    or Grand Etang elevation — then protect the return window rather than adding “just one more stop”.
  </p>
  <p class="space-x-4">
    <a href="/grenada-waterfall-tours" class="text-ocean-600 font-semibold">Waterfalls →</a>
    <a href="/grenada-spice-island-tours" class="text-ocean-600 font-semibold">Spice Island →</a>
    <a href="/grenada-rainforest-tours" class="text-ocean-600 font-semibold">Rainforest →</a>
  </p>
</div>
<div class="mb-10">
  <div class="section-label">Culture &amp; water</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Tastings, snorkel and island overview</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Chocolate and rum days stay calmer when inclusions are clear. Snorkel days depend on sea conditions
    and departure logistics. Island sightseeing covers Carenage, viewpoints and an optional beach stop
    without duplicating the spice guide.
  </p>
  <p class="space-x-4">
    <a href="/grenada-chocolate-rum-tours" class="text-ocean-600 font-semibold">Chocolate &amp; rum →</a>
    <a href="/grenada-snorkelling-tours" class="text-ocean-600 font-semibold">Snorkelling →</a>
    <a href="/grenada-island-sightseeing-tours" class="text-ocean-600 font-semibold">Island sightseeing →</a>
  </p>
</div>
<div class="mb-4">
  <div class="section-label">Private &amp; family</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">When the group needs a custom pace</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Private plans help when mobility, ages or timing differ. Family days usually favour calm beach time,
    gentler waterfall walks and age-appropriate snorkel choices.
  </p>
  <p class="space-x-4">
    <a href="/grenada-private-tours" class="text-ocean-600 font-semibold">Private tours →</a>
    <a href="/grenada-family-excursions" class="text-ocean-600 font-semibold">Family →</a>
  </p>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  These pages are planning guides. Booking is not offered on this website — if you arrange
  anything independently, confirm inclusions, pickup logistics and timing with the operator and
  your cruise line before you travel. Leave margin before all-aboard.
</p>
''' + related_links([
    ("/one-day-in-grenada", "One day scenarios"),
    ("/grenada-cruise-port-guide", "Port guide"),
    ("/grenada-faq", "FAQ"),
    ("/contact", "Contact"),
]), bg="bg-white")}
{faq_section([
    (
        "How should I choose between beach and inland?",
        "Choose beach for lower transfer complexity and swimming priority. Choose waterfall, spice or "
        "rainforest when you accept inland road time and still leave a conservative return window.",
    ),
    (
        "Do you sell tours here?",
        "No. This is an independent planning guide. Use /contact for editorial questions only.",
    ),
    (
        "Is there one best Grenada excursion?",
        "No single product fits every ship schedule. Match beach, inland, snorkel or private pacing to "
        "your call length and group energy, then stop adding stops.",
    ),
], heading="Comparing Grenada day styles")}
"""

    faqs: FaqList = [
        (
            "How should I choose between beach and inland?",
            "Choose beach for lower transfer complexity and swimming priority. Choose waterfall, spice or "
            "rainforest when you accept inland road time and still leave a conservative return window.",
        ),
        (
            "Do you sell tours here?",
            "You can request Grenada's Spice Route online from the spice guide. Other pages remain "
            "editorial planning guides. Use /contact for general questions.",
        ),
        (
            "Is there one best Grenada excursion?",
            "No single product fits every ship schedule. Match beach, inland, snorkel or private pacing to "
            "your call length and group energy, then stop adding stops.",
        ),
    ]

    meta: Meta = {
        "title": "Best Grenada Shore Excursions | Compare Cruise Day Styles",
        "description": (
            "Compare Grenada cruise excursion styles from St George's — beach, waterfall, spice, "
            "rainforest, chocolate and rum, snorkelling and private options."
        ),
        "canonical_path": "/best-grenada-shore-excursions",
        "page_id": "excursions",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# PORT GUIDE
# ---------------------------------------------------------------------------


def port_guide() -> PageTuple:
    hero = hero_band(
        eyebrow="Port logistics",
        title_html=f'Grenada <br/> <span class="{ACCENT}">cruise port guide</span>',
        lead=(
            "What cruise passengers should know about St George's, the Carenage area, "
            "near-port walking, transfers toward Grand Anse, and practical planning notes "
            "without invented fares."
        ),
        image=INTRO,
        aria_label=INTRO_ALT,
        breadcrumb="Port guide",
        actions=_cta(
            "/best-grenada-shore-excursions",
            "Compare day styles",
            "/one-day-in-grenada",
            "One day ashore",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Port area", "St George's — Melville Street / Carenage orientation (typical)"),
            ("Typical call", "Often several hours — confirm your ship"),
            ("Near-port", "Carenage and hillside town walking"),
            ("Grand Anse", "Usually needs a short taxi or organised transfer"),
            ("Currency", "XCD official; USD commonly accepted at tourist points"),
            ("Return planning", "Leave margin; traffic and queues vary"),
        ]
    )

    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Grenada's main cruise gateway is <strong>St George's</strong>. Ships generally dock with
  passenger orientation around the <strong>Melville Street / Carenage</strong> harbour area —
  treat that as typical guidance for planning, not a guarantee that every sailing uses the same berth or
  gangway arrangement. Confirm your ship's port notes for the call.
</p>
''' + snap)}
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Near the pier</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Walkability around the Carenage</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      The harbour-front Carenage and the colourful hillside town reward an unhurried walk: shops,
      viewpoints and a sense of place without committing to a long inland road day. Keep valuables
      organised, watch for traffic on narrow streets, and leave time to re-enter the terminal area.
    </p>
    <p class="text-gray-600 leading-relaxed">
      For harbour views and fort lookouts as part of a broader loop, see the
      <a href="/grenada-island-sightseeing-tours" class="text-ocean-600 font-medium">island sightseeing</a> guide.
    </p>
  </div>
  <div>
    <div class="section-label">Further out</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Grand Anse needs transport</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      <strong>Grand Anse</strong> is typically a short taxi or organised transfer from the St George's
      port area. We do not publish fares — rates and vehicle types change. Agree the return pickup
      clearly, and leave margin before all-aboard rather than assuming a perfect traffic day.
    </p>
    <p class="text-gray-600 leading-relaxed">
      Read the dedicated
      <a href="/grand-anse-beach-excursions" class="text-ocean-600 font-medium">Grand Anse cruise page</a>
      and the
      <a href="/best-beaches-in-grenada" class="text-ocean-600 font-medium">beach comparison</a>
      before stacking inland stops onto a beach morning.
    </p>
  </div>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Currency and practical notes</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Eastern Caribbean dollars (XCD) are official. US dollars are commonly accepted at tourist-facing
  points, though change may be given in local currency. Carry small notes for taxis and tips where
  appropriate, and confirm payment expectations with any operator before you depart.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Ship-sold tours and independent arrangements both have trade-offs. Ship products can feel simpler
  on timing; independent plans may offer more flexibility — at the cost of your own return discipline.
  Neither approach is “always safer” in absolute terms; match the method to your group and call length.
</p>
''' + related_links([
    ("/one-day-in-grenada", "One day ashore"),
    ("/best-grenada-shore-excursions", "Excursion styles"),
    ("/grenada-faq", "FAQ"),
    ("/contact", "Contact"),
]))}
{faq_section([
    (
        "Can I walk to Grand Anse from the cruise pier?",
        "Plan on a taxi or organised transfer rather than treating Grand Anse as a waterfront stroll "
        "from St George's. Build time both ways and leave margin before all-aboard.",
    ),
    (
        "What currency should I bring?",
        "XCD is official; USD is commonly accepted at many tourist-facing businesses. Confirm with "
        "taxis and operators, and avoid relying on a single payment method.",
    ),
    (
        "Should I book through the ship?",
        "Ship tours and independent plans both have trade-offs on timing confidence, group needs and "
        "provider reputation. We do not sell either — decide based on your sailing and risk tolerance.",
    ),
], heading="Port guide FAQ")}
"""

    faqs: FaqList = [
        (
            "Can I walk to Grand Anse from the cruise pier?",
            "Plan on a taxi or organised transfer rather than treating Grand Anse as a waterfront stroll "
            "from St George's. Build time both ways and leave margin before all-aboard.",
        ),
        (
            "What currency should I bring?",
            "XCD is official; USD is commonly accepted at many tourist-facing businesses. Confirm with "
            "taxis and operators, and avoid relying on a single payment method.",
        ),
        (
            "Should I book through the ship?",
            "Ship tours and independent plans both have trade-offs on timing confidence, group needs and "
            "provider reputation. We do not sell either — decide based on your sailing and risk tolerance.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Cruise Port Guide | St George's for Passengers",
        "description": (
            "Practical St George's cruise port guidance — Carenage walkability, Grand Anse transfers, "
            "currency notes and return planning for Grenada shore days."
        ),
        "canonical_path": "/grenada-cruise-port-guide",
        "page_id": "port",
        "og_image": INTRO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# ONE DAY
# ---------------------------------------------------------------------------


def one_day() -> PageTuple:
    hero = hero_band(
        eyebrow="Port-day planning",
        title_html=f'One day in <br/> <span class="{ACCENT}">Grenada</span>',
        lead=(
            "Practical shortlists for a St George's call: beach morning or inland "
            "waterfall and spice themes, short-call versus fuller-day shapes, and "
            "honest return planning — without treating sample timelines as ship schedules."
        ),
        image=INTRO,
        aria_label=INTRO_ALT,
        breadcrumb="One day",
        actions=_cta(
            "/best-grenada-shore-excursions",
            "Compare styles",
            "/grenada-cruise-port-guide",
            "Port guide",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Short call", "One theme — beach or a compact inland loop"),
            ("Fuller day", "Still protect return margin; avoid stacking everything"),
            ("Beach path", "Grand Anse morning; optional light town time"),
            ("Inland path", "Waterfall or spice/rainforest — check duration"),
            ("Timeline below", "Illustrative only — not a schedule fact"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  A Grenada cruise day works best when you pick <strong>one primary story</strong>: calm beach time
  at Grand Anse, or an inland theme built around waterfalls, spice estates or Grand Etang.
  Trying to “do the island” on a short call usually costs your buffer before all-aboard.
</p>
''' + snap)}
{_section('''
<div class="grid md:grid-cols-2 gap-10 mb-12">
  <div>
    <div class="section-label">Beach-forward</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Morning swim, protected afternoon</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Transfer to Grand Anse, swim and rest, then return with margin. Pairing a long inland waterfall
      stop onto the same morning only makes sense on a fuller call — and still needs written timing
      discipline if you use an operator.
    </p>
    <a href="/grand-anse-beach-excursions" class="text-ocean-600 font-semibold">Grand Anse cruise page →</a>
  </div>
  <div>
    <div class="section-label">Inland-forward</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Falls, spice or rainforest</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Choose Annandale-style nearer falls for tighter clocks, or confirm duration carefully for
      Concord / Seven Sisters style longer drives. Spice and Grand Etang loops share road time —
      pick the story you care about most.
    </p>
    <p class="space-x-3">
      <a href="/grenada-waterfall-tours" class="text-ocean-600 font-semibold">Waterfalls →</a>
      <a href="/grenada-spice-island-tours" class="text-ocean-600 font-semibold">Spice →</a>
    </p>
  </div>
</div>
<div class="rounded-3xl border border-ocean-100 bg-white p-6 sm:p-8">
  <div class="section-label">Illustrative only</div>
  <h2 class="text-2xl font-display font-bold text-gray-900 mb-3">Sample timeline shape</h2>
  <p class="text-sm text-gray-500 mb-6">
    This is a planning sketch, not a published ship schedule or operator itinerary. Replace every
    time with your sailing’s gangway and all-aboard notices.
  </p>
  <ol class="space-y-3 text-gray-600 leading-relaxed list-decimal list-inside">
    <li>Disembark and clear the pier area without rushing into the furthest option first.</li>
    <li>Commit to beach <em>or</em> inland theme; confirm return pickup or self-timed transport.</li>
    <li>Build a mid-day check: are you still on track for the buffer you planned?</li>
    <li>Leave the last activity with margin — traffic, queues and photo stops compress easily.</li>
    <li>Re-enter the terminal area calmly; do not treat “almost enough time” as enough.</li>
  </ol>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  Short calls favour one low-complexity theme. Fuller days still benefit from saying no to the
  third stop. Confirm operator return policy in writing before you pay, and leave margin before
  all-aboard rather than relying on optimistic road times.
</p>
''' + related_links([
    ("/best-beaches-in-grenada", "Best beaches"),
    ("/grenada-waterfall-tours", "Waterfalls"),
    ("/grenada-private-tours", "Private pacing"),
    ("/grenada-faq", "FAQ"),
]))}
{faq_section([
    (
        "Can I do Grand Anse and a waterfall on the same call?",
        "Sometimes on a fuller day with disciplined timing — often not on a short call. Treat dual "
        "themes as a stretch plan and protect the return window first.",
    ),
    (
        "What if my ship’s hours change?",
        "Rebuild the day around the new all-aboard time. Drop the furthest stop rather than compressing "
        "every segment. Confirm any operator change policy promptly.",
    ),
], heading="One-day FAQ")}
"""

    faqs: FaqList = [
        (
            "Can I do Grand Anse and a waterfall on the same call?",
            "Sometimes on a fuller day with disciplined timing — often not on a short call. Treat dual "
            "themes as a stretch plan and protect the return window first.",
        ),
        (
            "What if my ship’s hours change?",
            "Rebuild the day around the new all-aboard time. Drop the furthest stop rather than compressing "
            "every segment. Confirm any operator change policy promptly.",
        ),
    ]

    meta: Meta = {
        "title": "One Day in Grenada from a Cruise Ship | Practical Shortlist",
        "description": (
            "Plan one day in Grenada from St George's — beach morning or inland waterfall and spice "
            "themes, short-call vs fuller-day shapes, and return planning."
        ),
        "canonical_path": "/one-day-in-grenada",
        "page_id": "one-day",
        "og_image": INTRO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# GRAND ANSE
# ---------------------------------------------------------------------------


def grand_anse() -> PageTuple:
    hero = hero_band(
        eyebrow="Beach day · cruise focus",
        title_html=f'Grand Anse <br/> <span class="{ACCENT}">beach excursions</span>',
        lead=(
            "A practical cruise page for Grenada’s signature beach day: transfer framing "
            "from St George's, calm swim use-cases, and when not to stack inland stops — "
            "not a beach comparison guide."
        ),
        image=None,
        aria_label="Grand Anse beach day planning for Grenada cruise passengers",
        css_only=True,
        breadcrumb="Grand Anse",
        actions=_cta(
            "/best-beaches-in-grenada",
            "Compare beaches",
            "/one-day-in-grenada",
            "One-day planning",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Role", "Primary calm beach day from a St George's call"),
            ("Transfer", "Typically a short taxi/transfer from the port area — no fare quoted here"),
            ("Best use", "Swim, sand time, low activity for mixed groups"),
            ("Pairing", "Inland only if time genuinely allows"),
            ("Return", "Agree pickup; leave margin before all-aboard"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  <strong>Grand Anse</strong> is the beach most cruise passengers mean when they want a classic
  Grenada swim day: a long stretch of sand and generally calm water for an unhurried few hours.
  This page is the practical cruise brief. For how Grand Anse sits beside other beach names,
  use the <a href="/best-beaches-in-grenada" class="text-ocean-600 font-medium">best beaches comparison</a>.
</p>
''' + snap)}
{_section('''
<div class="grid lg:grid-cols-2 gap-12">
  <div>
    <div class="section-label">From the pier</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Transfer, not a waterfront stroll</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Grand Anse is typically a short taxi or organised transfer from the St George's port area.
      We do not invent fares or chair prices — agree transport and any beach facilities with your
      driver or operator on the day, and confirm how you will return.
    </p>
    <p class="text-gray-600 leading-relaxed">
      Port orientation around the Carenage is useful context; see the
      <a href="/grenada-cruise-port-guide" class="text-ocean-600 font-medium">cruise port guide</a>.
    </p>
  </div>
  <div>
    <div class="section-label">Use-case</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Calm beach day, protected clock</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Grand Anse suits mixed ages, lower activity levels and anyone who wants swimming ahead of
      rainforest roads. Pair with a waterfall or spice stop only when your call length and energy
      clearly allow it — otherwise keep the day simple and leave margin before all-aboard.
    </p>
    <p class="text-gray-600 leading-relaxed">
      Confirm operator return policy before you pay. Traffic and pier queues are ordinary risks,
      not rare exceptions.
    </p>
  </div>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  Facilities, chair hire and dining change by season and operator. Treat anything you hear on the pier
  as a starting point to verify, not a fixed price list. This site stays editorial and does not sell
  beach packages.
</p>
''' + related_links([
    ("/best-beaches-in-grenada", "Best beaches comparison"),
    ("/one-day-in-grenada", "One day ashore"),
    ("/grenada-family-excursions", "Family notes"),
    ("/grenada-faq", "FAQ"),
]))}
{faq_section([
    (
        "How far is Grand Anse from the cruise port?",
        "Treat it as a typically short taxi or organised transfer from the St George's port area. "
        "Exact minutes vary with traffic; we do not publish fares.",
    ),
    (
        "Should I combine Grand Anse with a waterfall?",
        "Only when you have a fuller call and a clear return plan. On shorter calls, a dedicated beach "
        "day is usually the lower-stress choice.",
    ),
], heading="Grand Anse FAQ")}
"""

    faqs: FaqList = [
        (
            "How far is Grand Anse from the cruise port?",
            "Treat it as a typically short taxi or organised transfer from the St George's port area. "
            "Exact minutes vary with traffic; we do not publish fares.",
        ),
        (
            "Should I combine Grand Anse with a waterfall?",
            "Only when you have a fuller call and a clear return plan. On shorter calls, a dedicated beach "
            "day is usually the lower-stress choice.",
        ),
    ]

    meta: Meta = {
        "title": "Grand Anse Beach Excursions | Grenada Cruise Day Guide",
        "description": (
            "Plan a Grand Anse beach day from St George's cruise port — transfer framing, calm swim "
            "use-cases and return planning for Grenada passengers."
        ),
        "canonical_path": "/grand-anse-beach-excursions",
        "page_id": "grand-anse",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# BEST BEACHES (SEO priority)
# ---------------------------------------------------------------------------


def beaches() -> PageTuple:
    hero = hero_band(
        eyebrow="Decision guide · beaches",
        title_html=f'Best beaches in <br/> <span class="{ACCENT}">Grenada</span>',
        lead=(
            "A cruise-passenger comparison for Grenada beach choices: Grand Anse as the "
            "primary swim day, careful notes on nearby names often discussed by visitors, "
            "and clear links to the dedicated Grand Anse cruise page."
        ),
        image=None,
        aria_label="Best beaches in Grenada for cruise passengers comparison",
        css_only=True,
        breadcrumb="Beaches",
        actions=_cta(
            "/grand-anse-beach-excursions",
            "Grand Anse cruise page",
            "/one-day-in-grenada",
            "One-day planning",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Primary pick", "Grand Anse for most cruise swim days"),
            ("This page’s job", "Compare / decide — not a facilities catalogue"),
            ("Nearby names", "Morne Rouge / Magazine often discussed by visitors"),
            ("Transfer", "Beach time from St George's usually needs transport"),
            ("Next step", "Open the Grand Anse cruise page for practical timing"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  If you are choosing a <strong>beach-focused shore day</strong> from St George's, start here.
  This is the comparison and decision page. The
  <a href="/grand-anse-beach-excursions" class="text-ocean-600 font-medium">Grand Anse excursions</a>
  page covers transfer framing, calm-day use-cases and return planning for that specific beach.
</p>
''' + snap)}
{_section('''
<div class="mb-12">
  <div class="section-label">Primary recommendation</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Grand Anse for most cruise passengers</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Grand Anse is the island’s signature long beach for a cruise swim day: straightforward intent
    (sand and water), typically a short transfer from the St George's port area, and a better fit
    for mixed groups than committing the clock to far inland roads. We do not invent chair prices
    or facility inventories — verify on the day.
  </p>
  <a href="/grand-anse-beach-excursions" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">
    Open Grand Anse cruise guide
  </a>
</div>
<div class="mb-12">
  <div class="section-label">Nearby names</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Morne Rouge and Magazine Beach</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-4">
    <strong>Morne Rouge</strong> and <strong>Magazine Beach</strong> are often discussed by visitors
    looking for alternatives near the south-west coast. Treat those mentions as orientation for
    conversation with a trusted driver or operator — not as verified facility lists, always-open
    amenities, or guaranteed quieter conditions on your sailing date.
  </p>
  <p class="text-gray-600 leading-relaxed max-w-3xl">
    If your group simply wants a reliable swim-and-sand plan with clear cruise logistics, Grand Anse
    remains the primary decision for most calls.
  </p>
</div>
<div>
  <div class="section-label">Intent split</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Comparison page vs Grand Anse page</h2>
  <ul class="space-y-3 text-gray-600 leading-relaxed max-w-3xl">
    <li><strong>This page</strong> — which beach theme fits your call, and why Grand Anse is usually first.</li>
    <li><strong>Grand Anse page</strong> — transfer framing, calm-day use-case, pairing advice and return planning.</li>
  </ul>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  Beach days still need a return plan. Agree transport both ways, leave margin before all-aboard,
  and confirm operator policy if you book anything independently. For inland alternatives, see
  waterfalls and rainforest guides rather than forcing a dual theme onto a short call.
</p>
''' + related_links([
    ("/grand-anse-beach-excursions", "Grand Anse cruise page"),
    ("/best-grenada-shore-excursions", "All day styles"),
    ("/grenada-snorkelling-tours", "Snorkelling"),
    ("/grenada-cruise-port-guide", "Port guide"),
]))}
{faq_section([
    (
        "Which beach is best for a Grenada cruise stop?",
        "For most passengers, Grand Anse is the primary calm swim-day choice from St George's. "
        "Open the Grand Anse cruise page for transfer and timing notes.",
    ),
    (
        "Are Morne Rouge or Magazine Beach better than Grand Anse?",
        "They are often discussed by visitors as nearby south-west options, but conditions and "
        "facilities vary. Do not assume a quieter or better-equipped day without local confirmation.",
    ),
    (
        "Do you list beach chair prices?",
        "No. Prices and hire arrangements change. Verify on the day with vendors or your operator.",
    ),
], heading="Grenada beaches FAQ")}
"""

    faqs: FaqList = [
        (
            "Which beach is best for a Grenada cruise stop?",
            "For most passengers, Grand Anse is the primary calm swim-day choice from St George's. "
            "Open the Grand Anse cruise page for transfer and timing notes.",
        ),
        (
            "Are Morne Rouge or Magazine Beach better than Grand Anse?",
            "They are often discussed by visitors as nearby south-west options, but conditions and "
            "facilities vary. Do not assume a quieter or better-equipped day without local confirmation.",
        ),
        (
            "Do you list beach chair prices?",
            "No. Prices and hire arrangements change. Verify on the day with vendors or your operator.",
        ),
    ]

    meta: Meta = {
        "title": "Best Beaches in Grenada for Cruise Passengers | Grand Anse Guide",
        "description": (
            "Compare the best beaches in Grenada for cruise passengers — Grand Anse as the primary "
            "swim day, nearby names often discussed by visitors, and links to practical planning."
        ),
        "canonical_path": "/best-beaches-in-grenada",
        "page_id": "beaches",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# WATERFALLS
# ---------------------------------------------------------------------------


def waterfalls() -> PageTuple:
    hero = hero_band(
        eyebrow="Inland · waterfalls",
        title_html=f'Grenada <br/> <span class="{ACCENT}">waterfall tours</span>',
        lead=(
            "Annandale as a nearer, commonly discussed choice; Concord and Seven Sisters "
            "as longer-drive options to check against your call length — plus practical "
            "footwear notes for wet paths, without timing guarantees."
        ),
        image=WATERFALLS,
        aria_label=WATERFALLS_ALT,
        breadcrumb="Waterfalls",
        actions=_cta(
            "/one-day-in-grenada",
            "One-day planning",
            "/grenada-rainforest-tours",
            "Rainforest context",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Nearer framing", "Annandale often discussed for tighter clocks"),
            ("Longer drives", "Concord / Seven Sisters — verify duration for your call"),
            ("Paths", "Expect wet, uneven footing — sturdy shoes help"),
            ("Activity", "Moderate walking; not a beach substitute"),
            ("Return", "Leave margin; do not treat durations as guarantees"),
        ]
    )

    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Waterfall days trade sand time for rainforest pools and humid trails. From St George's,
  <strong>Annandale</strong> is often framed as a nearer, commonly chosen option when the clock is
  tight. <strong>Concord</strong> and <strong>Seven Sisters</strong> style itineraries usually mean
  more road time — confirm total duration with any operator against your all-aboard window.
</p>
<div class="info-image rounded-3xl aspect-[16/9] shadow-xl overflow-hidden my-8 max-w-3xl">
  <img src="{WATERFALLS}" alt="{escape(WATERFALLS_ALT)}" width="960" height="540" loading="lazy" decoding="async" />
</div>
''' + snap)}
{_section('''
<div class="grid md:grid-cols-2 gap-10">
  <div>
    <div class="section-label">Practical kit</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Wet paths and footwear</h2>
    <p class="text-gray-600 leading-relaxed">
      Expect damp rock, mud and spray near pools. Closed shoes with grip beat flip-flops on approaches.
      A dry bag for phones, insect awareness and a change of shirt help — none of which replaces checking
      live trail or access conditions on the day.
    </p>
  </div>
  <div>
    <div class="section-label">Related inland</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Rainforest without duplicating this page</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Grand Etang cooler elevation and crater-lake context live on the rainforest guide. Spice loops
      may share road corridors — pick one primary story rather than stacking falls, nutmeg and lake
      viewpoints onto a short call.
    </p>
    <a href="/grenada-rainforest-tours" class="text-ocean-600 font-semibold">Rainforest tours →</a>
  </div>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  We do not guarantee swim access, trail openness or exact drive minutes. Confirm inclusions and
  return timing with the operator before you pay, and leave margin before all-aboard.
</p>
''' + related_links([
    ("/grenada-rainforest-tours", "Rainforest"),
    ("/grenada-spice-island-tours", "Spice Island guide"),
    ("/one-day-in-grenada", "One day"),
    ("/best-grenada-shore-excursions", "Compare styles"),
]))}
<p class="text-gray-600 leading-relaxed text-sm mt-6 max-w-3xl">
  Looking for a guided half-day with spice-estate context (and Concord Falls on that itinerary —
  not Annandale)? See the
  <a href="/grenada-spice-island-tours" class="text-ocean-600 font-medium">spice island guide</a>
  or
  <a href="/book/grenadas-spice-route" class="text-ocean-600 font-medium">request Grenada's Spice Route</a>.
</p>
{faq_section([
    (
        "Which waterfall is best on a short cruise call?",
        "Annandale is often discussed as a nearer option. Longer-drive falls need a clearer duration "
        "check against your sailing. Neither is guaranteed to fit every schedule.",
    ),
    (
        "Do I need special shoes?",
        "Closed shoes with grip are wiser than flip-flops on wet approaches. Confirm any swim or "
        "climb segments with your operator.",
    ),
], heading="Waterfall FAQ")}
"""

    faqs: FaqList = [
        (
            "Which waterfall is best on a short cruise call?",
            "Annandale is often discussed as a nearer option. Longer-drive falls need a clearer duration "
            "check against your sailing. Neither is guaranteed to fit every schedule.",
        ),
        (
            "Do I need special shoes?",
            "Closed shoes with grip are wiser than flip-flops on wet approaches. Confirm any swim or "
            "climb segments with your operator.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Waterfall Tours | Annandale & Longer-Drive Options",
        "description": (
            "Plan Grenada waterfall tours from a cruise call — Annandale nearer framing, Concord and "
            "Seven Sisters duration checks, footwear notes and return planning."
        ),
        "canonical_path": "/grenada-waterfall-tours",
        "page_id": "waterfalls",
        "og_image": WATERFALLS,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# SPICE
# ---------------------------------------------------------------------------


def spice() -> PageTuple:
    hero = hero_band(
        eyebrow="Spice Island",
        title_html=f'Grenada <br/> <span class="{ACCENT}">spice island tours</span>',
        lead=(
            "Nutmeg, plantation storytelling and west-coast or Grand Etang style loops — "
            "editorial decision guidance for cruise passengers, without inventing stop lists "
            "or duplicating waterfall and rainforest focus."
        ),
        image=None,
        aria_label="Grenada spice island tours for cruise passengers",
        css_only=True,
        breadcrumb="Spice Island",
        actions=_cta(
            "/book/grenadas-spice-route",
            "Book now",
            "/best-grenada-shore-excursions",
            "Compare styles",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Theme", "Nutmeg / plantation / Spice Island identity"),
            ("Often combined", "West-coast or Grand Etang style scenic loops"),
            ("Activity", "Low to moderate — walking and listening"),
            ("Not the same as", "Dedicated waterfall or deep rainforest trail days"),
            ("Request option", "Grenada's Spice Route — $89 · ages 3+ · about 4 hours"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Grenada earned its <strong>Spice Island</strong> name through nutmeg and related crops.
  Cruise-oriented spice tours are usually about plantation context, scent and story — often
  woven into a west-coast or inland scenic loop rather than a single isolated stop. Treat operator
  itineraries as packages to verify, not as a fixed national circuit.
</p>
''' + snap)}
{_section('''
<div class="max-w-3xl mb-12">
  <div class="section-label">Request online</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Grenada's Spice Route</h2>
  <p class="text-gray-600 leading-relaxed mb-4">
    A guided half-day scenic and cultural excursion from the cruise ship pier — typically about
    4 hours — covering Concord Falls, Gouyave, a traditional spice estate, and Grand Etang rainforest
    / crater lake context. Mona monkeys may be seen; they are not guaranteed. Food and drinks are
    not included. Optional spice purchases are at your own cost. Moderate walking on mixed surfaces
    and inclines. This is not an Annandale Falls tour, and it does not claim Fort George or Fort Frederick stops.
  </p>
  <p class="text-gray-600 leading-relaxed mb-4">
    Guests (ages 3+) $89 · ages 0–2 not permitted · guests under 16 must travel with a responsible adult ·
    maximum 10 guests online. Payment creates a booking request; confirmation is emailed separately.
    Free cancellation outside 14 days before your excursion; from the 14th day, non-refundable.
    If we cannot confirm, you receive a full refund to your original payment method.
  </p>
  <p class="text-gray-600 leading-relaxed mb-6">
    <a href="/book/grenadas-spice-route" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">Book now</a>
  </p>
</div>
<div class="grid md:grid-cols-2 gap-10">
  <div>
    <div class="section-label">Decision</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">When spice beats beach or falls</h2>
    <p class="text-gray-600 leading-relaxed">
      Choose spice when your group wants cultural context and lighter walking more than a long swim
      or wet-path waterfall morning. It pairs naturally with viewpoint driving — less naturally with
      a full Grand Anse afternoon on a short call.
    </p>
  </div>
  <div>
    <div class="section-label">Cross-links</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Waterfall and rainforest without copying them</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Falls and Grand Etang appear on many island loops. If waterfalls or crater-lake elevation are
      the main reason you leave the pier, open those dedicated guides instead of expecting this page
      to cover trail detail.
    </p>
    <p class="space-x-3">
      <a href="/grenada-waterfall-tours" class="text-ocean-600 font-semibold">Waterfalls →</a>
      <a href="/grenada-rainforest-tours" class="text-ocean-600 font-semibold">Rainforest →</a>
    </p>
  </div>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  Confirm which plantations, markets or tasting stops are included before you pay. Leave margin
  before all-aboard; scenic loops expand easily when every viewpoint becomes a photo stop.
</p>
''' + related_links([
    ("/book/grenadas-spice-route", "Book Grenada's Spice Route"),
    ("/grenada-chocolate-rum-tours", "Chocolate & rum"),
    ("/grenada-island-sightseeing-tours", "Island sightseeing"),
    ("/one-day-in-grenada", "One day"),
]))}
{faq_section([
    (
        "Are spice tours suitable for a short call?",
        "Often yes when the loop is compact and return timing is clear. Verify duration with the "
        "operator against your all-aboard time.",
    ),
    (
        "Can I book Grenada's Spice Route here?",
        "Yes. Use Book now to request Grenada's Spice Route. Payment creates a request; confirmation "
        "is emailed separately. If we cannot confirm, you receive a full refund.",
    ),
    (
        "Is a spice tour the same as a rainforest tour?",
        "No. Spice emphasises plantations and island identity; rainforest emphasises Grand Etang "
        "elevation and forest context. Some packages blend elements — read inclusions carefully.",
    ),
], heading="Spice Island FAQ")}
"""

    faqs: FaqList = [
        (
            "Are spice tours suitable for a short call?",
            "Often yes when the loop is compact and return timing is clear. Verify duration with the "
            "operator against your all-aboard time.",
        ),
        (
            "Can I book Grenada's Spice Route here?",
            "Yes. Use Book now to request Grenada's Spice Route. Payment creates a request; confirmation "
            "is emailed separately. If we cannot confirm, you receive a full refund.",
        ),
        (
            "Is a spice tour the same as a rainforest tour?",
            "No. Spice emphasises plantations and island identity; rainforest emphasises Grand Etang "
            "elevation and forest context. Some packages blend elements — read inclusions carefully.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Spice Island Tours | Nutmeg & Plantation Shore Days",
        "description": (
            "Plan Grenada spice island tours from a cruise call — nutmeg and plantation context, "
            "west-coast style loops, and how spice differs from waterfall or rainforest focus."
        ),
        "canonical_path": "/grenada-spice-island-tours",
        "page_id": "spice",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# RAINFOREST
# ---------------------------------------------------------------------------


def rainforest() -> PageTuple:
    hero = hero_band(
        eyebrow="Interior · Grand Etang",
        title_html=f'Grenada <br/> <span class="{ACCENT}">rainforest tours</span>',
        lead=(
            "Grand Etang crater-lake context, cooler elevation and forest atmosphere "
            "for cruise passengers who want inland greenery rather than a beach morning."
        ),
        image=RAINFOREST,
        aria_label=RAINFOREST_ALT,
        breadcrumb="Rainforest",
        actions=_cta(
            "/grenada-waterfall-tours",
            "Waterfall guide",
            "/grenada-spice-island-tours",
            "Spice Island",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Focus", "Grand Etang / crater lake / cooler elevation"),
            ("Feel", "Forest atmosphere — not a swim-beach day"),
            ("Activity", "Moderate; paths and viewpoints vary by package"),
            ("Often nearby themes", "Spice loops or waterfall add-ons — verify duration"),
            ("Return", "Inland roads still need a buffer before all-aboard"),
        ]
    )

    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  <strong>Grand Etang</strong> sits in Grenada’s mountainous interior: crater-lake views, cooler
  air than the coast, and rainforest context that feels different from Grand Anse. Cruise packages
  vary — some emphasise lookouts and short walks; others fold in spice or waterfall stops. Read
  the inclusions rather than assuming a single “standard” rainforest day.
</p>
<div class="info-image rounded-3xl aspect-[16/9] shadow-xl overflow-hidden my-8 max-w-3xl">
  <img src="{RAINFOREST}" alt="{escape(RAINFOREST_ALT)}" width="960" height="540" loading="lazy" decoding="async" />
</div>
''' + snap)}
{_section('''
<div class="grid md:grid-cols-2 gap-10">
  <div>
    <div class="section-label">Who it suits</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Elevation over sand</h2>
    <p class="text-gray-600 leading-relaxed">
      Choose rainforest when your group wants greenery, viewpoints and a break from heat at sea level.
      It is a weaker fit for passengers whose only priority is a long unsupervised beach afternoon.
    </p>
  </div>
  <div>
    <div class="section-label">Boundaries</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Falls and spice live next door</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Dedicated waterfall footwear and pool guidance sits on the waterfall page. Nutmeg storytelling
      sits on the spice page. Cross-link for planning — do not expect one article to replace the others.
    </p>
    <p class="space-x-3">
      <a href="/grenada-waterfall-tours" class="text-ocean-600 font-semibold">Waterfalls →</a>
      <a href="/grenada-spice-island-tours" class="text-ocean-600 font-semibold">Spice →</a>
    </p>
  </div>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  Weather inland can differ from the harbour. Confirm duration, walking expectations and return
  timing with the operator before you pay, and leave margin before all-aboard.
</p>
''' + related_links([
    ("/one-day-in-grenada", "One day"),
    ("/best-grenada-shore-excursions", "Compare styles"),
    ("/grenada-island-sightseeing-tours", "Island sightseeing"),
    ("/grenada-faq", "FAQ"),
]))}
<p class="text-gray-600 leading-relaxed text-sm mt-6 max-w-3xl">
  Some spice-focused half-days also include Grand Etang context without being a dedicated rainforest hike.
  See the
  <a href="/grenada-spice-island-tours" class="text-ocean-600 font-medium">spice island guide</a>
  or
  <a href="/book/grenadas-spice-route" class="text-ocean-600 font-medium">request Grenada's Spice Route</a>
  — that itinerary is not an Annandale waterfall tour.
</p>
{faq_section([
    (
        "Is Grand Etang far from the cruise port?",
        "It is an inland commitment from St George's. Exact minutes vary with traffic and stops — "
        "confirm total tour duration against your call.",
    ),
    (
        "Can I swim at Grand Etang?",
        "Do not assume swimming is included or appropriate. Confirm access and safety guidance with "
        "your operator or park information on the day.",
    ),
], heading="Rainforest FAQ")}
"""

    faqs: FaqList = [
        (
            "Is Grand Etang far from the cruise port?",
            "It is an inland commitment from St George's. Exact minutes vary with traffic and stops — "
            "confirm total tour duration against your call.",
        ),
        (
            "Can I swim at Grand Etang?",
            "Do not assume swimming is included or appropriate. Confirm access and safety guidance with "
            "your operator or park information on the day.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Rainforest Tours | Grand Etang from a Cruise Call",
        "description": (
            "Plan Grenada rainforest tours from St George's — Grand Etang crater-lake context, "
            "cooler elevation and how rainforest days differ from beach or spice themes."
        ),
        "canonical_path": "/grenada-rainforest-tours",
        "page_id": "rainforest",
        "og_image": RAINFOREST,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# CHOCOLATE & RUM
# ---------------------------------------------------------------------------


def chocolate_rum() -> PageTuple:
    hero = hero_band(
        eyebrow="Culture · tasting",
        title_html=f'Grenada <br/> <span class="{ACCENT}">chocolate &amp; rum</span>',
        lead=(
            "Cocoa, chocolate and rum tasting as a calmer cultural option for cruise "
            "passengers — verify operator inclusions, and keep the return window honest."
        ),
        image=None,
        aria_label="Grenada chocolate and rum tasting tours for cruise passengers",
        css_only=True,
        breadcrumb="Chocolate & rum",
        actions=_cta(
            "/grenada-spice-island-tours",
            "Spice Island",
            "/best-grenada-shore-excursions",
            "Compare styles",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Role", "Calmer cultural / tasting day"),
            ("Activity", "Typically low — walking and tasting"),
            ("Verify", "Which estates, tastings and transfers are included"),
            ("Alcohol", "Pace tastings; know your own limits before returning"),
            ("Commerce", "Editorial only — no product codes or checkout"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Chocolate and rum experiences suit passengers who want Grenada’s agricultural story without
  committing to wet waterfall paths or a full beach transfer morning. Packages differ widely:
  some emphasise cocoa processing, others distillery context or combined spice stops. Verify
  inclusions before you pay.
</p>
''' + snap)}
{_section('''
<div class="max-w-3xl">
  <div class="section-label">Planning notes</div>
  <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Taste, then protect the clock</h2>
  <p class="text-gray-600 leading-relaxed mb-4">
    Tasting days expand when every sample becomes a long conversation. Agree the return plan early,
    especially if alcohol is involved. Leave margin before all-aboard and confirm whether transport
    is round-trip or one-way.
  </p>
  <p class="text-gray-600 leading-relaxed">
    For broader plantation identity without focusing on tastings, see
    <a href="/grenada-spice-island-tours" class="text-ocean-600 font-medium">spice island tours</a>.
  </p>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  This site does not sell chocolate or rum tours and does not list commercial product codes.
  Contact operators directly for availability on your sailing date.
</p>
''' + related_links([
    ("/grenada-spice-island-tours", "Spice Island"),
    ("/grenada-island-sightseeing-tours", "Island sightseeing"),
    ("/one-day-in-grenada", "One day"),
    ("/contact", "Contact"),
]))}
{faq_section([
    (
        "Is a chocolate and rum tour a full-day commitment?",
        "Duration varies by operator. Confirm total time including transfers against your all-aboard "
        "window before you book.",
    ),
    (
        "Can children join tasting tours?",
        "Policies differ. Ask about age rules and non-alcoholic options before paying.",
    ),
], heading="Chocolate & rum FAQ")}
"""

    faqs: FaqList = [
        (
            "Is a chocolate and rum tour a full-day commitment?",
            "Duration varies by operator. Confirm total time including transfers against your all-aboard "
            "window before you book.",
        ),
        (
            "Can children join tasting tours?",
            "Policies differ. Ask about age rules and non-alcoholic options before paying.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Chocolate & Rum Tours | Cruise Cultural Days",
        "description": (
            "Plan Grenada chocolate and rum tasting tours from a cruise call — calmer cultural options, "
            "inclusion checks and return planning from St George's."
        ),
        "canonical_path": "/grenada-chocolate-rum-tours",
        "page_id": "chocolate-rum",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# ISLAND SIGHTSEEING
# ---------------------------------------------------------------------------


def island() -> PageTuple:
    hero = hero_band(
        eyebrow="Overview day",
        title_html=f'Grenada <br/> <span class="{ACCENT}">island sightseeing</span>',
        lead=(
            "A broader overview: Carenage harbour character, Fort Frederick viewpoints, "
            "harbour views and an optional beach stop — without duplicating the spice plantation focus."
        ),
        image=INTRO,
        aria_label=INTRO_ALT,
        breadcrumb="Island sightseeing",
        actions=_cta(
            "/grenada-cruise-port-guide",
            "Port guide",
            "/best-grenada-shore-excursions",
            "Compare styles",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Role", "Overview / viewpoints / harbour character"),
            ("Typical beats", "Carenage, fort lookouts, optional beach stop"),
            ("Not the same as", "Dedicated spice plantation deep-dive"),
            ("Pacing", "Several stops — easy to overrun the clock"),
            ("Return", "Cap the photo stops; leave margin"),
        ]
    )

    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Island sightseeing days trade depth at one site for a sequence of views: the
  <strong>Carenage</strong>, hillside colour, <strong>Fort Frederick</strong> style viewpoints and
  harbour panoramas, sometimes finishing with a beach stop. Use this page for that overview intent.
  For nutmeg and plantation storytelling, open the
  <a href="/grenada-spice-island-tours" class="text-ocean-600 font-medium">spice island guide</a> instead.
</p>
<div class="info-image rounded-3xl aspect-[4/3] shadow-xl overflow-hidden my-8 max-w-xl">
  <img src="{INTRO}" alt="{escape(INTRO_ALT)}" width="800" height="600" loading="lazy" decoding="async" />
</div>
''' + snap)}
{_section('''
<div class="max-w-3xl">
  <div class="section-label">How to use an overview day</div>
  <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Views first, stacking second</h2>
  <p class="text-gray-600 leading-relaxed mb-4">
    Overview loops suit first-time callers who want photographs and orientation more than a long
    unsupervised swim. They are weaker when everyone in the group wanted Grand Anse for three quiet
    hours — in that case, simplify.
  </p>
  <p class="text-gray-600 leading-relaxed">
    Confirm which forts, lookouts and beach stops are included. Leave margin before all-aboard;
    viewpoint days expand whenever every ridge becomes “just five more minutes”.
  </p>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
''' + related_links([
    ("/grand-anse-beach-excursions", "Grand Anse"),
    ("/grenada-spice-island-tours", "Spice Island"),
    ("/grenada-private-tours", "Private pacing"),
    ("/one-day-in-grenada", "One day"),
]))}
{faq_section([
    (
        "Is island sightseeing the same as a spice tour?",
        "No. Sightseeing emphasises harbour and viewpoint orientation; spice emphasises plantations "
        "and nutmeg identity. Some operators blend both — read the inclusions.",
    ),
    (
        "Should I add a beach stop?",
        "Only if the remaining clock still protects your return. A rushed ten-minute beach photo is "
        "rarely worth risking all-aboard.",
    ),
], heading="Island sightseeing FAQ")}
"""

    faqs: FaqList = [
        (
            "Is island sightseeing the same as a spice tour?",
            "No. Sightseeing emphasises harbour and viewpoint orientation; spice emphasises plantations "
            "and nutmeg identity. Some operators blend both — read the inclusions.",
        ),
        (
            "Should I add a beach stop?",
            "Only if the remaining clock still protects your return. A rushed ten-minute beach photo is "
            "rarely worth risking all-aboard.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Island Sightseeing Tours | Carenage & Viewpoints",
        "description": (
            "Plan Grenada island sightseeing from a cruise call — Carenage character, Fort Frederick "
            "viewpoints, harbour views and optional beach stops."
        ),
        "canonical_path": "/grenada-island-sightseeing-tours",
        "page_id": "island",
        "og_image": INTRO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# SNORKELLING
# ---------------------------------------------------------------------------


def snorkelling() -> PageTuple:
    hero = hero_band(
        eyebrow="Water day",
        title_html=f'Grenada <br/> <span class="{ACCENT}">snorkelling tours</span>',
        lead=(
            "Molinere and Underwater Sculpture Park context, reef choices and sea-condition "
            "awareness — confirm departure logistics with the operator; some trips involve a "
            "transfer to a departure point."
        ),
        image=None,
        aria_label="Grenada snorkelling tours for cruise passengers",
        css_only=True,
        breadcrumb="Snorkelling",
        actions=_cta(
            "/best-beaches-in-grenada",
            "Beach comparison",
            "/one-day-in-grenada",
            "One-day planning",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Known context", "Molinere / Underwater Sculpture Park often discussed"),
            ("Conditions", "Sea state matters — trips can change or cancel"),
            ("Logistics", "Some trips may transfer to a departure point — confirm"),
            ("Activity", "Low to moderate swimming comfort needed"),
            ("Not claimed here", "Specific marina pickup as a universal fact"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Snorkel days around Grenada often reference the <strong>Molinere</strong> coast and the
  <strong>Underwater Sculpture Park</strong>, alongside other reef choices. Treat those names as
  planning context — exact sites, swim times and boat types depend on the operator and the day’s
  sea conditions.
</p>
''' + snap)}
{_section('''
<div class="grid md:grid-cols-2 gap-10">
  <div>
    <div class="section-label">Logistics</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Confirm how you reach the boat</h2>
    <p class="text-gray-600 leading-relaxed">
      Do not assume a fixed marina pickup as a universal fact for every product. Some trips may
      involve a transfer from the cruise area to a departure point. Confirm meeting place, return
      location and total duration in writing before you pay.
    </p>
  </div>
  <div>
    <div class="section-label">Conditions</div>
    <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Sea state can rewrite the day</h2>
    <p class="text-gray-600 leading-relaxed">
      Wind and swell change visibility and comfort. Have a backup theme (calm beach or town walking)
      if water conditions are poor. Leave margin before all-aboard even when the sea looks friendly
      at mid-morning.
    </p>
  </div>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<p class="text-gray-600 leading-relaxed mb-4">
  This guide does not list commercial snorkel product codes or invent equipment fees. Ask operators
  about mask fit, flotation options and cancellation rules for your sailing date.
</p>
''' + related_links([
    ("/grand-anse-beach-excursions", "Grand Anse"),
    ("/grenada-family-excursions", "Family"),
    ("/best-grenada-shore-excursions", "Compare styles"),
    ("/grenada-faq", "FAQ"),
]))}
{faq_section([
    (
        "Will I see the Underwater Sculpture Park?",
        "Many snorkel conversations reference Molinere / the sculpture park, but inclusions vary. "
        "Confirm the site list with your operator for that day.",
    ),
    (
        "Do snorkel trips leave from beside the ship?",
        "Not necessarily. Some trips may involve a transfer to a departure point. Confirm meeting "
        "and return logistics before you pay.",
    ),
], heading="Snorkelling FAQ")}
"""

    faqs: FaqList = [
        (
            "Will I see the Underwater Sculpture Park?",
            "Many snorkel conversations reference Molinere / the sculpture park, but inclusions vary. "
            "Confirm the site list with your operator for that day.",
        ),
        (
            "Do snorkel trips leave from beside the ship?",
            "Not necessarily. Some trips may involve a transfer to a departure point. Confirm meeting "
            "and return logistics before you pay.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Snorkelling Tours | Molinere & Reef Choices",
        "description": (
            "Plan Grenada snorkelling from a cruise call — Molinere and Underwater Sculpture Park "
            "context, reef choices, sea conditions and transfer logistics to confirm."
        ),
        "canonical_path": "/grenada-snorkelling-tours",
        "page_id": "snorkelling",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# PRIVATE
# ---------------------------------------------------------------------------


def private_tours() -> PageTuple:
    hero = hero_band(
        eyebrow="Custom pacing",
        title_html=f'Grenada <br/> <span class="{ACCENT}">private tours</span>',
        lead=(
            "Editorial guidance for private shore days: custom pacing, mixed mobility within "
            "a group, and confirming return time in writing before you pay."
        ),
        image=None,
        aria_label="Grenada private tours for cruise passengers",
        css_only=True,
        breadcrumb="Private tours",
        actions=_cta(
            "/one-day-in-grenada",
            "One-day planning",
            "/best-grenada-shore-excursions",
            "Compare styles",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Best for", "Mixed ages, mobility needs, custom stop lists"),
            ("Advantage", "Pace control — not automatic schedule safety"),
            ("Must do", "Confirm return time in writing before paying"),
            ("Still true", "Leave margin before all-aboard"),
            ("This site", "Editorial only — no booking checkout"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Private tours help when one shared package will not fit everyone in the party: different walking
  speeds, a stroller, limited stairs tolerance, or a wish to blend Grand Anse with a short inland
  viewpoint without joining a fixed coach script. Flexibility is the point — it is not a substitute
  for written timing discipline.
</p>
''' + snap)}
{_section('''
<div class="max-w-3xl">
  <div class="section-label">Before you pay</div>
  <h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Return time in writing</h2>
  <p class="text-gray-600 leading-relaxed mb-4">
    Agree the latest pier return, what happens if traffic builds, and whether the driver waits at
    beach or waterfall stops. Keep the plan shorter than the maximum hours available. Confirm
    payment method and cancellation terms without sharing card details by casual email threads
    you do not trust.
  </p>
  <p class="text-gray-600 leading-relaxed">
    Use the theme guides —
    <a href="/grand-anse-beach-excursions" class="text-ocean-600 font-medium">Grand Anse</a>,
    <a href="/grenada-waterfall-tours" class="text-ocean-600 font-medium">waterfalls</a>,
    <a href="/grenada-spice-island-tours" class="text-ocean-600 font-medium">spice</a> —
    to choose ingredients, then ask a private operator to sequence only what fits.
  </p>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
''' + related_links([
    ("/grenada-family-excursions", "Family"),
    ("/grenada-cruise-port-guide", "Port guide"),
    ("/grenada-faq", "FAQ"),
    ("/contact", "Contact"),
]))}
{faq_section([
    (
        "Is a private tour safer for making the ship?",
        "Private pacing can help, but it does not remove traffic or queue risk. Confirm return time "
        "in writing and still leave margin before all-aboard.",
    ),
    (
        "Can we mix beach and waterfall privately?",
        "Sometimes on a fuller call. On shorter calls, choose one primary theme. Ask the operator "
        "for an honest duration before paying.",
    ),
], heading="Private tours FAQ")}
"""

    faqs: FaqList = [
        (
            "Is a private tour safer for making the ship?",
            "Private pacing can help, but it does not remove traffic or queue risk. Confirm return time "
            "in writing and still leave margin before all-aboard.",
        ),
        (
            "Can we mix beach and waterfall privately?",
            "Sometimes on a fuller call. On shorter calls, choose one primary theme. Ask the operator "
            "for an honest duration before paying.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Private Tours | Custom Cruise Shore Days",
        "description": (
            "Plan Grenada private tours from a cruise call — custom pacing, mixed mobility, and "
            "confirming return time in writing before you pay."
        ),
        "canonical_path": "/grenada-private-tours",
        "page_id": "private",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# FAMILY
# ---------------------------------------------------------------------------


def family() -> PageTuple:
    hero = hero_band(
        eyebrow="Family planning",
        title_html=f'Grenada <br/> <span class="{ACCENT}">family excursions</span>',
        lead=(
            "Short, practical notes for cruise families: calm beach time, gentler waterfall "
            "walks and age-appropriate snorkel choices — without over-promising."
        ),
        image=None,
        aria_label="Grenada family excursions for cruise passengers",
        css_only=True,
        breadcrumb="Family",
        actions=_cta(
            "/grand-anse-beach-excursions",
            "Grand Anse",
            "/one-day-in-grenada",
            "One-day planning",
        ),
    )

    snap = cruise_snapshot(
        [
            ("Strong default", "Calm beach time at Grand Anse"),
            ("Inland", "Gentler waterfall walks — check path difficulty"),
            ("Water", "Age-appropriate snorkel only — confirm rules"),
            ("Pacing", "Fewer stops beat a packed highlight reel"),
            ("Return", "Build extra margin with children"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  With children aboard, Grenada usually rewards simplicity: a
  <a href="/grand-anse-beach-excursions" class="text-ocean-600 font-medium">Grand Anse</a>
  swim morning, or a carefully chosen gentler waterfall walk, rather than stacking spice, forts
  and reefs onto one short call. Nap needs and snack timing matter as much as attraction names.
</p>
''' + snap)}
{_section('''
<ul class="space-y-4 text-gray-600 leading-relaxed max-w-3xl">
  <li><strong>Beach first</strong> — lowest complexity for mixed ages; agree return transport early.</li>
  <li><strong>Waterfalls</strong> — ask about path length, spray and whether little legs will cope; see the <a href="/grenada-waterfall-tours" class="text-ocean-600 font-medium">waterfall guide</a>.</li>
  <li><strong>Snorkel</strong> — confirm minimum ages, flotation and sea conditions; see <a href="/grenada-snorkelling-tours" class="text-ocean-600 font-medium">snorkelling</a>.</li>
  <li><strong>Private pacing</strong> — useful when ages differ widely; confirm return time in writing via the <a href="/grenada-private-tours" class="text-ocean-600 font-medium">private guide</a>.</li>
</ul>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
''' + related_links([
    ("/best-beaches-in-grenada", "Best beaches"),
    ("/grenada-faq", "FAQ"),
    ("/grenada-cruise-port-guide", "Port guide"),
    ("/contact", "Contact"),
]))}
{faq_section([
    (
        "What is the easiest Grenada shore day with kids?",
        "A calm Grand Anse beach plan is usually the lowest-complexity default. Confirm transport "
        "both ways and leave extra margin before all-aboard.",
    ),
    (
        "Are waterfall tours suitable for young children?",
        "It depends on the path and the child’s stamina. Ask the operator about difficulty and "
        "duration before paying.",
    ),
], heading="Family FAQ")}
"""

    faqs: FaqList = [
        (
            "What is the easiest Grenada shore day with kids?",
            "A calm Grand Anse beach plan is usually the lowest-complexity default. Confirm transport "
            "both ways and leave extra margin before all-aboard.",
        ),
        (
            "Are waterfall tours suitable for young children?",
            "It depends on the path and the child’s stamina. Ask the operator about difficulty and "
            "duration before paying.",
        ),
    ]

    meta: Meta = {
        "title": "Grenada Family Excursions | Cruise Days with Children",
        "description": (
            "Plan Grenada family shore excursions — calm beach time, gentler waterfall walks and "
            "age-appropriate snorkel choices from St George's."
        ),
        "canonical_path": "/grenada-family-excursions",
        "page_id": "family",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------------


def faq() -> PageTuple:
    hero = hero_band(
        eyebrow="Help",
        title_html=f'Grenada <br/> <span class="{ACCENT}">cruise FAQ</span>',
        lead=(
            "Honest answers for St George's cruise passengers: ship versus independent "
            "booking trade-offs, timing, beaches and inland themes — without guarantees."
        ),
        image=None,
        aria_label="Grenada cruise passenger FAQ",
        css_only=True,
        breadcrumb="FAQ",
        actions=_cta("/best-grenada-shore-excursions", "Compare styles", "/contact", "Contact"),
    )

    faqs: FaqList = [
        (
            "Where do cruise ships dock in Grenada?",
            "Ships generally dock at St George's, with passenger orientation around the Melville Street / "
            "Carenage area. Confirm berth details for your sailing.",
        ),
        (
            "Should I book through the ship or independently?",
            "Ship tours can feel simpler on timing; independent plans may offer more flexibility but "
            "require your own return discipline. Neither is universally “safer”. Match the method to "
            "your group and call length — we sell neither.",
        ),
        (
            "How long will we have ashore?",
            "Typical calls often run several hours, but schedules vary by ship and season. Use your "
            "sailing’s gangway and all-aboard times, not a generic estimate.",
        ),
        (
            "Is Grand Anse the best beach for cruise passengers?",
            "For most swim-focused calls, yes as a primary choice. See the best beaches comparison and "
            "the Grand Anse cruise page for intent split and transfer framing.",
        ),
        (
            "Can I see a waterfall and the beach on one call?",
            "Sometimes on a fuller day with disciplined timing; often not on a short call. Protect the "
            "return window first.",
        ),
        (
            "Do you guarantee I will make it back to the ship?",
            "No. No editorial guide can guarantee traffic, queues or sea conditions. Leave margin before "
            "all-aboard and confirm operator return policy before you pay.",
        ),
        (
            "Do you sell excursions on this website?",
            "No. This is an independent planning guide. Email us for editorial questions only.",
        ),
    ]

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Straight answers for planning a Grenada shore day from St George's. For deeper theme pages,
  use the excursions hub and port guide linked below.
</p>
''')}
{faq_section(faqs, heading="Frequently asked questions")}
{_prose('''
''' + related_links([
    ("/grenada-cruise-port-guide", "Port guide"),
    ("/one-day-in-grenada", "One day"),
    ("/best-grenada-shore-excursions", "Excursion styles"),
    ("/contact", "Contact"),
]), bg="bg-white")}
"""

    meta: Meta = {
        "title": f"Grenada Cruise FAQ | {SITE}",
        "description": (
            "Frequently asked questions for Grenada cruise passengers — St George's docking, "
            "ship vs independent booking, beaches, timing and return planning."
        ),
        "canonical_path": "/grenada-faq",
        "page_id": "faq",
        "og_image": None,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# TRUST PAGES
# ---------------------------------------------------------------------------


def contact() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'Contact <br/> <span class="{ACCENT}">{SITE}</span>',
        lead="Editorial questions about this Grenada cruise planning guide.",
        image=None,
        aria_label="Contact Grenada Shore Excursion",
        css_only=True,
        breadcrumb="Contact",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Email <a href="mailto:{EMAIL}" class="text-ocean-600 font-semibold">{EMAIL}</a>
  for questions about this independent guide. We do not process bookings, payments or shore-excursion
  checkouts on this website.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Please include your ship’s scheduled Grenada / St George's date if you are asking about planning logic —
  we still will not invent fares or guarantee operator inventory.
</p>
<p class="text-sm text-gray-500">Do not send payment card details by email.</p>
''')}
"""
    meta: Meta = {
        "title": f"Contact | {SITE}",
        "description": f"Contact {SITE} at {EMAIL} for editorial questions about this Grenada cruise planning guide.",
        "canonical_path": "/contact",
        "page_id": "contact",
        "og_image": None,
    }
    return hero, main, None, meta


def about() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'About <br/> <span class="{ACCENT}">{SITE}</span>',
        lead="Independent cruise-passenger planning for Grenada, from St George's.",
        image=INTRO,
        aria_label=INTRO_ALT,
        breadcrumb="About",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  {SITE} helps cruise passengers decide what is genuinely practical from a St George's call —
  Grand Anse beach time, spice and island loops, waterfall or rainforest interiors, snorkelling,
  and private or family pacing — without pretending every highlight fits every ship schedule.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  We are not a cruise line, not a pier operator, and not a booking marketplace.
</p>
<p class="text-gray-600 leading-relaxed">
  Read our <a href="/methodology" class="text-ocean-600 font-medium">methodology</a>
  and <a href="/contact" class="text-ocean-600 font-medium">contact</a> pages for how we work.
</p>
''')}
"""
    meta: Meta = {
        "title": f"About | {SITE}",
        "description": f"About {SITE} — an independent cruise passenger planning guide for Grenada from St George's.",
        "canonical_path": "/about",
        "page_id": "about",
        "og_image": INTRO,
    }
    return hero, main, None, meta


def privacy() -> PageTuple:
    hero = hero_band(
        eyebrow="Legal",
        title_html=f'Privacy <br/> <span class="{ACCENT}">policy</span>',
        lead="How this editorial website handles information.",
        image=None,
        aria_label="Privacy policy",
        css_only=True,
        breadcrumb="Privacy",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  {SITE} is an editorial planning website. If you email us at
  <a href="mailto:{EMAIL}" class="text-ocean-600 font-medium">{EMAIL}</a>,
  we use your message only to respond. We do not sell personal information.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Standard server and security logs may record technical data such as IP address, user agent and requested URLs.
  Analytics, if enabled by the hosting platform, may collect aggregated traffic statistics.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  This site does not operate a booking checkout and does not ask for payment card details.
</p>
<p class="text-sm text-gray-500">Questions: <a href="mailto:{EMAIL}" class="text-ocean-600">{EMAIL}</a>.</p>
''')}
"""
    meta: Meta = {
        "title": f"Privacy Policy | {SITE}",
        "description": f"Privacy policy for {SITE} — how this Grenada cruise planning website handles information.",
        "canonical_path": "/privacy",
        "page_id": "privacy",
        "og_image": None,
    }
    return hero, main, None, meta


def terms() -> PageTuple:
    hero = hero_band(
        eyebrow="Legal",
        title_html=f'Terms of <br/> <span class="{ACCENT}">use</span>',
        lead="Editorial information only — not a booking contract.",
        image=None,
        aria_label="Terms of use",
        css_only=True,
        breadcrumb="Terms",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  Content on {SITE} is general planning information for cruise passengers. It is not a ticket,
  voucher, insurance policy or contract with any tour operator. Attraction access, road times and
  ship schedules change — confirm live details before you travel.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  We are not affiliated with cruise lines calling at St George's, Grenada. Mentions of beaches,
  waterfalls, spice estates or reefs do not imply partnership.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  To the fullest extent permitted by law, we disclaim liability for decisions made solely on the basis
  of this website. Nothing here creates a consumer booking relationship.
</p>
<p class="text-sm text-gray-500">Contact: <a href="mailto:{EMAIL}" class="text-ocean-600">{EMAIL}</a>.</p>
''')}
"""
    meta: Meta = {
        "title": f"Terms of Use | {SITE}",
        "description": f"Terms of use for {SITE} — editorial cruise planning information, not a booking marketplace.",
        "canonical_path": "/terms",
        "page_id": "terms",
        "og_image": None,
    }
    return hero, main, None, meta


def methodology() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'Methodology <br/> <span class="{ACCENT}">&amp; sourcing</span>',
        lead="How we organise Grenada cruise-day guidance without inventing commercial claims.",
        image=INTRO,
        aria_label=INTRO_ALT,
        breadcrumb="Methodology",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  {SITE} prioritises cruise-passenger decisions: call length, transfer burden, and whether a stop
  sits in St George's local orbit or requires a longer inland or water commitment.
</p>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-6">
  <li>Preserve equity URLs that already attract search interest (extensionless, no trailing slash).</li>
  <li>Separate beach comparison intent from the practical Grand Anse cruise page.</li>
  <li>Use soft claims (“often”, “typically”, “confirm live”) instead of invented schedules or fares.</li>
  <li>Image policy: verified St George's intro imagery, waterfall and rainforest assets only when themed; CSS-only heroes where quarantine images were retired.</li>
  <li>No ship schedules imported as facts; commerce and booking checkout remain deferred.</li>
  <li>Avoid review-aggregate, product-offer and local-business schema types; no fake popularity language.</li>
</ul>
<p class="text-gray-600 leading-relaxed">
  See <a href="/about" class="text-ocean-600 font-medium">about</a> and
  <a href="/contact" class="text-ocean-600 font-medium">contact</a>. Site apex:
  <a href="{APEX}/" class="text-ocean-600 font-medium">{APEX}/</a>.
</p>
''')}
"""
    meta: Meta = {
        "title": f"Methodology | {SITE}",
        "description": f"How {SITE} researches and organises Grenada cruise shore excursion planning guides.",
        "canonical_path": "/methodology",
        "page_id": "methodology",
        "og_image": INTRO,
    }
    return hero, main, None, meta


def not_found() -> PageTuple:
    hero = ""
    main = f"""
<section class="pt-28 pb-24 bg-white">
  <div class="max-w-xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="section-label justify-center">404</p>
    <h1 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Page not found</h1>
    <p class="text-gray-600 leading-relaxed mb-8">
      That URL is not part of the {SITE} guide. Try the excursions hub or port guide.
    </p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="/" class="btn-ocean inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Home</a>
      <a href="/best-grenada-shore-excursions" class="inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm border border-ocean-200 text-ocean-700">Excursions</a>
      <a href="/grenada-cruise-port-guide" class="inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm border border-ocean-200 text-ocean-700">Port guide</a>
    </div>
  </div>
</section>
"""
    meta: Meta = {
        "title": f"Page not found | {SITE}",
        "description": f"The requested page was not found on {SITE}.",
        "canonical_path": "/404.html",
        "page_id": "not-found",
        "og_image": INTRO,
    }
    return hero, main, None, meta
