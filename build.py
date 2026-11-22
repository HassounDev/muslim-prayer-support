#!/usr/bin/env python3
"""Builds the static site in docs/ from site.json and content/*.py.

Python 3 standard library only:  python3 build.py
Files in docs/assets/ are static and are not touched."""

import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True
from content import ar, en, fr  # noqa: E402

CONF = json.loads((ROOT / "site.json").read_text("utf-8"))
BASE = CONF["baseUrl"].rstrip("/")
BASE_PATH = urlsplit(BASE).path  # "/muslim-prayer-support", "" on a root domain
EMAIL = CONF["supportEmail"]
PRIVACY = CONF["privacyPolicyUrl"]
EMAIL_READY = re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", EMAIL) is not None

LANGS = {"en": en.T, "fr": fr.T, "ar": ar.T}
DIRS = {"en": "", "fr": "fr/", "ar": "ar/"}
PAGES = {"home": "", "faq": "faq.html", "contact": "contact.html"}

# Order of the FAQ. The ids are anchors (faq.html#adhan-30s): keep them stable,
# they can be used in support replies.
FAQ = [
    ("prayer-times", ["how-calculated", "methods", "mosque", "asr", "estimated",
                      "umm-al-qura-ramadan", "travel", "timetable"]),
    ("location-privacy", ["what-location", "without-permission", "not-found",
                          "what-is-sent", "change-delete"]),
    ("notifications", ["turn-on", "choose-sound", "adhan-30s", "no-sound",
                       "stopped", "reminders"]),
    ("qibla", ["how-to-use", "wrong", "north", "no-compass", "near-makkah"]),
    ("quran", ["text", "offline", "translation-audio", "find", "share"]),
    ("adhkar", ["adhkar-source", "adhkar-language", "counting", "tasbih"]),
    ("hijri", ["calendar", "differs", "maghrib", "ramadan", "fasting"]),
    ("general", ["language", "account-ads", "internet"]),
]

STAR = ('<svg class="star" viewBox="0 0 24 24" aria-hidden="true"><path d="M16.6 '
        '.9l1.9 4.6 4.6 1.9L21.2 12l1.9 4.6-4.6 1.9-1.9 4.6L12 21.2l-4.6 1.9-1.9-4.6'
        'L.9 16.6 2.8 12 .9 7.4l4.6-1.9L7.4.9 12 2.8z"/></svg>')


def check_content():
    ids = [q for _, qs in FAQ for q in qs]
    assert len(ids) == len(set(ids)), "duplicate FAQ id"
    ref = LANGS["en"]
    for lang, t in LANGS.items():
        assert t.keys() == ref.keys(), (lang, t.keys() ^ ref.keys())
        assert set(t["cats"]) == {c for c, _ in FAQ}, (lang, "cats")
        assert set(t["faq"]) == set(ids), (lang, set(t["faq"]) ^ set(ids))
        for q in ids:
            shape = [p.startswith("- ") for p in t["faq"][q][1]]
            assert shape == [p.startswith("- ") for p in ref["faq"][q][1]], (lang, q)
        for key in ("features", "note", "contact_include"):
            assert len(t[key]) == len(ref[key]), (lang, key)


def typo(text, lang):
    if lang == "fr":
        text = re.sub(r" ([:;?!»›])", "\u00a0\\1", text).replace("« ", "«\u00a0")
        # "Puis-je", "différent-ils", "Y a-t-il": no line break at the hyphen.
        text = re.sub(r"-(?=(?:t-)?(?:ils?|elles?|je|ce)\b)", "\u2011", text)
        text = re.sub(r"-t(?=\u2011)", "\u2011t", text)
    if lang == "ar":
        # Menu paths stay right to left even between two Latin names.
        text = text.replace(" › ", "\u200f › \u200f")
        # Latin runs at a sentence end must not drag the full stop with them.
        text = re.sub(r"([A-Za-z0-9])([.:،؛])(?=\s|$)", "\\1\u200f\\2", text)
    return text


def inline(text, lang):
    text = html.escape(typo(text, lang), quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)


