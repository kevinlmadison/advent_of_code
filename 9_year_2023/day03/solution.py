import re
import math

def get_neighbors(row: int, m: re.Match) -> list[str]:
    rv  = [(row - 1, x) for x in range(m.start() - 1, m.end() + 1)]
    rv += [(row, m.start() - 1), (row, m.end())]
    rv += [(row + 1, x) for x in range(m.start() - 1, m.end() + 1)]
    return rv
          

def part1(inputs: list[str]) -> int:
    total = 0

    for i, input in enumerate(inputs):
        for match in re.finditer(r'\d+', input):
            for (x, y) in get_neighbors(i, match):
                char = inputs[x][y] if 0 <= x < len(inputs) - 1\
                       and 0 <= y < len(inputs[0]) - 1 else '.'
                if not char.isdigit() and char != '.':
                    total += int(match.group(0))
                    break
    return total
                   
    
def part2(inputs):
    total = 0
    gears = {}

    for i, input in enumerate(inputs):
        for match in re.finditer(r'\d+', input):
            for (x, y) in get_neighbors(i, match):
                char = inputs[x][y] if 0 <= x < len(inputs)\
                       and 0 <= y < len(inputs[0]) else '.'
                if char == '*':
                    gears[(x, y)] = gears.get((x, y), []) + [int(match.group(0))]

    return sum([math.prod(x) for x in gears.values() if len(x) == 2])

def main():
    inputs_1 = list(open('input').readlines())
    inputs_2 = list(open('input').readlines())
    print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')

if __name__ == '__main__':
    main()
