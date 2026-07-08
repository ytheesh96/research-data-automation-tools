#!/usr/bin/env python3
"""Validate the public-ready umbrella package without publishing anything."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md",
    "docs/index.md",
    "PUBLIC_SAFETY_NOTES.md",
    "PUBLISH_CHECKLIST.md",
    "RESUME_LINK_HANDOFF.md",
    "COMPONENT_METADATA.json",
]
FORBIDDEN_PATTERNS = {
    "mac_user_path": re.compile("/" + r"Users/[^\\s)`]+"),
    "home_path": re.compile("~" + r"/(?!$)"),
    "likely_credential_assignment": re.compile(r"(?i)(api[_-]?key|secret|to" + r"ken|password)\\s*[:=]"),
    "internal_marker": re.compile(r"(?i)(PRIVATE_" + r"NOTE|CONF" + r"IDENTIAL|DO_NOT_" + r"SHARE)"),
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing:
        fail(f"missing required files: {missing}")

    metadata = json.loads((ROOT / "COMPONENT_METADATA.json").read_text())
    if metadata["future_hub_url"] != "https://github.com/ytheesh96/research-data-automation-tools":
        fail("future hub URL mismatch")

    for component in metadata["components"]:
        url = component["url"]
        req = Request(url, headers={"User-Agent": "Hermes-public-target-validator"})
        with urlopen(req, timeout=20) as response:
            if response.status != 200:
                fail(f"{url} returned HTTP {response.status}")
        print(f"URL OK: {url}")

    scanned = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".py"}:
            text = path.read_text(errors="replace")
            rel = path.relative_to(ROOT)
            scanned.append(str(rel))
            for label, pattern in FORBIDDEN_PATTERNS.items():
                match = pattern.search(text)
                if match:
                    fail(f"forbidden pattern {label} in {rel}: {match.group(0)!r}")

    print(json.dumps({"status": "ok", "files_scanned": scanned}, indent=2))


if __name__ == "__main__":
    main()
