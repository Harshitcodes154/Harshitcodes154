"""Check portable references, SVG safety, resume integrity and real activity totals."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
links = 0
for md in [ROOT/'README.md', *sorted((ROOT/'docs').glob('*.md'))]:
    content = md.read_text(encoding='utf-8')
    targets = re.findall(r'\]\(([^)]+)\)', content) + re.findall(r'(?:src|srcset|href)="([^"]+)"', content)
    for target in targets:
        if urlsplit(target).scheme or target.startswith('#'):
            continue
        dest = (md.parent / unquote(target.split('#')[0])).resolve()
        if not dest.is_relative_to(ROOT): errors.append(f'Outside-package reference: {md.name}: {target}')
        elif not dest.exists(): errors.append(f'Missing reference: {md.name}: {target}')
        links += 1

svgs = list((ROOT/'assets').rglob('*.svg'))
for path in svgs:
    src = path.read_text(encoding='utf-8')
    try: doc = ET.fromstring(src)
    except ET.ParseError as exc:
        errors.append(f'{path.name}: {exc}')
        continue
    if not doc.get('viewBox'): errors.append(f'{path.name}: missing viewBox')
    if re.search(r'<(?:script|foreignObject)\b|(?:href|src)="https?://|\son\w+=', src, re.I):
        errors.append(f'{path.name}: active/external dependency in SVG')
    if '/static/' in path.as_posix() and re.search(r'@keyframes|<animate\b', src):
        errors.append(f'{path.name}: animation in static asset')

resume = ROOT/'assets/resume/Harshit-Kumar-Resume.pdf'
resume_hash = hashlib.sha256(resume.read_bytes()).hexdigest().upper()
expected_resume_hash = '1D24B96FD7042BD8B658B4D77C8832B35DE29AE5F3571B09219FEEE9B5F5C314'
if resume_hash != expected_resume_hash:
    errors.append('Resume changed; verify the replacement and update its documented checksum.')

data = json.loads((ROOT/'assets/contribution/activity-source.json').read_text())
days = data['calendar']['days']
if sum(d['count'] for d in days) != data['calendar']['total']:
    errors.append('Contribution sum mismatch')
if len(set(d['date'] for d in days)) != len(days): errors.append('Duplicate calendar dates')
readme = (ROOT/'README.md').read_text(encoding='utf-8')
if 'AXH AI' in readme: errors.append('AXH included despite user omission request')
if 'Null Matrix' in readme: errors.append('Old CTF name in README')
if 'AI-Wafer-Defect-Detection' in readme: errors.append('Duplicate wafer project link')
linkedins = set(re.findall(r'https://www\.linkedin\.com/[^"\s)]+',readme))
if linkedins != {'https://www.linkedin.com/in/harshit-kumar-59783b311/'}:
    errors.append('LinkedIn URL mismatch')
if '<script' in readme.lower(): errors.append('Runtime JavaScript in README')

for e in errors: print('FAIL:',e)
if errors: raise SystemExit(1)
print(f'PASS: {links} local references; {len(svgs)} SVGs; exact resume checksum; {len(days)} real contribution dates; {data["calendar"]["total"]} contributions.')
print('PASS: exact LinkedIn; canonical CTF name; AXH omitted; no duplicate wafer entry; no active SVG or README scripts.')
