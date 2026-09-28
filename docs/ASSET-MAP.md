# Exact folder and asset map

Generated from the final README. Line numbers are one-based. Run `python scripts/build_package.py` after future edits.

| Asset path from repository root | Purpose | README.md lines | docs/STATIC-PROFILE.md lines |
| :--- | :--- | :--- | :--- |
| `assets/achievements/ctf.svg` | Null Chapter CTF winner module | 144 | — |
| `assets/contribution/activity-source.json` | Exact normalized GitHub data and provenance | 166 | 166 |
| `assets/contribution/calendar.svg` | Real GitHub contribution calendar snapshot | 157 | 157 |
| `assets/contribution/stats.svg` | Repository metadata, language bytes and calendar-derived streaks | 159 | 159 |
| `assets/hero-mobile.png` | Mobile portrait/hero composition | 3 | 3 |
| `assets/hero.png` | Desktop hero: portrait, identity, terminal and status | 4 | 4 |
| `assets/profile/cinematic-headshot.png` | Cinematic portrait edit; hero rebuild input | Indirect: baked into hero at lines 3, 4 | — |
| `assets/profile/original-headshot.jpeg` | Unchanged uploaded photo; optional hero rebuild input | Indirect: baked into hero at lines 3, 4 | — |
| `assets/projects/ashoka-cooling-point.svg` | Ashoka Cooling Point project card | 98 | — |
| `assets/projects/operation-sindoor.svg` | Operation Sindoor project card | 72 | — |
| `assets/projects/razorrecover.svg` | Razorrecover project card | 84 | — |
| `assets/projects/thermowatch-ai.svg` | Thermowatch Ai project card | 58 | — |
| `assets/projects/wafer-gpt.svg` | Wafer Gpt project card | 34 | — |
| `assets/resume/Harshit-Kumar-Resume.pdf` | Actual supplied resume PDF; byte-identical copy | 8, 179, 181 | 8, 179, 181 |
| `assets/static/achievements/ctf.svg` | Static counterpart: Null Chapter CTF winner module | — | 144 |
| `assets/static/projects/ashoka-cooling-point.svg` | Static counterpart: Ashoka Cooling Point project card | — | 98 |
| `assets/static/projects/operation-sindoor.svg` | Static counterpart: Operation Sindoor project card | — | 72 |
| `assets/static/projects/razorrecover.svg` | Static counterpart: Razorrecover project card | — | 84 |
| `assets/static/projects/thermowatch-ai.svg` | Static counterpart: Thermowatch Ai project card | — | 58 |
| `assets/static/projects/wafer-gpt.svg` | Static counterpart: Wafer Gpt project card | — | 34 |
| `assets/static/ui/boot.png` | Static counterpart: Profile boot animation | — | 13 |
| `assets/static/ui/current-focus.svg` | Static counterpart: Current focus modules | — | 25 |
| `assets/static/ui/deep-scan.png` | Static counterpart: Typing profile diagnostics | — | 195 |
| `assets/static/ui/demo.svg` | Static counterpart: App button | — | 68 |
| `assets/static/ui/engineering-pipeline.svg` | Static counterpart: Six-stage engineering workflow | — | 127 |
| `assets/static/ui/github.svg` | Static counterpart: GitHub contact button | — | 187 |
| `assets/static/ui/interface.svg` | Static counterpart: Published interface button | — | 47, 94 |
| `assets/static/ui/linkedin.svg` | Static counterpart: Exact LinkedIn contact button | — | 9, 186 |
| `assets/static/ui/mail.svg` | Static counterpart: Email contact button | — | 10, 185 |
| `assets/static/ui/resume.svg` | Static counterpart: Resume download button | — | 8, 179 |
| `assets/static/ui/signature.svg` | Static counterpart: Final terminal signature | — | 197 |
| `assets/static/ui/source.svg` | Static counterpart: Reusable source button | — | 46, 67, 80, 93, 107 |
| `assets/ui/boot.gif` | Profile boot animation | 13 | — |
| `assets/ui/current-focus.svg` | Current focus modules | 25 | — |
| `assets/ui/deep-scan.gif` | Typing profile diagnostics | 195 | — |
| `assets/ui/demo.svg` | App button | 68 | — |
| `assets/ui/engineering-pipeline.svg` | Six-stage engineering workflow | 127 | — |
| `assets/ui/github.svg` | GitHub contact button | 187 | — |
| `assets/ui/interface.svg` | Published interface button | 47, 94 | — |
| `assets/ui/linkedin.svg` | Exact LinkedIn contact button | 9, 186 | — |
| `assets/ui/mail.svg` | Email contact button | 10, 185 | — |
| `assets/ui/resume.svg` | Resume download button | 8, 179 | — |
| `assets/ui/signature.svg` | Final terminal signature | 197 | — |
| `assets/ui/source.svg` | Reusable source button | 46, 67, 80, 93, 107 | — |

