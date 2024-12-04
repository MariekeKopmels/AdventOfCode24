

def process_reports():
    report = []
    no_safe_reports = 0
    input_file = open('input.txt', 'r')
    while True:
        content=input_file.readline().split()
        if not content:
            break
        report = [int(item) for item in content]
        if is_safe_report(report):
            no_safe_reports += 1
    input_file.close()
    return no_safe_reports


def is_safe_report(report):
    increasing = 1 if ((report[0] - report[1]) <= 0) else -1
    for i in range(len(report)-1):
        value = (report[i] - report[i+1]) * increasing
        if value < -3 or value >= 0:
            return False
    return True

if __name__ == "__main__":
    no_safe_reports = process_reports()
    print(no_safe_reports)