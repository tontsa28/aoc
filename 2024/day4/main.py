def solve_part1(grid: list[list[str]]) -> int:
    count = 0
    for row in grid:
        s = ''.join(row)
        count += s.count('XMAS')
        count += s.count('SAMX')
    for col in range(len(grid[0])):
        s = ''.join([row[col] for row in grid])
        count += s.count('XMAS')
        count += s.count('SAMX')
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            try:
                if grid[i][j] == 'X' and grid[i + 1][j + 1] == 'M' and grid[i + 2][j + 2] == 'A' and grid[i + 3][j + 3] == 'S':
                    count += 1
                if grid[i][j] == 'S' and grid[i + 1][j + 1] == 'A' and grid[i + 2][j + 2] == 'M' and grid[i + 3][j + 3] == 'X':
                    count += 1
                if grid[i][j] == 'X' and grid[i + 1][j - 1] == 'M' and grid[i + 2][j - 2] == 'A' and grid[i + 3][j - 3] == 'S':
                    count += 1
                if grid[i][j] == 'S' and grid[i + 1][j - 1] == 'A' and grid[i + 2][j - 2] == 'M' and grid[i + 3][j - 3] == 'X':
                    count += 1
            except IndexError:
                continue
    return count


def solve_part2(grid: list[list[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            try:
                if grid[i][j] == 'M' and grid[i + 1][j + 1] == 'A' and grid[i + 2][j + 2] == 'S' and grid[i + 2][j] == 'M' and grid[i][j + 2] == 'S':
                    count += 1
                if grid[i][j] == 'S' and grid[i + 1][j + 1] == 'A' and grid[i + 2][j + 2] == 'M' and grid[i + 2][j] == 'S' and grid[i][j + 2] == 'M':
                    count += 1
                if grid[i][j] == 'M' and grid[i + 1][j + 1] == 'A' and grid[i + 2][j + 2] == 'S' and grid[i + 2][j] == 'S' and grid[i][j + 2] == 'M':
                    count += 1
                if grid[i][j] == 'S' and grid[i + 1][j + 1] == 'A' and grid[i + 2][j + 2] == 'M' and grid[i + 2][j] == 'M' and grid[i][j + 2] == 'S':
                    count += 1
            except IndexError:
                continue
    return count

def main():
    with open('input.txt') as file:
        data: list[list[str]] = [list(line.removesuffix('\n')) for line in file]

    print('Part 1:', solve_part1(data))
    print('Part 2:', solve_part2(data))

if __name__ == '__main__':
    main()