def attr(text, lang):
    return html.escape(typo(text, lang), quote=True)


def blocks(paragraphs, lang):
    out, items = [], []

    def flush():
        if items:
            out.append("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>")
            items.clear()

    for p in paragraphs:
        if p.startswith("- "):
            items.append(inline(p[2:], lang))
        else:
            flush()
            out.append(f"<p>{inline(p, lang)}</p>")
    flush()
    return "\n".join(out)


def url(lang, page):
    return f"{BASE}/{DIRS[lang]}{PAGES[page]}"


def rel(src_lang, dst_lang, page):
    """Relative link, so the site works under any path and domain."""
    up = "../" if DIRS[src_lang] else ""
    path = PAGES[page] if src_lang == dst_lang else up + DIRS[dst_lang] + PAGES[page]
    return path or "./"


def mail_href(lang):
    return f"mailto:{quote(EMAIL, safe='@+._-')}?subject={quote(LANGS[lang]['mail_subject'])}"


def email_link(lang, cls="email"):
    t = LANGS[lang]
    extra = "" if EMAIL_READY else " is-placeholder"
    note = "" if EMAIL_READY else f'<span class="placeholder-note">{inline(t["placeholder_notice"], lang)}</span>'
    return (f'<a class="{cls}{extra}" href="{html.escape(mail_href(lang))}"><bdi dir="ltr">'
            f"{html.escape(EMAIL)}</bdi></a>{note}")


def privacy_link(lang, cls=""):
    t = LANGS[lang]
    return (f'<a class="{cls}" href="{html.escape(PRIVACY)}" rel="noopener noreferrer">{inline(t["privacy_link"], lang)}</a>'
            f'<span class="hint">{inline(t["privacy_hint"], lang)}</span>')


def lang_switch(lang, page):
    links = []
    for code, t in LANGS.items():
        cur = ' aria-current="true"' if code == lang else ""
        links.append(f'<li><a href="{rel(lang, code, page)}" lang="{code}" hreflang="{code}"'
                     f' dir="{"rtl" if code == "ar" else "ltr"}" data-lang-link{cur}>{t["name"]}</a></li>')
    return (f'<nav class="langs" aria-label="{attr(LANGS[lang]["nav_language"], lang)}"><ul>'
            + "".join(links) + "</ul></nav>")


def layout(lang, page, body):
    t = LANGS[lang]
    assets = ("../" if DIRS[lang] else "") + "assets"
    title, desc = t[f"{page}_title"], t[f"{page}_desc"]
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="{url(c, page)}">' for c in LANGS)
    og_alt = "\n".join(f'<meta property="og:locale:alternate" content="{o["og_locale"]}">'
                       for c, o in LANGS.items() if c != lang)

    def nav_item(key):
        cur = ' aria-current="page"' if key == page else ""
        return f'<li><a href="{rel(lang, lang, key)}"{cur}>{inline(t["nav_" + key], lang)}</a></li>'

    nav = "".join(nav_item(k) for k in PAGES)

    def privacy_item(key):
        return (f'<li><a href="{html.escape(PRIVACY)}" rel="noopener noreferrer">'
                f'{inline(t[key], lang)}</a></li>')

    return f"""<!doctype html>
<html lang="{lang}" dir="{"rtl" if lang == "ar" else "ltr"}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{attr(title, lang)}</title>
<meta name="description" content="{attr(desc, lang)}">
<link rel="canonical" href="{url(lang, page)}">
{alternates}
<link rel="alternate" hreflang="x-default" href="{url("en", page)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Muslim Prayer">
<meta property="og:title" content="{attr(title, lang)}">
<meta property="og:description" content="{attr(desc, lang)}">
<meta property="og:url" content="{url(lang, page)}">
<meta property="og:image" content="{BASE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Muslim Prayer">
<meta property="og:locale" content="{t["og_locale"]}">
{og_alt}
<meta name="twitter:card" content="summary_large_image">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#0D1F40">
<link rel="icon" href="{assets}/icon.svg" type="image/svg+xml">
<link rel="icon" href="{assets}/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{assets}/apple-touch-icon.png">
<link rel="stylesheet" href="{assets}/style.css">
<script src="{assets}/site.js" defer></script>
</head>
<body class="page-{page}">
<a class="skip" href="#main">{inline(t["skip"], lang)}</a>
<header class="top">
<div class="wrap top-in">
<a class="brand" href="{rel(lang, lang, "home")}"><img src="{assets}/icon.svg" width="36" height="36" alt=""><span><bdi>Muslim Prayer</bdi></span></a>
<nav class="main" aria-label="{attr(t["nav_main"], lang)}"><ul>{nav}{privacy_item("nav_privacy_header")}</ul></nav>
{lang_switch(lang, page)}
</div>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
<div class="wrap foot-in">
<p>{inline(t["footer_note"], lang)}<br><span class="copy">© {CONF["year"]} <bdi>Muslim Prayer</bdi></span></p>
<nav aria-label="{attr(t["nav_main"], lang)} (2)"><ul>{nav}{privacy_item("nav_privacy")}</ul></nav>
</div>
</footer>
</body>
</html>
"""


