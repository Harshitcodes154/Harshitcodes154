# Install the command center

The package is ready to place in **Harshitcodes154/Harshitcodes154**. That repository already exists. Back up its current README and workflow files, then copy the **contents** of this package into its root. Do not nest the package inside another `Harshitcodes154` folder.

GitHub displays a public repository's root `README.md` on the account profile when the repository name exactly matches the username. [GitHub's profile README instructions](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)

## Upload

1. Open [the profile repository](https://github.com/Harshitcodes154/Harshitcodes154).
2. Put `README.md`, `assets/`, `scripts/`, `docs/` and `.github/workflows/update-activity.yml` at its root. Preserve the leading dot in `.github`.
3. Commit the files to the repository's default branch. No application deployment, package installation or server is needed to display the profile.
4. Open [the profile](https://github.com/Harshitcodes154). Verify the hero, all five projects, the contribution grid, the resume and contact buttons.
5. Open **Actions → Refresh real GitHub activity → Run workflow**. The supplied workflow also schedules a refresh at **03:23 UTC / 08:53 IST** daily. Enable Actions if the repository has disabled them.

No files were pushed to GitHub during preparation. The included first contribution snapshot is already real and renders immediately. The workflow starts refreshing it after you upload and enable it. Scheduled jobs may run late or stop after repository inactivity; the visible snapshot date makes stale data apparent.

The workflow uses GitHub's automatic token and `contents: write`; no personal access token is required. If your repository restricts workflow commits or protects the default branch, allow the workflow through your existing repository policy or run the script locally and commit the generated files yourself. Do not disable branch protections just to make this work.

## Folder map and exact references

See [ASSET-MAP.md](ASSET-MAP.md) for every filename, purpose, exact README line reference and the complete folder tree. Paths and capitalization are significant on GitHub.

`PREVIEW.html` is a local, static review copy. It can be opened in a browser; it does not need to be hosted or uploaded for the profile to work. Its surrounding styles approximate GitHub's Markdown layout. GitHub controls the actual profile font, margins and theme.

## Photo: already installed

- `assets/profile/original-headshot.jpeg` is your original, unchanged upload.
- `assets/profile/cinematic-headshot.png` is the cinematic lighting/background edit used in the generated hero images.
- `assets/hero.png` is the desktop composition; `assets/hero-mobile.png` is the mobile composition. The README's `<picture>` selects the mobile layout at widths up to 600px. If a client ignores `<picture>`, it still receives the desktop fallback.

You do **not** need to place the photo again. The portrait is baked into the PNG hero, so GitHub does not need to load external images from inside an SVG. Your original photo remains available as a rebuild source. [Portrait method and prompt](PORTRAIT.md)

To use a new portrait, replace `assets/profile/cinematic-headshot.png`, then rebuild the hero with Node.js and Sharp installed:

```sh
npm install --no-save sharp
node scripts/build_assets.cjs
```

To use the unchanged original photograph inside the same frame:

```sh
node scripts/build_assets.cjs --photo=assets/profile/original-headshot.jpeg
```

These commands are optional authoring tools; README viewers never run JavaScript. The builder also regenerates the primary UI cards. RazorRecover and Ashoka Cooling Point are directly editable SVG sources and are retained by the builder. Re-run `python scripts/build_package.py` after edits to refresh the low-motion copy and line map.

## Resume: already installed

`assets/resume/Harshit-Kumar-Resume.pdf` is a byte-identical copy of your supplied `latest_mine.pdf`. Both download buttons and the text link use this local file, with no placeholder URL.

To update it later, replace that PDF under the same filename and commit. No README link changes are needed. Update its SHA-256 in `docs/EVIDENCE.md` and `expected_resume_hash` in `scripts/verify_package.py` after an intentional replacement. The supplied resume still says “Null Matrix CTF”; the new profile uses your corrected name, **Null Chapter CTF**. The original PDF was intentionally preserved.

## Update later

| Change | Edit / command |
| :--- | :--- |
| Bio, education, skills or achievement | Edit native text in `README.md`. Keep claims grounded in source or your records. |
| Project description / links | Edit its README module; update the matching SVG if the title or short label changes. |
| WAFER / ThermoWatch / Operation / primary UI art | Edit `scripts/build_assets.cjs`, then run `node scripts/build_assets.cjs`. |
| RazorRecover / Ashoka art | Edit the matching SVG in `assets/projects/` and its static counterpart. |
| Boot or deep-scan animation | Edit `scripts/build_motion.py`; install Pillow, then run `python scripts/build_motion.py`. |
| Contribution data | Run `python scripts/update_activity.py`, or dispatch the included workflow. |
| Resume | Replace the existing PDF. |
| Photo | Replace the photo and rebuild the hero as above. |
| Low-motion profile / exact line map | Run `python scripts/build_package.py` after editing the README or asset set. |

The motion builder uses Consolas on Windows, with DejaVu Sans Mono as a Linux fallback. Set `PROFILE_MONO_FONT` to a local `.ttf` path if neither is available. `build_assets.cjs` uses installed system fonts and Sharp. Neither generator is needed to use the delivered assets.

The activity updater needs only Python's standard library and outbound HTTPS. It reads GitHub's public calendar and REST metadata. It rejects incomplete or inconsistent data and retains the previous snapshot if a fetch or validation fails. [Evidence and metric definitions](EVIDENCE.md)

## Animation and client behavior

The boot and deep-scan sequences are GIFs. Project modules, status indicators and the engineering path use script-free animated SVG. No JavaScript, React, Canvas, external stylesheet or third-party stats-image service is required by the README.

SVGs contain complete readable static states and honor `prefers-reduced-motion` where the viewer supports it. Some GitHub clients/proxies may freeze SVG motion or GIF playback; the information still renders. GIFs do not reliably honor reduced-motion preferences, so the footer provides a [low-motion profile](STATIC-PROFILE.md) with static assets. Essential descriptions are also native Markdown for mobile readability and accessibility.

The contribution calendar is deliberately a normal, readable GitHub-style grid. The optional 3D view was omitted to avoid adding an unverified service dependency.

## Verification before publishing

See [VERIFICATION.md](VERIFICATION.md). Local desktop/mobile layout and files were checked. GitHub-hosted image proxy behavior, workflow permissions and live app inference must be verified after upload; the package does not claim they were tested remotely.
