def solve_part1(reports: list[list[int]]) -> int:
    safe = 0
    for report in reports:
        if report == sorted(report) or report == sorted(report, reverse=True):
            diffs = [abs(b - a) for a, b in zip(report, report[1:])]
            if all(1 <= diff <= 3 for diff in diffs):
                safe += 1
    return safe

def solve_part2(reports: list[list[int]]) -> int:
    safe = 0
    for report in reports:
        temp = report.copy()
        ri = 0
        while ri < len(report):
            rn = temp.pop(ri)
            if temp == sorted(temp) or temp == sorted(temp, reverse=True):
                diffs = [abs(b - a) for a, b in zip(temp, temp[1:])]
                if all(1 <= diff <= 3 for diff in diffs):
                    safe += 1
                    break
            temp.insert(ri, rn)
            ri += 1
    return safe

def main():
    reports: list[list[int]] = []

    with open('input.txt') as file:
        for line in file:
            splitted = line.split(' ')
            reports.append([int(i) for i in splitted])

    print('Part 1:', solve_part1(reports))
    print('Part 2:', solve_part2(reports))

if __name__ == '__main__':
    main()
