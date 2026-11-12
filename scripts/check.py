#!/usr/bin/env python3
"""Checks the repository's prompt files.

- every .json file parses
- the SillyTavern preset's Main Prompt is exactly system_prompt.txt
- text files are UTF-8 without a byte-order mark and use LF line endings

Run from anywhere: python3 scripts/check.py
After editing system_prompt.txt, run python3 scripts/check.py --fix to copy it into the preset.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "system_prompt.txt"
PRESET = ROOT / "a_little_more_human.json"
MAIN_ID = "main"


def main_prompt(preset: dict) -> dict:
    for prompt in preset.get("prompts", []):
        if prompt.get("identifier") == MAIN_ID:
            return prompt
    raise KeyError(f"{PRESET.name} has no prompt with identifier '{MAIN_ID}'")


def main() -> int:
    fix = "--fix" in sys.argv[1:]
    errors: list[str] = []

    for path in sorted(ROOT.glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except ValueError as error:
            errors.append(f"{path.name}: invalid JSON ({error})")

    for path in sorted([*ROOT.glob("*.txt"), *ROOT.glob("*.json"), *ROOT.glob("*.md")]):
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"{path.name}: starts with a UTF-8 byte-order mark")
        if b"\r" in raw:
            errors.append(f"{path.name}: has CRLF line endings")
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError as error:
            errors.append(f"{path.name}: not UTF-8 ({error})")

    if not any(e.startswith(PRESET.name) for e in errors):
        text = PRESET.read_text(encoding="utf-8")
        preset = json.loads(text)
        prompt = main_prompt(preset)
        wanted = PROMPT.read_text(encoding="utf-8")
        if prompt.get("content") != wanted:
            if fix:
                prompt["content"] = wanted
                # Keep the file's existing formatting: 4-space indent, raw UTF-8, no final newline.
                PRESET.write_text(json.dumps(preset, indent=4, ensure_ascii=False), encoding="utf-8", newline="\n")
                print(f"Updated {PRESET.name} from {PROMPT.name}.")
            else:
                errors.append(
                    f"{PRESET.name}: Main Prompt differs from {PROMPT.name}; run python3 scripts/check.py --fix"
                )

    for error in errors:
        print(f"::error::{error}" if "GITHUB_ACTIONS" in os.environ else error)
    print(f"{'FAIL' if errors else 'PASS'}: {len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
