# Muslim Prayer – support website

Static site for GitHub Pages in English, French and Arabic (right to left).
Plain HTML and CSS, a few lines of optional JavaScript, system fonts. No
backend, cookies, analytics or third-party requests.

| Path | What |
|---|---|
| `site.json` | Site address, **support email** |
| `content/en.py` `fr.py` `ar.py` | All texts. Same keys in the three files; the build stops if they differ |
| `content/privacy.py` | Privacy policy in the three languages (English is the reference) and its date |
| `build.py` | Builds `docs/` (Python 3 standard library only) |
| `docs/` | The published site. HTML is generated; `docs/assets/` is edited by hand |
| `tools/preview.py` | Local preview at the same sub-path as GitHub Pages |
| `tools/check_site.py` | Links, anchors, languages, metadata; `--release`; `--live` |
| `DEPLOYMENT.md` | How to publish and verify |

Change a text or the email, then:

```bash
python3 build.py && python3 tools/check_site.py
```

```bash
python3 tools/preview.py
```

The answers describe Muslim Prayer **1.0.0 for iPhone** (no Quran recitation,
no ads). Review the FAQ with each app version.

Icon and pattern: the app's "Khatam Seal" icon. `docs/assets/home-*.webp`:
the app's iPhone Simulator captures (home screen), resized, not retouched.
