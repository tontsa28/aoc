def solve_part1(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()
    return sum([abs(l - r) for l, r in zip(left, right)])

def solve_part2(left: list[int], right: list[int]) -> int:
    return sum([l * right.count(l) for l in left])

def main():
    left: list[int] = []
    right: list[int] = []

    with open('input.txt') as file:
        for line in file:
            splitted = line.split('   ')
            left.append(int(splitted[0]))
            right.append(int(splitted[1].removesuffix('\n')))

    print('Part 1:', solve_part1(left, right))
    print('Part 2:', solve_part2(left, right))

if __name__ == '__main__':
    main()
