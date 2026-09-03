# Morning Handoff

## Finished

- Preserved the clean first screen and existing project and social links.
- Added a sticky `Resume ↓` link and a below-the-fold experience section.
- Added one-time scroll reveals for experience, Dander, skills, and education.
- Added a public résumé PDF without a phone number, email address, or location.
- Added stacked mobile layouts and reduced-motion support.

## Try It

- Visit `https://harrisonoconnorhover.github.io/`.
- Select `Resume ↓`, then continue scrolling through the entries.
- Use `Download resume (PDF)` for the one-page printable version.

## Checks

- `node --check script.js` passed.
- `git diff --check` passed.
- Browser checks passed at desktop, 390 px, and 320 px widths with no console errors or horizontal overflow.
- The one-page PDF was rendered and visually inspected.

## Decisions

- Kept the résumé below the first viewport so the landing page remains sparse.
- Used a restrained 24 px, 760 ms one-time reveal rather than copying the reference motion literally.
- Kept personal contact details out of the public PDF; the website, GitHub, and LinkedIn remain.

## Remaining

- None for the requested scope.

## Review First

- Review the AxisCare and REVGEN wording on the live page.
- Open the PDF download and confirm the public-contact treatment.
- Try the reveal on a phone-sized viewport.
