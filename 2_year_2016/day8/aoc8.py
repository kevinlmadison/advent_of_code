import re


def main(file):

    grid = [
            [0 for _ in range(50)]
            for _ in range(6)
            ]
    for line in file:
        m = re.match(r'rect (\d+)x(\d+)', line)
        if m:
            width, height = map(int, m.groups())
            for i in range(height):
                for j in range(width):
                    grid[i][j] = 1
        else:
            coord, row, num = re.match(r'rotate \w+ (x|y)=(\d+) by (\d+)', line).groups()
            row, num = int(row), int(num)
            if coord == 'x':
                grid = list(map(list, zip(*grid)))
                grid[row] = grid[row][-num:] + grid[row][:-num]
                grid = list(map(list, zip(*grid)))
            if coord == 'y':
                grid[row] = grid[row][-num:] + grid[row][:-num]


    #Part 1
    print(sum(map(sum, grid)))
    #Part 2
    for line in grid:
        print(''.join('#' if c else ' ' for c in line))

if __name__ == '__main__':
    with open('aoc8.txt', 'r') as file:
        main(file)
