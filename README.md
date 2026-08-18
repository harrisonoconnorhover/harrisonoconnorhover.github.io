# Harrison O'Connor-Hoover — personal site

A tiny, dependency-free static website designed for GitHub Pages. It uses one HTML file and one CSS file—no images, JavaScript, build step, or hosting bill.

## Publish with GitHub Pages

1. Create a GitHub repository. For the default personal URL, name it `YOUR-USERNAME.github.io`.
2. Add `index.html` and `style.css` to the repository's root.
3. Open the repository's **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**, then select the `main` branch and `/ (root)` folder.
5. Save. GitHub will publish the site at the repository's Pages URL.

To connect a custom domain later, use the **Custom domain** field on the same Pages settings screen, then add the DNS records requested by GitHub at your domain registrar.

## Local preview

Open `index.html` directly in a browser, or run a local server from this directory:

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.
