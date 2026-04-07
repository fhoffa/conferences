#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
from collections import Counter
from pathlib import Path
from statistics import mean
from typing import Any

import requests

CATALOG_URL = "https://reg.snowflake.com/flow/snowflake/summit25/sessions/page/catalog"
SESSIONS_API_URL = "https://events.summit.snowflake.com/api/sessions"
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "normalized" / "sessions.json"
DEFAULT_SAMPLE = ROOT / "normalized" / "sample_sessions.json"
DEFAULT_SUMMARY = ROOT / "analysis" / "summary.md"

# Observed from the public catalog XHRs on 2026-04-07.
API_HEADERS = {
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "referer": "https://reg.snowflake.com/",
    "rfApiProfileId": "oUZpqNJnpIbJ1tHgCIrfU8ykJpOzqzrG",
    "rfWidgetId": "DNtdzD64fWl9n73VY75eCEd2ZbDLZ0it",
    "user-agent": "Mozilla/5.0",
}
BASE_FORM = {
    "tab.sessioncatalogtab": "1714168666431001NNiH",
    "type": "session",
    "browserTimezone": "Africa/Abidjan",
    "catalogDisplay": "grid",
}
PAGE_SIZE = 50


def clean_text(value: str | None) -> str | None:
    if value is None:
        return None
    value = html.unescape(re.sub(r"<[^>]+>", "", value))
    value = re.sub(r"\s+", " ", value).strip()
    return value or None


def post_sessions_page(offset: int) -> dict[str, Any]:
    form = dict(BASE_FORM)
    if offset:
        form["from"] = str(offset)
    response = requests.post(SESSIONS_API_URL, headers=API_HEADERS, data=form, timeout=60)
    response.raise_for_status()
    payload = response.json()
    if payload.get("responseCode") != "0":
        raise RuntimeError(f"sessions API error at offset {offset}: {payload}")
    return payload


def extract_page_items(payload: dict[str, Any]) -> tuple[int, int, int, list[dict[str, Any]]]:
    if "sectionList" in payload:
        section = payload["sectionList"][0]
        return int(section["total"]), int(section["from"]), int(section["size"]), section["items"]
    return int(payload["total"]), int(payload["from"]), int(payload["size"]), payload["items"]


def fetch_all_items() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    items: list[dict[str, Any]] = []
    pages: list[dict[str, Any]] = []
    offset = 0
    total = None
    while True:
        payload = post_sessions_page(offset)
        page_total, page_from, page_size, page_items = extract_page_items(payload)
        pages.append(
            {
                "from": page_from,
                "size": page_size,
                "num_items": len(page_items),
                "total": page_total,
            }
        )
        items.extend(page_items)
        total = page_total
        offset = page_from + len(page_items)
        if offset >= total or not page_items:
            break
    return items, pages


