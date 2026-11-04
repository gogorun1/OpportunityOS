#!/usr/bin/env python3
"""Offline checks for a private Opportunity OS configuration (Python 3.9+)."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def check(root, examples_only=False):
    errors = []

    def load(relative):
        try:
            value = json.loads((root / relative).read_text())
            if not isinstance(value, dict):
                raise ValueError("expected a JSON object")
            return value
        except (OSError, ValueError) as exc:
            errors.append(f"{relative}: {exc}")
            return {}

    profile_path = "config/profile.example.json" if examples_only else "private/profile.json"
    workspace_path = "config/workspace.example.json" if examples_only else "private/workspace.json"
    profile, workspace = load(profile_path), load(workspace_path)
    identity = profile.get("identity", {})
    try:
        ZoneInfo(identity.get("timezone", ""))
    except (ZoneInfoNotFoundError, ValueError, TypeError):
        errors.append("identity.timezone must be a valid IANA timezone")
    lanes = profile.get("lanes", {})
    if not isinstance(lanes, dict) or not any(v is True for v in lanes.values()):
        errors.append("Enable at least one lane")
    if not examples_only:
        for label, value in (("preferred_name", identity.get("preferred_name")),
                             ("goal", profile.get("goals", [{}])[0].get("outcome") if profile.get("goals") else None)):
            if not value or value in ("YOUR_NAME", "REPLACE_WITH_YOUR_GOAL"):
                errors.append(f"Complete {label} during onboarding")
    if profile.get("permissions", {}).get("external_actions_require_final_approval") is not True:
        errors.append("The template requires final-version approval for external actions")
    if profile.get("investment", {}).get("trade_execution_allowed") is not False:
        errors.append("Trade execution must remain disabled in this research template")
    if profile.get("notifications", {}).get("max_daily_digests") != 1:
        errors.append("max_daily_digests must be 1")

    notion = workspace.get("notion", {})
    if notion.get("enabled"):
        for name in ("research_briefs", "opportunity_signals", "daily_reports"):
            if not notion.get("data_sources", {}).get(name):
                errors.append(f"Missing Notion destination: {name}")
        if profile.get("permissions", {}).get("internal_notion_archival") is not True:
            errors.append("Notion enabled without internal archival authorization")

    manifest_path = workspace.get("automation_manifest", "private/automation-manifest.json")
    if not examples_only:
        manifest = load(manifest_path)
        tasks = manifest.get("tasks")
        if not isinstance(tasks, list):
            errors.append("Manifest must contain a tasks array (empty is allowed)")
            tasks = []
        known_workflows = {"daily-radar", "research-executor", "career-preparation", "weekly-review"}
        names = set()
        for task in tasks:
            if not isinstance(task, dict):
                errors.append("Every manifest task must be an object")
                continue
            name = task.get("name", "unnamed")
            if name in names:
                errors.append(f"Duplicate task name: {name}")
            names.add(name)
            for field in ("name", "workflow", "prompt_path", "timezone", "cadence", "required_tools", "permission_scope"):
                if not task.get(field):
                    errors.append(f"{name}: missing {field}")
            if task.get("workflow") not in known_workflows:
                errors.append(f"{name}: unknown workflow")
            if not isinstance(task.get("enabled"), bool) or "scheduler_id" not in task:
                errors.append(f"{name}: enabled boolean and scheduler_id are required")
            if task.get("enabled") and not task.get("scheduler_id"):
                errors.append(f"{name}: enabled task needs an actual scheduler ID")
            try:
                ZoneInfo(task.get("timezone", ""))
            except (ZoneInfoNotFoundError, ValueError, TypeError):
                errors.append(f"{name}: invalid timezone")
            prompt = root / task.get("prompt_path", "__missing__")
            if not prompt.is_file():
                errors.append(f"{name}: prompt file missing")
            elif "YOUR_NAME" in prompt.read_text() or "REPLACE_WITH_" in prompt.read_text():
                errors.append(f"{name}: unresolved prompt placeholder")

    tracked = subprocess.run(["git", "ls-files", "--", "private", ".env", ".env.*", "*.pem", "*.key"],
                             cwd=root, capture_output=True, text=True)
    if tracked.returncode:
        errors.append("Cannot check tracked private files; run inside the repository")
    elif tracked.stdout.strip():
        errors.append("Private or credential files are tracked; review git ls-files before pushing")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: offline configuration checks. Tools, sources, account permissions, and scheduled runs still need a manual pilot.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--examples-only", action="store_true", help="Check public JSON examples without a private setup")
    arguments = parser.parse_args()
    sys.exit(check(Path(__file__).resolve().parents[1], arguments.examples_only))