def home(lang):
    t = LANGS[lang]
    assets = ("../" if DIRS[lang] else "") + "assets"
    feats = "".join(f"<li>{STAR}<div><h3>{inline(a, lang)}</h3><p>{inline(b, lang)}</p></div></li>"
                    for a, b in t["features"])
    topics = "".join(
        f'<li><a href="{rel(lang, lang, "faq")}#{c}"><span>{inline(t["cats"][c], lang)}</span>'
        '<svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></a></li>'
        for c, _ in FAQ)
    return f"""<section class="hero">
<div class="wrap hero-in">
<div class="hero-text">
<p class="kicker">{inline(t["home_kicker"], lang)}</p>
<h1><bdi>{inline(t["home_h1"], lang)}</bdi></h1>
<p class="lead">{inline(t["home_lead"], lang)}</p>
<p class="actions"><a class="btn gold" href="{rel(lang, lang, "faq")}">{inline(t["home_btn_faq"], lang)}</a>
<a class="btn line" href="{rel(lang, lang, "contact")}">{inline(t["home_btn_contact"], lang)}</a></p>
</div>
<div class="phone"><img src="{assets}/home-{lang}.webp" width="560" height="1217" alt="{attr(t["home_shot_alt"], lang)}"></div>
</div>
</section>
<section class="wrap sec" aria-labelledby="topics">
<h2 id="topics">{inline(t["topics_title"], lang)}</h2>
<ul class="topics">{topics}</ul>
</section>
<section class="band" aria-labelledby="features">
<div class="wrap sec">
<h2 id="features">{inline(t["features_title"], lang)}</h2>
<ul class="features">{feats}</ul>
</div>
</section>
<section class="wrap sec duo">
<div class="note"><h2>{inline(t["note_title"], lang)}</h2>{blocks(t["note"], lang)}</div>
<div class="note plain"><h2>{inline(t["version_title"], lang)}</h2><p>{inline(t["version"], lang)}</p></div>
</section>
<section class="wrap sec duo last">
<div class="card" id="contact"><h2>{inline(t["contact_card_title"], lang)}</h2><p>{inline(t["contact_card"], lang)}</p>
<p>{email_link(lang)}</p></div>
<div class="card"><h2>{inline(t["privacy_card_title"], lang)}</h2><p>{inline(t["privacy_card"], lang)}</p>
<p>{privacy_link(lang, "strong")}</p></div>
</section>"""


