"""Print separate line/branch percentages and enforce the lab's 90% minimum."""

import json
import sys
from pathlib import Path


def main():
    report = json.loads(Path(sys.argv[1]).read_text())
    summary = report["totals"]
    lines = summary["num_statements"]
    covered_lines = summary["covered_lines"]
    line_percent = 100 * covered_lines / lines
    print(f"Line coverage:   {covered_lines}/{lines} ({line_percent:.2f}%)")
    passed = line_percent >= 90
    if "num_branches" in summary:
        branches = summary["num_branches"]
        covered_branches = summary["covered_branches"]
        branch_percent = 100 * covered_branches / branches
        print(f"Branch coverage: {covered_branches}/{branches} ({branch_percent:.2f}%)")
        passed = passed and branch_percent >= 90
    print("90% minimum: " + ("PASS" if passed else "FAIL"))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
