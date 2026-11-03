"""Boundary and branch tests for the supplied password policy."""

import pytest

from password_policy import check_password, strength, suggest_fix


def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"


@pytest.mark.parametrize(
    "password, expected",
    [
        ("", ["too short", "no uppercase", "no lowercase", "no digit", "no special"]),
        ("Aa1!abc", ["too short"]),
        ("Aa1!abcd", []),
        ("Aa1!abcde", []),
        ("Aa1!" + "a" * 59, []),
        ("Aa1!" + "a" * 60, []),
        ("Aa1!" + "a" * 61, ["too long"]),
    ],
    ids=["empty", "length-7", "length-8", "length-9", "length-63", "length-64", "length-65"],
)
def test_password_length_boundaries(password, expected):
    assert check_password(password) == expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("abcdef1!", ["no uppercase"]),
        ("ABCDEF1!", ["no lowercase"]),
        ("Abcdefg!", ["no digit"]),
        ("Abcdef12", ["no special"]),
    ],
    ids=["uppercase", "lowercase", "digit", "special"],
)
def test_each_missing_character_category(password, expected):
    assert check_password(password) == expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("password", ["common", "no uppercase", "no digit", "no special"]),
        ("PASSWORD", ["common", "no lowercase", "no digit", "no special"]),
        ("PaSsWoRd", ["common", "no digit", "no special"]),
        ("123456", ["too short", "common", "no uppercase", "no lowercase", "no special"]),
        ("qwerty", ["too short", "common", "no uppercase", "no digit", "no special"]),
        ("letmein", ["too short", "common", "no uppercase", "no digit", "no special"]),
    ],
    ids=["password", "uppercase-common", "mixed-case-common", "digits-common", "qwerty", "letmein"],
)
def test_common_passwords_and_issue_order(password, expected):
    assert check_password(password) == expected


def test_common_word_with_extra_characters_is_not_an_exact_common_match():
    assert check_password("Password1!") == []


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Aa1!abc", "weak"),
        ("Aa1!abcd", "good"),
        ("Aa1!" + "a" * 9, "good"),
        ("Aa1!" + "a" * 10, "strong"),
        ("Aa1!" + "a" * 60, "strong"),
        ("Aa1!" + "a" * 61, "weak"),
        ("abcdef1!", "weak"),
        ("abcdef12", "weak"),
        ("abcdefgh", "very weak"),
        ("", "very weak"),
    ],
    ids=["length-7", "length-8", "length-13", "length-14", "length-64", "length-65", "one-issue", "two-issues", "three-issues", "empty"],
)
def test_strength_boundaries_and_issue_counts(password, expected):
    assert strength(password) == expected


@pytest.mark.parametrize(
    "issues, expected",
    [
        ([], "none needed"),
        (["too short"], "add more characters"),
        (["common"], "avoid common passwords"),
        (["no uppercase"], "add uppercase"),
        (["no lowercase"], "add lowercase"),
        (["no digit"], "add digit"),
        (["no special"], "add special"),
        (["too long"], "shorten it"),
        (["unrecognized issue"], "shorten it"),
    ],
    ids=["none", "too-short", "common", "uppercase", "lowercase", "digit", "special", "too-long", "fallback"],
)
def test_fix_for_each_issue(issues, expected):
    assert suggest_fix(issues) == expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("123456", "add more characters"),
        ("password", "avoid common passwords"),
        ("abcdefgh", "add uppercase"),
    ],
    ids=["length-before-common", "common-before-category", "first-missing-category"],
)
def test_fix_uses_first_issue_from_checker_without_changing_the_list(password, expected):
    issues = check_password(password)
    original = issues.copy()
    assert suggest_fix(issues) == expected
    assert issues == original


@pytest.mark.parametrize(
    "password",
    ["Abcdef1 ", "Abcdef1\n", "\u00c9bcdef1!", "Abcdef\u0661!"],
    ids=["space-is-special", "newline-is-special", "unicode-uppercase", "unicode-digit"],
)
def test_existing_whitespace_and_unicode_classification(password):
    # These document the supplied Python character-classification behavior.
    assert check_password(password) == []


def test_results_are_independent_between_calls():
    first = check_password("Abcdef1!")
    first.append("caller change")
    assert check_password("Abcdef1!") == []