def faq(lang):
    t = LANGS[lang]
    toc = "".join(f'<li><a href="#{c}">{inline(t["cats"][c], lang)}</a></li>' for c, _ in FAQ)
    secs = []
    for c, qs in FAQ:
        items = "".join(
            f'<details id="{q}"><summary><h3>{inline(t["faq"][q][0], lang)}</h3></summary>'
            f'<div class="answer">{blocks(t["faq"][q][1], lang)}</div></details>' for q in qs)
        extra = f'<p class="after">{privacy_link(lang, "strong")}</p>' if c == "location-privacy" else ""
        secs.append(f'<section id="{c}" aria-labelledby="h-{c}"><h2 id="h-{c}">{STAR}{inline(t["cats"][c], lang)}</h2>{items}{extra}</section>')
    return f"""<div class="pagehead"><div class="wrap"><h1>{inline(t["faq_h1"], lang)}</h1>
<p class="lead">{inline(t["faq_lead"], lang)}</p></div></div>
<div class="wrap faq">
<nav class="toc" aria-label="{attr(t["faq_toc"], lang)}"><h2>{inline(t["faq_toc"], lang)}</h2><ul>{toc}</ul></nav>
<div class="faq-body">
{"".join(secs)}
<div class="card"><h2>{inline(t["contact_card_title"], lang)}</h2><p>{inline(t["contact_card"], lang)}</p>
<p><a class="btn green" href="{rel(lang, lang, "contact")}">{inline(t["home_btn_contact"], lang)}</a></p></div>
</div>
</div>"""


def contact(lang):
    t = LANGS[lang]
    return f"""<div class="pagehead"><div class="wrap"><h1>{inline(t["contact_h1"], lang)}</h1>
<p class="lead">{inline(t["contact_lead"], lang)}</p></div></div>
<div class="wrap contact">
<div class="card mail"><p class="label">{inline(t["contact_email_label"], lang)}</p>
<p class="big">{email_link(lang)}</p>
<p><a class="btn green" href="{html.escape(mail_href(lang))}">{inline(t["contact_button"], lang)}</a></p></div>
<div class="contact-side">
<section><h2>{inline(t["contact_first_title"], lang)}</h2><p>{inline(t["contact_first"], lang)} <a href="{rel(lang, lang, "faq")}">{inline(t["home_btn_faq"], lang)}</a></p></section>
<section><h2>{inline(t["contact_include_title"], lang)}</h2>{blocks(t["contact_include"], lang)}</section>
<section><h2>{inline(t["contact_avoid_title"], lang)}</h2><p>{inline(t["contact_avoid"], lang)}</p></section>
<section><h2>{inline(t["privacy_card_title"], lang)}</h2><p>{inline(t["privacy_card"], lang)}</p><p>{privacy_link(lang, "strong")}</p></section>
</div>
</div>"""


def not_found():
    """GitHub Pages serves this for any missing path: absolute links only."""
    parts = "".join(
        f'<section lang="{c}" dir="{"rtl" if c == "ar" else "ltr"}"><h2>{inline(t["nf_title"], c)}</h2>'
        f'<p>{inline(t["nf_text"], c)}</p><p><a class="btn green" href="{BASE_PATH}/{DIRS[c]}">{inline(t["nf_link"], c)}</a></p></section>'
        for c, t in LANGS.items())
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>404 – Muslim Prayer</title>
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{BASE_PATH}/assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{BASE_PATH}/assets/style.css">
</head>
<body class="page-404">
<main class="wrap nf"><img src="{BASE_PATH}/assets/icon.svg" width="72" height="72" alt="Muslim Prayer">
<h1>404</h1><div class="nf-grid">{parts}</div></main>
</body>
</html>
"""


def sitemap():
    rows = []
    for page in PAGES:
        for lang in LANGS:
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{url(c, page)}"/>' for c in LANGS)
            rows.append(f"<url><loc>{url(lang, page)}</loc>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")


def main():
    check_content()
    render = {"home": home, "faq": faq, "contact": contact}
    for lang in LANGS:
        folder = OUT / DIRS[lang]
        folder.mkdir(parents=True, exist_ok=True)
        for page, name in PAGES.items():
            (folder / (name or "index.html")).write_text(layout(lang, page, render[page](lang)), "utf-8")
    (OUT / "404.html").write_text(not_found(), "utf-8")
    (OUT / "sitemap.xml").write_text(sitemap(), "utf-8")
    (OUT / ".nojekyll").write_text("", "utf-8")
    print(f"Built {len(LANGS) * len(PAGES)} pages + 404 + sitemap in {OUT}")
    if not EMAIL_READY:
        print("NOTE: supportEmail in site.json is still a placeholder - do not publish yet.")


if __name__ == "__main__":
    main()
