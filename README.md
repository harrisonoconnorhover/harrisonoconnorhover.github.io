# Harrison O'Connor-Hoover — personal site

A dependency-free static portfolio at [harrisonoconnorhoover.com](https://harrisonoconnorhoover.com/). GitHub Pages serves `main` from the repository root. HTML and CSS provide the content; a small script reveals resume entries when they enter the viewport and respects reduced-motion preferences.

The selected work is a compact list of links to GTM Control Tower, Pomade, and Hot Potato. Experience follows directly below the introduction; detailed workflow notes, source, and dated evidence follow the resume. Dander remains an additional project. Synthetic examples, historical development-system results, and private hosted access are labeled explicitly.

## Preview

```bash
python3 -m http.server 4198 --bind 127.0.0.1
```

Open [localhost:4198](http://127.0.0.1:4198/). Check the project notes, Resume link, and PDF at desktop and phone widths. There is no build step.

## Public resume

The experience and skills in `index.html` follow the approved September 24 GTM Engineering resume. Preserve contribution language, timeframes, and independent-project boundaries when editing.

`assets/Harrison_OConnor-Hoover_Resume.pdf` is a public derivative. It omits phone, email, and location; it is not the private application master. The private DOCX/PDF pair and submitted application copies stay outside this repository.

With Python and ReportLab installed, rebuild the public PDF from the HTML resume section:

```bash
python3 scripts/build_public_resume.py
```

Render and inspect the one-page result after editing. Verify the website, GitHub, LinkedIn, and project links and confirm no private contact information was included.

## Publish

Push the reviewed commit to `main`, then check GitHub Pages and the live site:

```bash
gh api repos/harrisonoconnorhover/harrisonoconnorhover.github.io/pages/builds/latest
```

Keep `CNAME` and existing DNS unchanged. See [HANDOFF.md](HANDOFF.md) for the latest verification.
