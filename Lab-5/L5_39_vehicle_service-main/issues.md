# Lab 5: Static Code Analysis - Identified Issues

All line numbers below refer to the original teacher-provided `vehicle_service.py`
used for the reports in `reports/before/`. High-severity findings are listed first.
Bandit reported no medium-severity findings. Pylint and Flake8 findings are labeled
by their tool categories rather than assigning them Bandit severity levels.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Shell command injection (Bandit B602) | Security - High | 61 | The destination is concatenated into a command executed with `shell=True`; shell metacharacters can execute unintended commands. | Replace shell execution with `shutil.copy2("services.json", folder)`. |
| Weak MD5 hash (Bandit B324) | Security - High | 39 | Bandit flags MD5 as a weak hash. The job-card ID is a display identifier, but the default hash call does not declare that limited use. | Use SHA-256 with explicit UTF-8 input, keeping the eight-character display format. The identifier changes and is not an authentication token or a guarantee of uniqueness. |
| Subprocess import (Bandit B404) | Security - Low | 3 | The subprocess module brings process-execution risks into a helper that only needs to copy a file. | Replace the subprocess import with `shutil` and use its file-copy API. |
| Hardcoded password (Bandit B105) | Security - Low | 8 | The unused `ADMIN_PASSWORD` embeds a password-like literal in the source. | Remove the unused constant; no authentication behavior depends on it. |
| Mutable default argument (Pylint W0102) | Bug - Warning | 12, 16 | The default `history=[]` is shared between calls, so unrelated calls accumulate vehicle numbers in the same list. | Default to `None` and create a fresh list inside the function; preserve explicitly supplied history lists. |
| Broad exception handler (Pylint W0718) | Reliability - Warning | 21-25 | Catching every `Exception` can hide unexpected defects when looking up a vehicle. | Catch only `KeyError`, preserving the missing-vehicle message and `False` return value. |
| Unspecified file encoding (Pylint W1514) | Portability - Warning | 50 | Saving records depends on the operating system default encoding, while loading already specifies UTF-8. | Specify `encoding="utf-8"` when writing JSON. |
| Missing documentation (Pylint C0114, C0116) | Maintainability - Convention | 1, 12, 20, 31, 38, 42, 49, 54, 59, 64 | The module and functions lack docstrings describing their purpose. | Add a module docstring and concise function docstrings. |
| Nonstandard names (Pylint C0103) | Maintainability - Convention | 12, 20, 31-39, 42, 49-55, 59 | Function names, arguments and local variables use camelCase. | Rename them to snake_case and update every internal call. |
| Missing comma spacing (Flake8 E231) | Style | 7 | There is no space after the comma before the brake-check rate. | Add the required space after the comma. |
| Missing assignment spacing (Flake8 E225) | Style | 43 | `best=None` omits spaces around the assignment operator. | Write `best = None`. |
| Missing top-level blank line (Flake8 E302) | Style | 49 | Only one blank line separates two top-level functions. | Use two blank lines between top-level functions. |
| Overlong output line (Flake8 E501) | Style | 77 | The final print statement is 83 characters, exceeding the 79-character limit. | Wrap the print arguments across multiple lines without changing the output. |

## Verification

All issues in the table have been fixed in the final `vehicle_service.py`.
No rules were disabled and no findings were suppressed.

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.66/10 | 10.00/10; no findings |
| Bandit | 4 findings: 2 high, 2 low | No issues identified |
| Flake8 | 4 formatting violations | No findings; the report is empty |

The original reports are in `reports/before/`; the final reports are in
`reports/after/`. Each directory contains `pylint_report.txt`,
`bandit_report.txt`, and `flake8_report.txt`. All three final tool commands
exited with status 0.

The demonstration was run before and after the fixes. Both runs report the
missing vehicle KA09ZZ0001, totals of 2300 and 2500, three vehicles on file,
and KA01AB1234 as the busiest vehicle. The job-card ID changes from `353ee89f`
to `bd2cd41f` because SHA-256 replaces MD5; it remains a stable eight-character
display identifier.

The three fix commits address Bandit security, Pylint code quality, and Flake8
formatting respectively. `reflection.md` is omitted as requested.
