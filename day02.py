def is_ordered(report, reverse=False):
    sorted_report = report.copy()
    sorted_report = sorted(sorted_report, reverse=reverse)
    return (report == sorted_report)

def is_diff_ok(report, step=3):
    for i in range(len(report)-1):
        if abs(report[i+1] - report[i]) > step or abs(report[i+1] - report[i]) == 0:
            return False
    return True

def is_report_safe(report):
    if report[0] < report[1]: #increasing
        return 1 if is_ordered(report, reverse=False) and is_diff_ok(report, step=3) else 0
    elif report[0] > report[1]: #decreasing 
        return 1 if is_ordered(report, reverse=True) and is_diff_ok(report, step=3) else 0
    else: #constant
        return 0

def is_ok_with_problem_dampener(report):
    if is_report_safe(report) or is_report_safe(report[:len(report)-1]):
        return True
    for i in range(0, len(report)-1):
        new_report = report[:i] + report[i+1:]
        if is_report_safe(new_report):
            return True
    return False

with open("input/day02-input.txt", "r") as file:
    count1 = 0
    count2 = 0
    for line in file:
        report = [int(s) for s in line.strip().split()]
        count1 += is_report_safe(report)
        count2 += is_ok_with_problem_dampener(report)
    print(f"Safe reports count: {count1}")
    print(f"Safe reports count with problem dampener: {count2}")