#!/usr/bin/env python3
"""Fetch real GitHub activity and render dependency-free, self-hosted SVGs.

Usage: python scripts/update_activity.py [--username Harshitcodes154]
GITHUB_TOKEN or GH_TOKEN is optional. It is sent only to api.github.com.
No external image renderer, JavaScript, or third-party stats service is used.
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "contribution"
COLORS = ["#172735", "#155a55", "#219c78", "#3ad899", "#6cf5b0"]
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")


def fetch(url: str, *, api: bool = False):
    headers = {"User-Agent": "Harshitcodes154-profile-activity", "Accept": "application/vnd.github+json" if api else "text/html"}
    if api:
        headers["X-GitHub-Api-Version"] = "2022-11-28"
        if TOKEN:
            headers["Authorization"] = "Bearer " + TOKEN
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=45) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if api else raw
        except urllib.error.HTTPError as exc:
            # Public data remains accessible when a locally supplied token is invalid.
            if exc.code == 401 and "Authorization" in headers:
                headers.pop("Authorization")
                continue
            if exc.code in (429, 500, 502, 503, 504) and attempt < 2:
                time.sleep(2 ** attempt)
                continue
            raise


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cells = {}
        self.tooltips = {}
        self.tooltip_id = None
        self.in_summary = False
        self.summary = ""

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "td" and attrs.get("data-date") and "ContributionCalendar-day" in attrs.get("class", ""):
            self.cells[attrs["id"]] = {"date": attrs["data-date"], "level": int(attrs["data-level"])}
        if tag == "tool-tip" and attrs.get("for"):
            self.tooltip_id = attrs["for"]
            self.tooltips[self.tooltip_id] = ""
        if tag == "h2" and attrs.get("id") == "js-contribution-activity-description":
            self.in_summary = True

    def handle_data(self, data):
        if self.tooltip_id:
            self.tooltips[self.tooltip_id] += data
        if self.in_summary:
            self.summary += data

    def handle_endtag(self, tag):
        if tag == "tool-tip":
            self.tooltip_id = None
        if tag == "h2":
            self.in_summary = False

    def result(self):
        days = []
        for identifier, cell in self.cells.items():
            label = " ".join(self.tooltips.get(identifier, "").split())
            match = re.match(r"(No|[\d,]+) contributions? on ", label)
            if not match:
                raise ValueError(f"Cannot establish exact count for {cell['date']}; GitHub markup may have changed")
            count = 0 if match[1] == "No" else int(match[1].replace(",", ""))
            if not 0 <= cell["level"] <= 4:
                raise ValueError("Unexpected GitHub intensity level")
            if (count == 0) != (cell["level"] == 0):
                raise ValueError("GitHub contribution intensity and exact count disagree")
            days.append({**cell, "count": count})
        days.sort(key=lambda day: day["date"])
        if len(days) < 350 or len({day["date"] for day in days}) != len(days):
            raise ValueError("Incomplete or duplicated contribution calendar")
        for left, right in zip(days, days[1:]):
            if dt.date.fromisoformat(right["date"]) - dt.date.fromisoformat(left["date"]) != dt.timedelta(days=1):
                raise ValueError("Contribution calendar has missing dates")
        summary = " ".join(self.summary.split())
        match = re.search(r"([\d,]+) contributions?", summary)
        if not match:
            raise ValueError("Cannot find GitHub's total contribution count")
        total = int(match[1].replace(",", ""))
        if sum(day["count"] for day in days) != total:
            raise ValueError("Exact daily counts do not match GitHub's displayed total; keeping previous assets")
        return days, total, summary


def svg_start(height, title, description):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{height}" viewBox="0 0 900 {height}" role="img" aria-labelledby="title description">',
            f'<title id="title">{html.escape(title)}</title><desc id="description">{html.escape(description)}</desc>',
            '<style>text{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;fill:#eaf5ff}.muted{fill:#91a7b9}.cyan{fill:#48dcff}.green{fill:#6cf5b0}</style>',
            f'<rect x="1" y="1" width="898" height="{height-2}" rx="16" fill="#080d14" stroke="#24384b"/>',
            '<path d="M28 1H162" stroke="#48dcff" stroke-width="2"/>']


def text(x, y, value, size=18, css="", **attributes):
    extra = " ".join(f'{k.replace("_", "-")}="{html.escape(str(v), quote=True)}"' for k, v in attributes.items())
    return f'<text x="{x}" y="{y}" font-size="{size}" class="{css}" {extra}>{html.escape(str(value))}</text>'


def render_calendar(data):
    days = data["calendar"]["days"]
    first = dt.date.fromisoformat(days[0]["date"])
    sunday = first - dt.timedelta(days=(first.weekday() + 1) % 7)
    last = dt.date.fromisoformat(days[-1]["date"])
    weeks = ((last - sunday).days // 7) + 1
    step = min(14.4, 772 / weeks)
    cell_size = step - 3.2
    x0, y0 = 90, 129
    total = data["calendar"]["total"]
    out = svg_start(316, "Git activity / contribution matrix", f"{total} actual GitHub-visible contributions, {days[0]['date']} through {days[-1]['date']}. Exact daily counts are embedded as cell titles.")
    out += [text(28, 38, "GIT ACTIVITY / CONTRIBUTION MATRIX", 23, "cyan"), text(28, 70, f"{total:,} contributions", 21), text(872, 69, "SOURCE: GITHUB", 14, "muted", text_anchor="end")]
    month_seen = set()
    for day in days:
        date = dt.date.fromisoformat(day["date"])
        week = (date - sunday).days // 7
        weekday = (date.weekday() + 1) % 7
        key = (date.year, date.month)
        # Month labels align to the first Sunday of that month.
        if weekday == 0 and key not in month_seen:
            out.append(text(round(x0 + week * step, 2), 111, date.strftime("%b"), 13, "muted"))
            month_seen.add(key)
        x, y = round(x0 + week * step, 2), round(y0 + weekday * step, 2)
        label = f"{day['date']}: {day['count']} contribution{'s' if day['count'] != 1 else ''}"
        out.append(f'<rect x="{x}" y="{y}" width="{cell_size:.2f}" height="{cell_size:.2f}" rx="2" fill="{COLORS[day["level"]]}"><title>{label}</title></rect>')
    for row, label in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
        out.append(text(35, round(y0 + row * step + cell_size, 2), label, 13, "muted"))
    out += [text(28, 256, f"{days[0]['date']}  —  {days[-1]['date']}", 16, "muted"), text(695, 256, "Less", 12, "muted")]
    for level, fill in enumerate(COLORS):
        out.append(f'<rect x="{731 + level*17}" y="246" width="12" height="12" rx="2" fill="{fill}"/>')
    out += [text(822, 256, "More", 12, "muted"), text(28, 288, f"{weeks}-WEEK SNAPSHOT  /  Updated {data['fetched_at'][:10]} UTC", 14, "muted"), "</svg>"]
    return "\n".join(out)


def streaks(days):
    best = running = 0
    for day in days:
        running = running + 1 if day["count"] > 0 else 0
        best = max(best, running)
    index = len(days) - 1
    # A not-yet-active final day does not break yesterday's streak.
    if days[index]["count"] == 0:
        index -= 1
    current = 0
    while index >= 0 and days[index]["count"] > 0:
        current += 1
        index -= 1
    return current, best


def render_stats(data):
    days = data["calendar"]["days"]
    current, longest = streaks(days)
    repos = data["repositories"]
    stars = sum(repo["stargazers_count"] for repo in repos)
    active = sum(day["count"] > 0 for day in days)
    total_bytes = sum(data["language_bytes"].values())
    ranked = sorted(data["language_bytes"].items(), key=lambda item: (-item[1], item[0]))
    top = ranked[:5]
    remainder = sum(count for _, count in ranked[5:])
    if remainder:
        top.append(("Other", remainder))
    out = svg_start(563, "GitHub telemetry / public repository statistics", "Statistics derived from GitHub REST metadata and the exact contribution calendar. Languages measure GitHub Linguist bytes across public non-fork repositories, not proficiency. Streaks measure consecutive days with any contribution within the displayed window.")
    out += [text(28, 38, "REPOSITORY TELEMETRY", 23, "cyan"), text(872, 38, data["fetched_at"][:10] + " UTC", 14, "muted", text_anchor="end")]
    metrics = [(28, len(repos), "PUBLIC REPOS"), (250, stars, "REPO STARS"), (468, active, "ACTIVE DAYS"), (690, data["calendar"]["total"], "CONTRIBUTIONS")]
    for x, value, label in metrics:
        out += [text(x, 104, f"{value:,}", 39), text(x, 135, label, 15, "muted")]
    out.append('<path d="M28 161H872" stroke="#24384b"/>')
    out += [text(28, 199, "CONTRIBUTION STREAK", 18, "green"), text(28, 249, current, 34), text(100, 247, "current / days", 16, "muted"), text(28, 299, longest, 34), text(100, 297, "longest in window", 16, "muted"), text(28, 335, "Any contribution counts.", 14, "muted"), text(28, 358, "Current allows an unfinished", 13, "muted"), text(28, 379, "final day with no contribution.", 13, "muted")]
    out += [text(460, 199, "TOP LANGUAGES / CODE BYTES", 18, "green")]
    language_colors = ["#48dcff", "#6cf5b0", "#568cff", "#b28cff", "#91a7b9", "#416078"]
    for index, (name, count) in enumerate(top):
        y = 229 + index * 27
        percentage = count / total_bytes * 100 if total_bytes else 0
        out += [text(460, y, name, 15), text(865, y, f"{percentage:.1f}%", 15, "muted", text_anchor="end"), f'<rect x="625" y="{y-10}" width="165" height="7" rx="3" fill="#172735"/>', f'<rect x="625" y="{y-10}" width="{165*percentage/100:.2f}" height="7" rx="3" fill="{language_colors[index]}"/>']
    out += [text(460, 409, "Public non-fork repositories only.", 13, "muted"), text(460, 430, "Language share is not a skill rating.", 13, "muted"), '<path d="M28 453H872" stroke="#24384b"/>']
    pushed = sorted((repo for repo in repos if repo.get("pushed_at")), key=lambda repo: repo["pushed_at"], reverse=True)
    if pushed:
        latest = pushed[0]
        out += [text(28, 486, "LATEST PUBLIC REPOSITORY PUSH", 14, "cyan"), text(28, 516, latest["name"][:53], 18), text(872, 516, latest["pushed_at"][:10] + " UTC", 15, "muted", text_anchor="end")]
    out += [text(28, 545, f"Streak + contribution window: {days[0]['date']} through {days[-1]['date']}.", 12, "muted"), "</svg>"]
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default="Harshitcodes154")
    args = parser.parse_args()
    if not re.fullmatch(r"[A-Za-z0-9-]+", args.username):
        raise ValueError("Invalid GitHub username")
    username = args.username
    api_url = f"https://api.github.com/users/{username}"
    calendar_url = f"https://github.com/users/{username}/contributions"
    profile = fetch(api_url, api=True)
    repositories = []
    page = 1
    while True:
        batch = fetch(api_url + f"/repos?type=owner&sort=full_name&per_page=100&page={page}", api=True)
        if not isinstance(batch, list):
            raise ValueError("Unexpected repository response")
        repositories.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    repositories = [repo for repo in repositories if not repo.get("private")]
    if len(repositories) != profile["public_repos"]:
        raise ValueError("Public repository list does not match profile count; retry later")
    languages = collections.Counter()
    normalized_repos = []
    for repo in repositories:
        # Linguist API returns byte counts only; no repository source is fetched.
        repo_languages = fetch(repo["languages_url"], api=True) if not repo["fork"] else {}
        if any(not isinstance(value, int) or value < 0 for value in repo_languages.values()):
            raise ValueError("Invalid language byte count")
        languages.update(repo_languages)
        normalized_repos.append({key: repo[key] for key in ["name", "html_url", "fork", "archived", "stargazers_count", "pushed_at", "updated_at", "language"]} | {"language_bytes": repo_languages})
    calendar = CalendarParser()
    calendar.feed(fetch(calendar_url))
    days, total, summary = calendar.result()
    if dt.date.fromisoformat(days[-1]["date"]) > dt.datetime.now(dt.timezone.utc).date():
        raise ValueError("Calendar contains a future UTC date; keeping the previous verified snapshot")
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    data = {
        "schema_version": 1,
        "username": username,
        "fetched_at": now,
        "sources": {"profile": api_url, "repositories": api_url + "/repos?type=owner&per_page=100", "languages": "Each public non-fork repository's GitHub REST /languages endpoint", "contributions": calendar_url},
        "definitions": {"contributions": "Exact daily counts and intensity levels from GitHub's public contribution calendar. This includes the contribution types and visibility settings that GitHub exposes, not just commits.", "current_streak": "Consecutive days with count > 0 ending on the final calendar day, or its preceding day when the final day has zero. Measured only within this snapshot window.", "longest_streak": "Longest consecutive run of dates with count > 0 within this snapshot window, not a lifetime streak.", "language_share": "GitHub Linguist byte totals across all public non-fork repositories. Not a proficiency score. Fork language bytes are excluded.", "repository_stars": "Sum of stargazers_count across all owned public repositories, including forks.", "latest_push": "Maximum pushed_at from owned public repository metadata; not a deployment/build result."},
        "profile": {key: profile[key] for key in ["login", "html_url", "public_repos", "followers", "created_at"]},
        "calendar": {"from": days[0]["date"], "to": days[-1]["date"], "total": total, "github_summary": summary, "days": days},
        "repositories": normalized_repos,
        "language_bytes": dict(sorted(languages.items())),
    }
    rendered = {"calendar.svg": render_calendar(data), "stats.svg": render_stats(data)}
    # Fully validate before replacing any working snapshot.
    for name, svg in rendered.items():
        ET.fromstring(svg)
        if "<script" in svg or "foreignObject" in svg or "http://" in svg.replace("http://www.w3.org/2000/svg", ""):
            raise ValueError(f"Unexpected active/external content in {name}")
    OUT.mkdir(parents=True, exist_ok=True)
    rendered["activity-source.json"] = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    for name, contents in rendered.items():
        destination = OUT / name
        temp = destination.with_suffix(destination.suffix + ".tmp")
        temp.write_text(contents, encoding="utf-8")
        temp.replace(destination)
    current, longest = streaks(days)
    print(f"Updated {username}: {len(repositories)} public repos; {total} exact contributions; current streak {current}; longest in window {longest}.")
    for name in rendered:
        print(f"{(OUT / name).relative_to(ROOT)}: {(OUT / name).stat().st_size:,} bytes")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        # Do not print request headers or secrets. Failing preserves previous snapshots.
        print(f"Activity refresh failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)
