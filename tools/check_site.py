#!/usr/bin/env python3
"""Checks the built site. Standard library only.

    python3 tools/check_site.py             structure, links, translations
    python3 tools/check_site.py --release   the same, plus: no placeholder left
    python3 tools/check_site.py --live      the published site (after deploying)
"""

import hashlib
import json
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CONF = json.loads((ROOT / "site.json").read_text("utf-8"))
BASE = CONF["baseUrl"].rstrip("/") + "/"
# The only pages outside the site, linked from the privacy policy.
EXTERNAL = {"https://firebase.google.com/support/privacy", "https://policies.google.com/privacy"}
LANGS = ("en", "fr", "ar")
PAGES = [p + n for p in ("", "fr/", "ar/") for n in ("index.html", "faq.html", "contact.html", "privacy.html")]
errors = []


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.meta, self.alt, self.root = [], [], {}, {}, {}
        self.title, self.canonical, self.h1, self._in_title, self.no_alt = "", "", 0, False, 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.root = a
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "a":
            self.links.append(a.get("href", ""))
        if tag in ("img", "script") and a.get("src"):
            self.links.append(a["src"])
        if tag == "img" and "alt" not in a:
            self.no_alt += 1
        if tag == "link":
            if a["rel"] == "canonical":
                self.canonical = a["href"]
            elif a["rel"] == "alternate":
                self.alt[a["hreflang"]] = a["href"]
            else:
                self.links.append(a["href"])
        if tag == "meta":
            self.meta[a.get("name") or a.get("property")] = a.get("content")
        self.h1 += tag == "h1"
        self._in_title = tag == "title"

    def handle_data(self, data):
        if self._in_title:
            self.title += data

    def handle_endtag(self, tag):
        self._in_title = False


def err(where, msg):
    errors.append(f"{where}: {msg}")


def local(path):
    path = unquote(path)
    return path + "index.html" if path == "" or path.endswith("/") else path


def check():
    pages = {p: Page((DOCS / p).read_text("utf-8")) for p in PAGES + ["404.html"]}
    mailto = f"mailto:{CONF['supportEmail']}?"
    for name, p in pages.items():
        own = urljoin(BASE, name)
        if len(p.ids) != len(set(p.ids)):
            err(name, "duplicate ids")
        if p.h1 != 1:
            err(name, f"{p.h1} h1")
        if p.no_alt:
            err(name, "image without alt")
        for link in p.links:
            if link in EXTERNAL and "privacy" in name or link.startswith(mailto):
                continue
            target = urljoin(own, link)
            if not target.startswith(BASE):
                err(name, f"unexpected link {link}")
                continue
            parts = urlsplit(target[len(BASE):])
            file = local(parts.path)
            if not (DOCS / file).is_file():
                err(name, f"broken link {link}")
            elif parts.fragment and parts.fragment not in pages[file].ids:
                err(name, f"missing anchor {link}")
        if name == "404.html":
            continue
        lang = name[:2] if name[:3] in ("fr/", "ar/") else "en"
        if p.root.get("lang") != lang or p.root.get("dir") != ("rtl" if lang == "ar" else "ltr"):
            err(name, "wrong lang/dir")
        if set(p.alt) != {*LANGS, "x-default"} or p.alt[lang] != p.canonical:
            err(name, "hreflang/canonical")
        for href in {*p.alt.values(), p.canonical, p.meta["og:image"]}:
            if not href.startswith(BASE) or not (DOCS / local(href[len(BASE):])).is_file():
                err(name, f"bad absolute URL {href}")
        if not p.title or not 50 <= len(p.meta.get("description") or "") <= 260:
            err(name, "title/description")
        if "privacy.html" not in p.links:
            err(name, "no privacy link")
        if ("faq" not in name) and not any(link.startswith(mailto) for link in p.links):
            err(name, "no email link")
    for kind in ("index", "faq", "contact", "privacy"):
        same = {tuple(pages[f"{d}{kind}.html"].ids) for d in ("", "fr/", "ar/")}
        if len(same) != 1:
            err(kind, "ids differ between languages")
    return len(pages)


def release():
    bad = ("SUPPORT_EMAIL_TO_BE_PROVIDED", "is-placeholder\"", "TODO", "example.com", "[YOUR", "[DEVELOPER", "{email}", "{site}", "docs.google")
    for f in DOCS.rglob("*.html"):
        text = f.read_text("utf-8")
        for b in bad:
            if b in text:
                err(f.relative_to(DOCS), f"placeholder {b!r}")


def live():
    files = [f for f in DOCS.rglob("*") if f.is_file() and not f.name.startswith(".")]
    for f in files:
        name = f.relative_to(DOCS).as_posix()
        url = BASE + (name[: -len("index.html")] if name.endswith("index.html") else name)
        code, body = fetch(url)
        if code != 200:
            err(url, f"HTTP {code}")
        elif hashlib.sha256(body).digest() != hashlib.sha256(f.read_bytes()).digest():
            err(url, "published content differs from this folder (not deployed yet, or cached: wait 10 min)")
    if fetch(BASE + "no-such-page")[0] != 404:
        err(BASE, "missing pages should answer 404")
    print(f"{len(files)} published files compared")


def fetch(url):
    # curl, because the python.org Python on macOS often has no CA certificates.
    out = subprocess.run(["curl", "-sS", "--max-time", "20", "-w", "\n%{http_code}", url], capture_output=True)
    body, _, code = out.stdout.rpartition(b"\n")
    return int(code or 0), body


if __name__ == "__main__":
    n = check()
    if "--release" in sys.argv or "--live" in sys.argv:
        release()
    if "--live" in sys.argv:
        live()
    print(f"{n} pages checked")
    for e in errors:
        print("ERROR", e)
    print("FAILED" if errors else "OK")
    sys.exit(bool(errors))
