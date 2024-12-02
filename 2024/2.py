from get_input import get_input
from pprint import pprint

reports = list(
    map(
        lambda report: list(map(lambda blah: int(blah), report.strip().split())),
        get_input(2),
    )
)


def get_diffs_for_line(line: list[int]) -> list[int]:
    diffs = []
    line_offset = line[1:]
    for a, b in zip(line, line_offset):
        diffs.append(abs(a - b))
    return diffs


def is_report_safe(report: list[int]) -> bool:
    diffs = get_diffs_for_line(report)
    if diffs == None:
        print(report)
    if any(map(lambda level_diff: level_diff < 1 or level_diff > 3, diffs)):
        return False

    levels_asc = sorted(report, reverse=False)
    levels_desc = sorted(report, reverse=True)
    if report != levels_asc and report != levels_desc:
        return False

    return True


num_safe_reports = 0
for report in reports:
    if is_report_safe(report):
        num_safe_reports += 1

print(f"{num_safe_reports} safe reports")


# pprint(reports)
