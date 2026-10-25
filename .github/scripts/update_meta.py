#!/usr/bin/env python3
"""Append ⭐ stars / 🗓 last-push metadata to GitHub repo entries in the README.

Run from the repo root. Uses GITHUB_TOKEN if set (GitHub Actions provides one);
otherwise falls back to anonymous API access (rate limit 60 req/h).

- Every list entry linking to a GitHub repo root gets:  `⭐ N · 🗓 YYYY-MM`
- Repos with no push in the last year additionally get 💤
- Archived repos get 🗄 instead
- Existing suffixes are stripped first, so the script is idempotent.
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

FILES = ["README.md"]
STALE_DAYS = 365

# - [text](https://github.com/owner/repo) — description ...
ENTRY_RE = re.compile(
    r"^(?P<prefix>- \[[^\]]+\]\(https://github\.com/(?P<owner>[A-Za-z0-9_.-]+)/(?P<repo>[A-Za-z0-9_.-]+)\)\s*—.*)$"
)
# trailing generated suffix: `⭐ N · 🗓 YYYY-MM` (+ optional 💤/🗄), possibly repeated
META_RE = re.compile(r"(?:\s*`⭐ \d+ · 🗓 \d{4}-\d{2}`[\s💤🗄]*)+\s*$")

cache: dict[str, dict | None] = {}


def gh_api(owner: str, repo: str) -> dict | None:
    key = f"{owner}/{repo}".lower()
    if key in cache:
        return cache[key]
    req = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-root-cern-meta-updater",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            cache[key] = json.load(r)
    except Exception as e:  # 404, rate limit, network — leave line untouched
        print(f"  ! {owner}/{repo}: {e}", file=sys.stderr)
        cache[key] = None
    return cache[key]


def annotate(line: str, today: datetime) -> str | None:
    m = ENTRY_RE.match(line)
    if not m:
        return None
    data = gh_api(m["owner"], m["repo"])
    if data is None:
        # keep the entry, just drop any stale suffix we can't refresh
        return META_RE.sub("", m["prefix"]).rstrip() if META_RE.search(line) else None

    stars = data.get("stargazers_count", 0)
    pushed = data.get("pushed_at") or data.get("updated_at") or ""
    ym = pushed[:7] if len(pushed) >= 7 else "????-??"
    age_days = (
        (today - datetime.fromisoformat(pushed.replace("Z", "+00:00"))).days
        if pushed
        else STALE_DAYS + 1
    )

    suffix = f" `⭐ {stars} · 🗓 {ym}`"
    if data.get("archived"):
        suffix += " 🗄"  # no U+FE0F: keep the strip regex simple
    elif age_days > STALE_DAYS:
        suffix += " 💤"

    base = META_RE.sub("", m["prefix"]).rstrip()
    new = base + suffix
    return new if new != line.rstrip("\n") else None


def main() -> None:
    today = datetime.now(timezone.utc)
    changed_total = 0
    for path in FILES:
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        changed = 0
        for i, line in enumerate(lines):
            if not line.startswith("- ["):
                continue
            new = annotate(line.rstrip("\n"), today)
            if new is not None:
                lines[i] = new + "\n"
                changed += 1
        if changed:
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lines)
        print(f"{path}: {changed} line(s) updated")
        changed_total += changed
    print(f"total: {changed_total} line(s) updated")


if __name__ == "__main__":
    main()