def normalize_attribute_values(values: list[dict[str, Any]]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for value in values or []:
        name = value.get("attribute") or value.get("attribute_id") or "Unknown"
        display_value = value.get("value")
        if not display_value:
            continue
        grouped.setdefault(name, [])
        if display_value not in grouped[name]:
            grouped[name].append(display_value)
    return grouped


def normalize_times(times: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized = []
    for slot in times or []:
        normalized.append(
            {
                "session_time_id": slot.get("sessionTimeID"),
                "date": slot.get("date"),
                "date_formatted": slot.get("dateFormatted"),
                "day_name": slot.get("dayName") or slot.get("dayDisplayName"),
                "start_time": slot.get("startTime"),
                "start_time_formatted": slot.get("startTimeFormatted"),
                "end_time": slot.get("endTime"),
                "end_time_formatted": slot.get("endTimeFormatted"),
                "room": slot.get("room"),
                "room_id": slot.get("roomId"),
                "length_minutes": slot.get("length"),
                "in_person_time": slot.get("inPersonTime"),
                "virtual_time": slot.get("virtualTime"),
                "utc_start_time": slot.get("utcStartTime"),
                "utc_end_time": slot.get("utcEndTime"),
            }
        )
    return normalized


def normalize_participants(participants: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized = []
    for person in participants or []:
        normalized.append(
            {
                "speaker_id": person.get("speakerId"),
                "full_name": person.get("fullName") or person.get("preferredFullName") or person.get("globalFullName"),
                "first_name": person.get("firstName") or person.get("preferredFirstname") or person.get("globalFirstname"),
                "last_name": person.get("lastName") or person.get("globalLastname"),
                "company": person.get("companyName") or person.get("globalCompany"),
                "job_title": person.get("jobTitle") or person.get("globalJobtitle"),
                "roles": person.get("roles"),
                "bio": clean_text(person.get("bio") or person.get("globalBio")),
                "photo_url": person.get("photoURL") or person.get("globalPhotoURL"),
                "linkedin": person.get("linkedIn"),
                "twitter": person.get("twitter"),
                "display_order": person.get("displayorder"),
            }
        )
    return normalized


def normalize_item(item: dict[str, Any]) -> dict[str, Any]:
    speakers = normalize_participants(item.get("participants") or [])
    return {
        "session_time_id": item.get("sessionTimeID"),
        "session_id": item.get("sessionID"),
        "external_id": item.get("externalID"),
        "title": item.get("title"),
        "session_code": item.get("code") or item.get("abbreviation"),
        "session_type": item.get("type"),
        "abstract": clean_text(item.get("abstract")),
        "language": item.get("language"),
        "status": item.get("status"),
        "length_minutes": item.get("length"),
        "event_id": item.get("eventId"),
        "event_code": item.get("eventCode"),
        "event_name": item.get("eventName"),
        "source_catalog_url": CATALOG_URL,
        "source_api_url": SESSIONS_API_URL,
        "times": normalize_times(item.get("times") or []),
        "attributes": normalize_attribute_values(item.get("attributevalues") or []),
        "speakers": speakers,
        "speaker_count": len(speakers),
        "view_access_public": item.get("viewAccessPublic"),
        "has_webinar_profile": item.get("hasWebinarProfile"),
        "has_webinar_chat_profile": item.get("hasWebinarChatProfile"),
        "modified_at": item.get("modified"),
    }


def write_summary(records: list[dict[str, Any]], pages: list[dict[str, Any]], path: Path) -> None:
    unique_sessions = len({record["session_id"] for record in records})
    speaker_counts = [record["speaker_count"] for record in records]
    duplicate_counter = Counter(record["session_id"] for record in records)
    duplicate_session_ids = sum(1 for count in duplicate_counter.values() if count > 1)
    attribute_names = Counter()
    for record in records:
        attribute_names.update(record["attributes"].keys())

    lines = [
        "# Snowflake Summit 2025 catalog API summary",
        "",
        f"- source catalog: {CATALOG_URL}",
        f"- source sessions API: {SESSIONS_API_URL}",
        f"- paginated catalog listings captured: {len(records)}",
        f"- unique session IDs captured: {unique_sessions}",
        f"- duplicate session IDs across multiple catalog listings: {duplicate_session_ids}",
        f"- pages fetched: {len(pages)}",
        f"- API page size observed: {PAGE_SIZE}",
        f"- sessions with at least one speaker: {sum(1 for record in records if record['speaker_count'] > 0)}",
        f"- average speakers per listing: {mean(speaker_counts):.2f}" if speaker_counts else "- average speakers per listing: n/a",
        "",
        "## What this capture is",
        "",
        "This is a deeper public RainFocus API capture of the Snowflake Summit 2025 catalog, using the same unauthenticated session API that the public catalog page calls in the browser. It is materially more complete than a first-page DOM scrape.",
        "",
        "## Remaining limits",
        "",
        "- The public API returns catalog listings, which means a small number of session IDs appear more than once when the catalog lists multiple time slots separately.",
        "- This pass only captures fields present on the public catalog API response. It does not claim access to private attendee-only or admin-only fields.",
        "- The API headers (`rfApiProfileId`, `rfWidgetId`) were observed from public browser traffic and could rotate in the future.",
        "",
        "## Most common attribute groups",
        "",
    ]
    for name, count in attribute_names.most_common(10):
        lines.append(f"- {name}: present on {count} listings")
    lines.extend(["", "## First five titles", ""])
    for record in records[:5]:
        code_suffix = f", {record['session_code']}" if record.get("session_code") else ""
        lines.append(f"- {record['title']}{code_suffix}")
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--sample-output", type=Path, default=DEFAULT_SAMPLE)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    args = parser.parse_args()

    raw_items, pages = fetch_all_items()
    records = [normalize_item(item) for item in raw_items]

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n")

    args.sample_output.parent.mkdir(parents=True, exist_ok=True)
    args.sample_output.write_text(json.dumps(records[:5], indent=2, ensure_ascii=False) + "\n")

    args.summary.parent.mkdir(parents=True, exist_ok=True)
    write_summary(records, pages, args.summary)

    print(
        json.dumps(
            {
                "captured_catalog_listings": len(records),
                "unique_session_ids": len({record['session_id'] for record in records}),
                "pages_fetched": len(pages),
                "output": str(args.output),
                "sample_output": str(args.sample_output),
                "summary": str(args.summary),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
