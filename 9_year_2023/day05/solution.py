import re
import math
from collections import Counter

def get_neighbors(row: int, m: re.Match) -> list[str]:
    rv  = [(row - 1, x) for x in range(m.start() - 1, m.end() + 1)]
    rv += [(row, m.start() - 1), (row, m.end())]
    rv += [(row + 1, x) for x in range(m.start() - 1, m.end() + 1)]
    return rv
          

def part1(inputs: list[str]) -> int:
    total = 0
    for line in inputs:
        exp = -1
        line = " ".join(line.strip().split(' ')[2:]).split('|')
        for m in re.finditer(r'\d+', line[1]):
            if m.group(0) in line[0].split(' '):
                exp += 1
        if exp > (-1):
            total += 2 ** exp
    return total
                   
    
def part2(inputs):
    mlts = [1] * len(inputs)
    for i, line in enumerate(inputs):
        exp = -1
        line = " ".join(line.strip().split(' ')[2:]).split('|')
        for m in re.finditer(r'\d+', line[1]):
            if m.group(0) in line[0].split(' '):
                    exp += 1
        if exp > (-1):
            for j in range(i + 1, (i + 1) + (exp + 1)):
                mlts[j] += mlts[i]
    total = sum(mlts)

    return total


def main():
    inputs_1 = list(open('input').readlines())
    inputs_2 = list(open('input').readlines())
    print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')

if __name__ == '__main__':
    main()
