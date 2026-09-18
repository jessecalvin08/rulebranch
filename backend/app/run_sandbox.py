"""Explicit CLI approval gate for the Nebius Sandbox comparison.

Example from backend/: python -m app.run_sandbox --reviewed-policy policy.json --approve
The policy JSON must be a previously reviewed RuleBranch draft.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .models import Policy
from .sandbox_runner import run_sandbox_comparison


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the synthetic RuleBranch fixture in Nebius Sandboxes")
    parser.add_argument("--reviewed-policy", type=Path, required=True, help="Path to a policy JSON you reviewed")
    parser.add_argument("--approve", action="store_true", help="Explicitly authorize this opt-in paid API/Sandbox run")
    parser.add_argument("--output", type=Path, help="Optional JSON evidence output path; reports/ is gitignored")
    args = parser.parse_args()
    if not args.approve:
        parser.error("Review the policy and pass --approve to authorize the run.")
    policy = Policy.model_validate_json(args.reviewed_policy.read_text(encoding="utf-8"))
    result = run_sandbox_comparison(policy)
    rendered = result.model_dump_json(indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
        print(json.dumps({"evidence_type": result.evidence_type, "output": str(args.output)}))
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
