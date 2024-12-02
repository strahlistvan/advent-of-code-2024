def is_ordered(report, reverse=False):
    sorted_report = report.copy()
    sorted_report = sorted(sorted_report, reverse=reverse)
    return (report == sorted_report)

def is_ordered_impl(report, reverse=False):
    for i in range(len(report)-1):
        if report[i] <= report[i+1] and reverse:
            return False
        if report[i] >= report[i+1] and not reverse:
            return False
    return True

def is_diff_ok(report, step=3):
    prev = report[0] + 1 #init
    for curr in report:
        if abs(curr - prev) > step or abs(curr - prev) == 0:
            return False
        prev = curr
    return True

def is_report_safe(report):
    if report[0] < report[1]: #increasing
        return 1 if is_ordered(report, reverse=False) and is_diff_ok(report, step=3) else 0
    elif report[0] > report[1]: #decreasing 
        return 1 if is_ordered(report, reverse=True) and is_diff_ok(report, step=3) else 0
    else: #constant
        return 0

with open("input/day02-input.txt", "r") as file:
    count = 0
    for line in file:
        report = line.strip().split()
        report = [int(s) for s in report]
        count += is_report_safe(report)
        print(report)
    print(f"Biztonságos riportok száma: {count}")