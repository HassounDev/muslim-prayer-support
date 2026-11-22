# Publishing on GitHub Pages

Address: `https://hassoundev.github.io/muslim-prayer-support/`
(account `HassounDev`, repository `muslim-prayer-support`). Live since
2026-11-22; steps 1 to 4 are kept for reference.

## 1. Support email (done)

Set in `site.json`, and public on the site. After changing it:

```bash
python3 build.py && python3 tools/check_site.py --release
```

It must end with `OK` (it fails while a placeholder remains).

## 2. Repository (done)

<https://github.com/HassounDev/muslim-prayer-support>, public (GitHub Free
publishes Pages only from public repositories), created empty. The app's own
repository stays private.

Commits use GitHub's noreply address, so they do not carry a personal one.

## 3. Commit and push this folder

```bash
cd ~/Desktop/muslim-prayer-support && git init -b main
```

```bash
git config user.email "29431713+HassounDev@users.noreply.github.com"
```

```bash
git add . && git status --short
```

```bash
git commit -m "Muslim Prayer support website"
```

```bash
git remote add origin https://github.com/HassounDev/muslim-prayer-support.git && git push -u origin main
```

Check the author before pushing with `git log -1 --format='%an <%ae>'`.

## 4. Turn on Pages

In the repository: Settings › Pages › Build and deployment › Source **Deploy
from a branch** › Branch **main**, folder **/docs** › Save. Keep **Enforce
HTTPS** on. No workflow is needed; `docs/.nojekyll` serves the files as they
are. The first publication takes a few minutes (Actions tab: "pages build and
deployment").

## 5. Verify the public URL

```bash
python3 tools/check_site.py --live
```

`OK` means every file answers HTTP 200, is identical to this folder, and
missing pages answer 404. Then, in a private browser window and on a phone:

- <https://hassoundev.github.io/muslim-prayer-support/>, `/fr/` and `/ar/`
  open over HTTPS without signing in; Arabic is right to left;
- the language selector keeps the same page;
- the email link opens a new message to the right address; send yourself one;
- the Privacy Policy opens, with the right date and contact email.

## 6. App Store Connect (after step 5 only)

| Locale | Support URL |
|---|---|
| en-US, es-ES, it, de-DE | `https://hassoundev.github.io/muslim-prayer-support/` |
| fr-FR | `https://hassoundev.github.io/muslim-prayer-support/fr/` |
| ar-SA | `https://hassoundev.github.io/muslim-prayer-support/ar/` |

Privacy Policy URL (all locales, and `AppLinks.privacyPolicy` in the app; a test
keeps them identical): `https://hassoundev.github.io/muslim-prayer-support/privacy.html`.
Keep this address stable: published app versions link to it. Versions that link
to the Google Doc need that document to stay online and up to date.

In the app repository the support URLs belong in
`docs/app-store/metadata/<locale>/support_url.txt` (now `TODO_SUPPORT_URL`).

## Later

- **Privacy policy**: edit `content/privacy.py` in the three languages and change
  `UPDATED`.
- **Update**: edit, `python3 build.py`, `python3 tools/check_site.py --release`,
  commit, push; Pages republishes (caches last up to about 10 minutes).
- **Other address or custom domain**: change `baseUrl` in `site.json` and
  rebuild (canonical links, hreflang, sitemap and the 404 page use it).
- **Unpublish**: Settings › Pages › Unpublish site.
