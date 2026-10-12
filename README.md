# Tech X-Ray — Interactive learning lab v1.0

**See beyond the headline.** Investigate the capabilities, dependencies, limits and stakeholders of emerging technologies. Designed as a short interactive activity for learning about systems, technological change and Contextual Adaptation.

## Launch locally — no installation required

Unzip and **double-click `index.html`** to open the app in a modern browser. Everything needed is inside this folder: no Python installation, API key, external library or internet required. On Windows, if you have Python installed, you can instead double-click **`Preview_on_Windows.bat`**; this starts a local preview server in your browser, which is more reliable for saving local history. For the optional offline PWA/service-worker behaviour, serve the folder locally with Python's standard library:

```sh
python -m http.server 8000
```

Then visit `http://localhost:8000/`. The app is still a static HTML/CSS/JavaScript website. GitHub Pages **does not run Python server-side**. Python is provided only to maintain editable challenge content or serve local files for testing.

## Deploy the same project to GitHub Pages

1. Create a **public** repository named `Tech-XRay` at `https://github.com/new`.
2. Extract the supplied project ZIP. Upload **the files inside the folder** directly to the repository root, **not the containing folder**. The root should include `index.html`, `dv-project.json`, `README.md`, `sw.js`, `manifest.webmanifest` and `assets/`.
3. Commit on `main`.
4. Under **Settings → Pages**, choose **Deploy from a branch → main → /(root)**, then save.
5. If using the `dvexperiments` GitHub user and exact repo name `Tech-XRay`, the eventual expected URL is `https://dvexperiments.github.io/Tech-XRay/` (confirm in GitHub Pages settings).
6. The root-level **`dv-project.json`** follows the DV Experiments dashboard metadata structure. It has a cover image, `visible: true` and `embed: true`. Your dashboard should discover a public repo with this metadata if its repository autosync is enabled. If it does not, confirm the repo is public, that `dv-project.json` is in the root and that Pages deployment succeeded.

**Important**: The existing dashboard is a separate repository. Do **not** upload these files over your dashboard files.

## What learners do

1. Select from **12 technologies** and one of four settings: Education & learning, Workplace & business, Community & public life, or Environment & place.
2. **Sort 12 evidence cards** into four X-Ray layers: **What it does** (capabilities), **What it needs** (dependencies), **What limits it** (constraints), **Who it affects** (stakeholders). Drag/drop or use each card's dropdown. All cards must be placed before step 2.
3. Choose **up to three dependencies to check first** from the items you classified as needs. Consider four prompts about potential applications, verification, risk and inclusion.
4. **Reveal the hidden layer**: inspect three extra dependencies withheld from the first stage, a breakdown of the 100-point formative practice score, and explanations for each evidence card's reference category.
5. Use **History** to revisit drafts/reviews, export Markdown notes, or back up and restore all attempts as JSON.

### Scoring, limits and learning goals

The **formative score** is deliberately transparent:

- 60 points: 5 points for each of 12 evidence cards placed in its reference layer.
- 15 points: 5 points for each of three curated reference high-priority dependencies included in the learner's first three choices.
- 25 points: for four reflection prompts, each with at least 35 non-whitespace characters, rounded as a group.

The app does **not** evaluate factual correctness of written responses, creativity, ethics, sector fit or validity of a proposed deployment. Multiple priorities and classifications may be reasonable in real contexts, and the hidden requirements are prompts, not exhaustive risk registers. A real application requires evidence, domain expertise, consultation and testing.

### Privacy and storage

No accounts, tracking, analytics, remote storage, AI model calls or API keys. History and reflections use browser `localStorage` for the same site and device. Clearing browser data or using another device removes access to saved work unless a **Backup JSON** was downloaded and restored. If run from a `file://` path, storage behaviour can vary across browsers; for reliable persistence use a local server or the GitHub Pages address. Do not enter sensitive personal information.

## Edit the content

- **Content library**: `assets/content.json`. Each technology has 12 cards with `layer`, `why` and `critical` fields, plus 3 `blindspots` shown at the end.
- To republish the browser version after modifying `assets/content.json`, rebuild `assets/content.js` using a Python one-liner that converts the JSON to `window.TECH_XRAY_CONTENT = ...;`, or edit `tools/build_content.py` (the *authoritative* Python content authoring script) and run it with `python tools/build_content.py` to regenerate both files.
- **Styles**: `assets/styles.css`.
- **Interface and storage**: `assets/app.js`.
- **Scoring and export**: `assets/engine.js`.
- **Dashboard card**: `dv-project.json`.
- **Offline cache version**: bump `CACHE` in `sw.js` after publishing changes.

## Project files

```text
index.html               Web app entry (upload to repo root)
dv-project.json          DV Experiments dashboard metadata
assets/app.js            App interface, drag/drop, history, exports
assets/engine.js         Pure offline scoring and learning logic
assets/content.json      Editable technology library
assets/content.js        Browser-ready embedded copy of library
assets/styles.css        Responsive UI
assets/cover.svg         Dashboard cover art
assets/icon.svg          App icon
manifest.webmanifest     Optional installable web app
sw.js                    Optional repeat/offline cache over HTTP(S)
tools/build_content.py   Source authoring script, standard Python only
preview.py               Optional standard-library local preview server
Preview_on_Windows.bat    Double-click launcher for Windows preview
tests/                  Browser/engine smoke tests
DEPLOY_QUICK_START.txt   Short deployment instructions
.nojekyll                Optional GitHub Pages compatibility
LICENSE                  MIT
```

### Accessibility and caveats

Card dropdowns are accessible without drag-and-drop, and input fields and buttons are keyboard reachable. The app uses visible focus indicators and includes a reduced-motion media query. Scoring is formative rather than a definitive evaluation of complex technological systems. Educational scenarios are illustrative and should be checked against current evidence when used for a real decision.