## Complete package tree

```text
Harshitcodes154/
├── .github/
│   └── workflows/
│       └── update-activity.yml
├── assets/
│   ├── achievements/
│   │   └── ctf.svg
│   ├── contribution/
│   │   ├── activity-source.json
│   │   ├── calendar.svg
│   │   └── stats.svg
│   ├── profile/
│   │   ├── cinematic-headshot.png
│   │   └── original-headshot.jpeg
│   ├── projects/
│   │   ├── ashoka-cooling-point.svg
│   │   ├── operation-sindoor.svg
│   │   ├── razorrecover.svg
│   │   ├── thermowatch-ai.svg
│   │   └── wafer-gpt.svg
│   ├── resume/
│   │   └── Harshit-Kumar-Resume.pdf
│   ├── static/
│   │   ├── achievements/
│   │   │   └── ctf.svg
│   │   ├── projects/
│   │   │   ├── ashoka-cooling-point.svg
│   │   │   ├── operation-sindoor.svg
│   │   │   ├── razorrecover.svg
│   │   │   ├── thermowatch-ai.svg
│   │   │   └── wafer-gpt.svg
│   │   └── ui/
│   │       ├── boot.png
│   │       ├── current-focus.svg
│   │       ├── deep-scan.png
│   │       ├── demo.svg
│   │       ├── engineering-pipeline.svg
│   │       ├── github.svg
│   │       ├── interface.svg
│   │       ├── linkedin.svg
│   │       ├── mail.svg
│   │       ├── resume.svg
│   │       ├── signature.svg
│   │       └── source.svg
│   ├── ui/
│   │   ├── boot.gif
│   │   ├── current-focus.svg
│   │   ├── deep-scan.gif
│   │   ├── demo.svg
│   │   ├── engineering-pipeline.svg
│   │   ├── github.svg
│   │   ├── interface.svg
│   │   ├── linkedin.svg
│   │   ├── mail.svg
│   │   ├── resume.svg
│   │   ├── signature.svg
│   │   └── source.svg
│   ├── hero-mobile.png
│   └── hero.png
├── docs/
│   ├── ASSET-MAP.md
│   ├── EVIDENCE.md
│   ├── INSTALL.md
│   ├── PORTRAIT.md
│   ├── STATIC-PROFILE.md
│   └── VERIFICATION.md
├── scripts/
│   ├── build_assets.cjs
│   ├── build_motion.py
│   ├── build_package.py
│   ├── update_activity.py
│   └── verify_package.py
├── PREVIEW.html
└── README.md
```

## References beyond images

- `.github/workflows/update-activity.yml` runs `scripts/update_activity.py` and refreshes the three contribution files only.
- `scripts/build_assets.cjs` creates the hero PNGs and primary SVG UI. The supplied PNGs need no runtime generator.
- `scripts/build_motion.py` creates the two GIFs and their static PNG counterparts.
- The two secondary project cards are editable SVG source files.
- `docs/EVIDENCE.md` records implementation sources, owner attestations, limits and resume integrity.
- `docs/INSTALL.md`, `docs/PORTRAIT.md` and `docs/VERIFICATION.md` cover setup, maintenance and checks.
- `PREVIEW.html` is a static local review copy; README.md remains the GitHub deliverable.
