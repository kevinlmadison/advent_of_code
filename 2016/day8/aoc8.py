import re
def main(file):

    grid = [
            [0 for _ in range(50)]
            for _ in range(6)
            ]
    print(grid)
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
            if coord == 'y':
                grid = list(map(list, zip(*grid)))
                grid[row]

    #Part 1
    return sum(map(sum, grid))

main()
