"""One bounded provider check. Prints only sanitized diagnostic information."""

import json

from openai import APIStatusError

from .nebius_client import compile_policy


def main() -> None:
    try:
        policy, model, mode = compile_policy(
            "Allow reading README.md, src/ and tests/. Allow writing src/ and running pytest. "
            "Deny reading .env or .git, deletion, and network requests."
        )
        print(json.dumps({"status": "compiled", "model": model, "response_mode": mode, "rule_count": len(policy.rules)}))
    except APIStatusError as error:
        print(json.dumps({"status": "rejected", "http_status": error.status_code, "type": type(error).__name__}))
        raise SystemExit(1) from None
    except Exception as error:
        print(json.dumps({"status": "failed", "type": type(error).__name__}))
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
