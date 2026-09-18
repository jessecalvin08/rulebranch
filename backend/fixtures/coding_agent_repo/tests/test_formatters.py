from src.formatters import normalize_branch_name


def test_normalize_branch_name_preserves_product_casing() -> None:
    assert normalize_branch_name("  RuleBranch    Safety ") == "RuleBranch Safety"
