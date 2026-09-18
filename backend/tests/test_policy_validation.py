from app.demo_data import DEMO_POLICY
from app.models import Policy, PolicyRule, RuleEffect
from app.policy_validation import VALIDATION_FIXTURES, validate_policy


def expected_policy() -> Policy:
    return Policy(
        version=DEMO_POLICY.version,
        rules=[rule.model_copy(deep=True) for rule in DEMO_POLICY.rules],
    )


def test_validation_suite_passes_a_policy_with_intended_authority() -> None:
    result = validate_policy(expected_policy())
    assert result.passed is True
    assert result.status == "passed"
    assert result.passed_checks == result.total_checks == len(VALIDATION_FIXTURES) == 18
    assert all(case.passed for case in result.cases)
    assert "No agent, command, file, or network action was executed" in result.message


def test_validation_suite_identifies_missing_useful_capability() -> None:
    policy = expected_policy()
    policy.rules = [rule for rule in policy.rules if rule.id != "allow-tests"]
    result = validate_policy(policy)
    failed = [case for case in result.cases if not case.passed]
    assert result.passed is False
    assert result.status == "failed"
    assert [case.id for case in failed] == ["run-pytest"]
    assert failed[0].actual.value == "deny"


def test_validation_suite_distinguishes_delete_approval_from_required_denial() -> None:
    policy = expected_policy()
    policy.rules = [
        rule.model_copy(update={"effect": RuleEffect.APPROVAL_REQUIRED}) if rule.id == "approval-for-delete" else rule
        for rule in policy.rules
    ]
    result = validate_policy(policy)
    deletion = next(case for case in result.cases if case.id == "delete")
    assert result.passed is False
    assert deletion.expected.value == "deny"
    assert deletion.actual.value == "approval_required"
    assert deletion.passed is False
