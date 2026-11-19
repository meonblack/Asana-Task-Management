"""Review-first local CLI; deliberately never writes to Asana."""
from __future__ import annotations
import json
import sys
from pathlib import Path
from src.rules import prepare_draft


def main(argv=None):
    argv = argv or sys.argv[1:]
    if len(argv) != 1:
        print("Usage: python -m src.cli examples/sample-input.json", file=sys.stderr)
        return 2
    data = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    result = [prepare_draft(task, data["source"]) for task in data["tasks"]]
    print(json.dumps({"mode": "DRY_RUN", "published": False, "proposals": result}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
