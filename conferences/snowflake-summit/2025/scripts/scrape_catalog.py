#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
from pathlib import Path
from statistics import mean

CATALOG_URL = "https://reg.snowflake.com/flow/snowflake/summit25/sessions/page/catalog"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "normalized" / "sessions.json"
DEFAULT_SUMMARY = ROOT / "analysis" / "summary.md"


def fetch_rendered_dom(url: str) -> str:
    cmd = [
        "chromium",
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        "--virtual-time-budget=20000",
        "--dump-dom",
        url,
    ]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout


def clean_text(value: str | None) -> str | None:
    if value is None:
        return None
    value = html.unescape(re.sub(r"<[^>]+>", "", value))
    value = re.sub(r"\s+", " ", value).strip()
    return value or None


def infer_code(title: str | None) -> str | None:
    if not title:
        return None
    if "," in title:
        tail = title.rsplit(",", 1)[-1].strip()
        if re.fullmatch(r"[A-Z]{1,}[0-9]{2,}[A-Z0-9-]*", tail):
            return tail
    match = re.search(r"\b([A-Z]{1,}[0-9]{2,}[A-Z0-9-]*)\b$", title)
    return match.group(1) if match else None


def extract_sessions(dom: str) -> list[dict]:
    starts = list(re.finditer(r'<div id="(session-[^"]+)" class="rf-tile-wrapper"', dom))
    sessions = []
    for i, match in enumerate(starts):
        chunk = dom[match.start() : starts[i + 1].start() if i + 1 < len(starts) else len(dom)]
        session_tile_id = match.group(1)
        banner = re.search(r'<div class="rf-tile-banner"><img src="([^"]+)" alt="([^"]*)">', chunk)
        title = clean_text(re.search(r'<h4 class="rf-tile-title"><a[^>]*>(.*?)</a></h4>', chunk, re.S).group(1) if re.search(r'<h4 class="rf-tile-title"><a[^>]*>(.*?)</a></h4>', chunk, re.S) else None)
        abstract_match = re.search(r'<p class="rf-tile-info rf-tile-line-two"><p>(.*?)</p>', chunk, re.S)
        abstract = clean_text(abstract_match.group(1) if abstract_match else None)
        speakers = [html.unescape(name) for name in re.findall(r'aria-label="([^"]+?) speaker for the', chunk)]
        sessions.append(
            {
                "session_tile_id": session_tile_id,
                "session_id": session_tile_id.removeprefix("session-").split("-", 1)[0],
                "title": title,
                "session_code": infer_code(title),
                "abstract": abstract,
                "speakers": speakers,
                "speaker_count": len(speakers),
                "banner_image_url": banner.group(1) if banner else None,
                "banner_alt": html.unescape(banner.group(2)) if banner else None,
                "source_catalog_url": CATALOG_URL,
            }
        )
    return sessions


def write_summary(sessions: list[dict], path: Path) -> None:
    codes = sum(1 for s in sessions if s["session_code"])
    speaker_counts = [s["speaker_count"] for s in sessions]
    lines = [
        "# Snowflake Summit 2025 visible-catalog summary",
        "",
        f"- source: {CATALOG_URL}",
        f"- captured visible session cards: {len(sessions)}",
        f"- sessions with parsed session code: {codes}",
        f"- sessions with at least one speaker: {sum(1 for s in sessions if s['speaker_count'] > 0)}",
        f"- average speakers per captured card: {mean(speaker_counts):.2f}" if speaker_counts else "- average speakers per captured card: n/a",
        "",
        "## Important limitation",
        "",
        "This is a practical public capture of the rendered visible catalog cards from the live page state. It is not presented as a complete internal export of all Summit 2025 sessions or metadata.",
        "",
        "## First five titles",
        "",
    ]
    for session in sessions[:5]:
        lines.append(f"- {session['title']}")
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    args = parser.parse_args()

    dom = fetch_rendered_dom(CATALOG_URL)
    sessions = extract_sessions(dom)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(sessions, indent=2, ensure_ascii=False) + "\n")

    args.summary.parent.mkdir(parents=True, exist_ok=True)
    write_summary(sessions, args.summary)

    print(json.dumps({"captured_sessions": len(sessions), "output": str(args.output), "summary": str(args.summary)}, indent=2))


if __name__ == "__main__":
    main()
