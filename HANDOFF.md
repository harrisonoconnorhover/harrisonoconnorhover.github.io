# Morning Handoff

## Finished

- Preserved the clean first screen and existing project and social links.
- Added a sticky `Resume ↓` link and a below-the-fold experience section.
- Added one-time scroll reveals for experience, Dander, skills, and education, plus stacked mobile layouts and reduced-motion support.
- Added a public résumé PDF without a phone number, email address, or location.
- Connected the site to `harrisonoconnorhoover.com` with `www` support.

## Try It

- Visit `https://harrisonoconnorhoover.com/`.
- Select `Resume ↓`, then continue scrolling through the entries.
- Use `Download resume (PDF)` for the one-page printable version.

## Checks

- `node --check script.js` passed.
- `git diff --check` passed.
- Browser checks passed at desktop, 390 px, and 320 px widths with no console errors or horizontal overflow.
- The one-page PDF was rendered and visually inspected.
- Porkbun DNS was verified with all GitHub Pages A/AAAA records and the `www` CNAME; its parking records were removed.
- GitHub Pages built successfully, approved the apex/`www` certificate, and has HTTPS enforcement enabled.
- Live checks passed: the apex returns 200, while `www` and the prior GitHub Pages URL redirect to the apex.

## Decisions

- Kept the résumé below the first viewport so the landing page remains sparse.
- Kept personal contact details out of the public PDF; the website, GitHub, and LinkedIn remain.
- Made the apex custom domain canonical, with `www` routed to the same GitHub Pages site.

## Remaining

- None for the requested scope.

## Review First

- Open the PDF download and confirm the public-contact treatment.
- Try the reveal on a phone-sized viewport.
- Open the apex and `www` URLs once from your usual browser bookmarks.
