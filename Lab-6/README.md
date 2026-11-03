# Lab 6 - Code and Branch Coverage

**Atul Suresh | PES1UG24CS098 | Section B**

[Assigned scenario: Password Policy Checker](https://github.com/SETAPESU26/L6_L7_39_password_policy).
The supplied `password_policy.py` is unchanged from upstream commit `bbef87f`.

| Separate test file | Tests passed | Statement coverage | Branch coverage |
| --- | ---: | ---: | ---: |
| `test_code_coverage.py` | 47 | 100% (47/47) | Not measured |
| `test_branch_coverage.py` | 12 | 100% (47/47) | 100% (36/36) |

Both metrics exceed the required 90%. Only `password_policy.py` is measured.
The tests are recorded in separate code-coverage and branch-coverage commits.

## Run

From this folder, using Python 3.10+ (tested on 3.12.14):

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

python3 -m pytest test_code_coverage.py --cov=password_policy --cov-report=term-missing --cov-report=json:evidence/code_coverage.json --cov-fail-under=90
python3 show_coverage.py evidence/code_coverage.json

python3 -m pytest test_branch_coverage.py --cov=password_policy --cov-branch --cov-report=term-missing --cov-report=json:evidence/branch_coverage.json --cov-fail-under=90
python3 show_coverage.py evidence/branch_coverage.json
```

The summary helper checks line and branch percentages separately.
Run `python3 -m pytest` to run all 59 cases together.

## Submit

Upload `PES1UG24CS098_Lab6_Code_Branch_Coverage.pdf` to the class form.
It contains both complete test files, results, terminal screenshots and commands.
The screenshots show assisted Linux execution. Raw logs and coverage data are
in `evidence/`; the two terminal screenshots are in `screenshots/`.
