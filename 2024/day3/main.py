import re

def solve_part1(data: str) -> int:
    regex: str = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches: list[tuple[str, str]] = re.findall(regex, data)
    return sum([int(i) * int(j) for i, j in matches])

def solve_part2(data: str) -> int:
    regex: str = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
    matches: list[tuple[str, str, str]] = re.findall(regex, data)

    temp = matches.copy()
    do = True
    for match in temp:
        if match[0] == "do()":
            do = True
            matches.remove(match)
            continue
        elif match[0] == "don't()":
            do = False
            matches.remove(match)
            continue
        if not do:
            matches.remove(match)
    return sum([int(m[1]) * int(m[2]) for m in matches])

def main():
    with open('input.txt') as file:
        data: str = ''.join([line.removesuffix('\n') for line in file])

    print('Part 1:', solve_part1(data))
    print('Part 2:', solve_part2(data))

if __name__ == '__main__':
    main()
