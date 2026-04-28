# ICRP CT Dose Calculator JavaScript Version

This folder contains the standalone JavaScript/HTML version and the data files it needs.
The app prefers the generated `.f64` binary tables for faster startup and falls back to
the CSV files if those binaries are unavailable.

For GitHub Pages deployment, publish this folder and open the site root.
GitHub Pages will serve `index.html` automatically.

For local testing, run it with a local web server from this folder:

```sh
python3 -m http.server 8000
```

Then open:

```text
http://127.0.0.1:8000/
```

Do not open the HTML directly with `file://`, because browsers block loading the data files that way.

If any CSV data file changes, regenerate the binary tables before publishing:

```sh
python3 tools/build-data-binaries.py
```
