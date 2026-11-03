"""Exercise both outcomes of the policy's decisions independently."""

import pytest

from password_policy import check_password, strength, suggest_fix


@pytest.mark.parametrize(
    "password, issues, rating, fix",
    [
        ("Abcdef1!", [], "good", "none needed"),
        ("Aa1!" + "a" * 10, [], "strong", "none needed"),
        ("Ab1!", ["too short"], "weak", "add more characters"),
        ("Aa1!" + "a" * 61, ["too long"], "weak", "shorten it"),
        ("password", ["common", "no uppercase", "no digit", "no special"], "very weak", "avoid common passwords"),
        ("abcdef1!", ["no uppercase"], "weak", "add uppercase"),
        ("ABCDEF1!", ["no lowercase"], "weak", "add lowercase"),
        ("Abcdefg!", ["no digit"], "weak", "add digit"),
        ("Abcdef12", ["no special"], "weak", "add special"),
        ("abcdef12", ["no uppercase", "no special"], "weak", "add uppercase"),
        ("abcdefgh", ["no uppercase", "no digit", "no special"], "very weak", "add uppercase"),
        ("", ["too short", "no uppercase", "no lowercase", "no digit", "no special"], "very weak", "add more characters"),
    ],
    ids=[
        "valid-good", "valid-strong", "too-short", "too-long", "common",
        "missing-uppercase", "missing-lowercase", "missing-digit",
        "missing-special", "two-issues", "three-issues", "empty-loop",
    ],
)
def test_policy_decision_paths(password, issues, rating, fix):
    assert check_password(password) == issues
    assert strength(password) == rating
    assert suggest_fix(issues) == fix
