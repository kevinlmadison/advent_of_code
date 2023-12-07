import re
import math
from collections import Counter

def part1(inputs: list[str]) -> int:
    seeds = [[] for _ in range(8)]
    cat = 0
    for line in inputs:
        m = re.findall(r'\d+', line)
        if line.startswith('\n'):
            cat += 1
        if len(m) > 0:
            seeds[cat] += [m]

    locs = []
    for seed in seeds[0]:
        seed = list(map(int, seed))
        for s in seed:
            for instrs in seeds[1:]:
                for instr in instrs:
                    instr = list(map(int, instr))
                    if (instr[1]) <= s <= (instr[1] + instr[2]):
                        s = instr[0] + (s - instr[1])
                        break
            locs += [s]

    return min(locs)
    
def part2(inputs):
    seeds = [[] for _ in range(8)]
    cat = 0
    for line in inputs:
        m = re.findall(r'\d+', line)
        if line.startswith('\n'):
            cat += 1
        if len(m) > 0:
            seeds[cat] += [m]

    seed = list(map(int, seeds[0][0]))
    seed_ranges = []
    for x in range(0, len(seed), 2):
        seed_ranges.append((seed[x], seed[x] + seed[x + 1]))
    print(seed_ranges)

    for i in range(10000000000):
        rv = i
        for instrs in seeds[:0:-1]:
            for instr in instrs:
                instr = list(map(int, instr))
                if (instr[0]) <= i <= (instr[0] + instr[2]):
                    i = instr[1] + (i - instr[0])
                    break
        for (x, y) in seed_ranges:
            if x <= i <= y:
                return rv
def main():
    # inputs_1 = list(open('input').readlines())
    inputs_2 = list(open('input').readlines())
    # print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')

if __name__ == '__main__':
    main()
