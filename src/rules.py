"""Deterministic validation, priority scoring and fingerprinting; no API calls."""
from __future__ import annotations
import hashlib
import json
from datetime import date


def priority(urgency: int, impact: int) -> str:
    if not all(isinstance(x, int) and not isinstance(x, bool) and 0 <= x <= 3 for x in (urgency, impact)):
        raise ValueError("urgency and impact must each be an integer from 0 to 3")
    score = urgency + impact
    return "Low" if score <= 1 else "Normal" if score <= 3 else "High" if score <= 5 else "Urgent"


def fingerprint(source_type: str, source_id: str, title: str) -> str:
    """Stable, non-secret deduplication key. Check Asana for semantic duplicates too."""
    values = [s.strip().casefold() for s in (source_type, source_id, title)]
    if not all(values):
        raise ValueError("source type, ID and title are required")
    return hashlib.sha256(json.dumps(values, ensure_ascii=False).encode()).hexdigest()


def validate_proposal(proposal: dict) -> None:
    required = ("proposal_id", "title", "description", "source", "priority", "status", "review_required")
    for field in required:
        if field not in proposal:
            raise ValueError(f"Missing required field: {field}")
    if len(proposal["title"].strip()) < 5:
        raise ValueError("Task title too short")
    if proposal["priority"] not in {"Low", "Normal", "High", "Urgent"}:
        raise ValueError("Invalid priority")
    if proposal["status"] != "pending_review" or proposal["review_required"] is not True:
        raise ValueError("New drafts must require review")
    source = proposal["source"]
    if not isinstance(source, dict) or not source.get("id") or source.get("type") not in {"meeting", "email", "calendar", "drive", "manual"}:
        raise ValueError("Invalid source")
    if proposal.get("due_date") is not None:
        date.fromisoformat(proposal["due_date"])
    confidence = proposal.get("confidence")
    if confidence is not None and (not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1):
        raise ValueError("Invalid confidence")


def prepare_draft(task: dict, source: dict) -> dict:
    """Produces an approval-needed task; does NOT write to Asana."""
    data = {
        "proposal_id": task["proposal_id"],
        "title": task["title"],
        "description": task.get("description", ""),
        "acceptance_criteria": task.get("acceptance_criteria", []),
        "source": source,
        "project_gid": task.get("project_gid"),
        "section_gid": task.get("section_gid"),
        "assignee_gid": task.get("assignee_gid"),
        "due_date": task.get("due_date"),
        "priority": priority(task["urgency"], task["impact"]),
        "confidence": task.get("confidence", 0.0),
        "review_required": True,
        "fingerprint": fingerprint(source["type"], source["id"], task["title"]),
        "status": "pending_review",
        "uncertain_fields": [f for f in ("project_gid", "section_gid", "assignee_gid", "due_date") if not task.get(f)],
    }
    validate_proposal(data)
    return data
