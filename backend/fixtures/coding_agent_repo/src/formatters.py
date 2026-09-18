def normalize_branch_name(value: str) -> str:
    """Return the display name used for a RuleBranch policy branch."""
    return " ".join(value.strip().split()).lower()
