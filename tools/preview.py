#!/usr/bin/env python3
"""Local preview that behaves like GitHub Pages (same sub-path, 404 page).

    python3 tools/preview.py   ->  http://localhost:8791/muslim-prayer-support/
"""

import json
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BASE = urlsplit(json.loads((ROOT / "site.json").read_text("utf-8"))["baseUrl"]).path.rstrip("/")
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8791


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        parts = urlsplit(path)
        if not parts.path.startswith(BASE + "/"):
            return str(DOCS / "__missing__")
        return super().translate_path(parts.path[len(BASE):])

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_error(self, code, message=None, explain=None):
        if code != 404:
            return super().send_error(code, message, explain)
        body = (DOCS / "404.html").read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print(f"http://localhost:{PORT}{BASE}/", flush=True)
    ThreadingHTTPServer(("127.0.0.1", PORT), partial(Handler, directory=str(DOCS))).serve_forever()
