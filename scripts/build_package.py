"""Refresh the low-motion README and exact asset reference inventory. Stdlib only."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
readme = (ROOT / 'README.md').read_text(encoding='utf-8')
static = readme
static = static.replace('assets/ui/boot.gif', 'assets/static/ui/boot.png')
static = static.replace('assets/ui/deep-scan.gif', 'assets/static/ui/deep-scan.png')
for folder in ('ui', 'projects', 'achievements'):
    static = re.sub(r'assets/' + folder + r'/([\w-]+\.svg)', r'assets/static/' + folder + r'/\1', static)
static = re.sub(r'([("\s])assets/', r'\1../assets/', static)
static = static.replace('](.github/', '](../.github/')
static = static.replace('href="docs/STATIC-PROFILE.md"', 'href="../README.md"')
static = static.replace('Low-motion profile</a>', 'Animated profile</a>')
static = static.replace('href="docs/EVIDENCE.md"', 'href="EVIDENCE.md"')
static = static.replace('![Animated profile diagnostics.', '![Profile diagnostics.')
(ROOT / 'docs/STATIC-PROFILE.md').write_text(static, encoding='utf-8')

def refs(content, target):
    return ', '.join(str(i) for i, line in enumerate(content.splitlines(), 1) if target in line) or '—'

def purpose(rel):
    if rel == 'assets/hero.png': return 'Desktop hero: portrait, identity, terminal and status'
    if rel == 'assets/hero-mobile.png': return 'Mobile portrait/hero composition'
    if '/profile/original' in rel: return 'Unchanged uploaded photo; optional hero rebuild input'
    if '/profile/cinematic' in rel: return 'Cinematic portrait edit; hero rebuild input'
    if '/resume/' in rel: return 'Actual supplied resume PDF; byte-identical copy'
    if rel.endswith('calendar.svg'): return 'Real GitHub contribution calendar snapshot'
    if rel.endswith('stats.svg'): return 'Repository metadata, language bytes and calendar-derived streaks'
    if rel.endswith('activity-source.json'): return 'Exact normalized GitHub data and provenance'
    name = Path(rel).stem
    descriptions = {'boot':'Profile boot animation', 'deep-scan':'Typing profile diagnostics',
        'current-focus':'Current focus modules', 'engineering-pipeline':'Six-stage engineering workflow',
        'signature':'Final terminal signature', 'ctf':'Null Chapter CTF winner module',
        'source':'Reusable source button', 'interface':'Published interface button', 'demo':'App button',
        'resume':'Resume download button', 'linkedin':'Exact LinkedIn contact button',
        'github':'GitHub contact button', 'mail':'Email contact button'}
    desc = descriptions.get(name, name.replace('-', ' ').title() + ' project card')
    return ('Static counterpart: ' if '/static/' in rel else '') + desc

out = ['# Exact folder and asset map', '', 'Generated from the final README. Line numbers are one-based. Run `python scripts/build_package.py` after future edits.', '',
       '| Asset path from repository root | Purpose | README.md lines | docs/STATIC-PROFILE.md lines |',
       '| :--- | :--- | :--- | :--- |']
for p in sorted((ROOT/'assets').rglob('*')):
    if p.is_file():
        rel = p.relative_to(ROOT).as_posix()
        main = refs(readme,rel)
        if '/profile/' in rel: main = 'Indirect: baked into hero at lines ' + refs(readme,'assets/hero')
        out.append(f'| `{rel}` | {purpose(rel)} | {main} | {refs(static,rel)} |')
out += ['', '## Complete package tree', '', '```text', 'Harshitcodes154/']
def walk(directory, prefix=''):
    entries = sorted(directory.iterdir(), key=lambda p:(not p.is_dir(),p.name))
    for i,p in enumerate(entries):
        last=i==len(entries)-1
        out.append(prefix+('└── ' if last else '├── ')+p.name+('/' if p.is_dir() else ''))
        if p.is_dir(): walk(p,prefix+('    ' if last else '│   '))
walk(ROOT)
out += ['```', '', '## References beyond images', '',
        '- `.github/workflows/update-activity.yml` runs `scripts/update_activity.py` and refreshes the three contribution files only.',
        '- `scripts/build_assets.cjs` creates the hero PNGs and primary SVG UI. The supplied PNGs need no runtime generator.',
        '- `scripts/build_motion.py` creates the two GIFs and their static PNG counterparts.',
        '- The two secondary project cards are editable SVG source files.',
        '- `docs/EVIDENCE.md` records implementation sources, owner attestations, limits and resume integrity.',
        '- `docs/INSTALL.md`, `docs/PORTRAIT.md` and `docs/VERIFICATION.md` cover setup, maintenance and checks.',
        '- `PREVIEW.html` is a static local review copy; README.md remains the GitHub deliverable.', '']
(ROOT/'docs/ASSET-MAP.md').write_text('\n'.join(out),encoding='utf-8')
print('Updated low-motion profile and exact asset map.')
