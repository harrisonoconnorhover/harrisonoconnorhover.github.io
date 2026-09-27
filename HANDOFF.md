# Morning Handoff

## Finished

- Updated Control Tower's existing comparison paragraph with a link to its read-only approximate match review.
- Described selectable suggested fields and evidence-based 0–100 scores, not probabilities. Suggestions do not merge or link records or approve writes.
- Retained the exact-email comparison link and synthetic/local testing and pending live development-account qualification boundaries.
- Preserved the existing workflows, historical evidence, other projects, resume HTML, and public PDF.

## Try It

Run `python3 -m http.server 4199 --bind 127.0.0.1` and open `http://127.0.0.1:4199/#project-notes`. Under Control Tower's **Compare with CRM** paragraph, find **read-only approximate match review**.

## Checks

- HTML IDs are unique; internal anchors and local assets resolve. Only the existing comparison paragraph differs in HTML; resume HTML and public PDF match the previous committed version. The new guide URL is exact.
- JavaScript syntax and diff checks passed. This dependency-free site has no build step.
- Local Chrome/Playwright checks passed at 1365px and 390px: HTTP 200, no horizontal overflow or page errors, intended link URL, score caveat, and qualification text. Both screenshots were visually inspected.
- No runtime tests, native CRM calls, or live publication checks were run for this site change.

## Decisions

- Edit the existing paragraph instead of adding a feature section.
- Keep approximate suggestions separate from exact-email write planning, probabilities, and automatic record changes.
- Preserve the self-hosted and simulated-verification boundaries.

## Remaining

- Hold public push until the approximate-match guide is confirmed published.
- Live development-account qualification of the new CRM comparison remains pending.

## Review First

- `index.html`: Control Tower's **Compare with CRM** paragraph.
- `docs/decisions.md`: approximate matching and verification boundaries.
- The linked `docs/approximate-import-matches.md` guide when published.
