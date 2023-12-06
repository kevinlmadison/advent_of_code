import re
import math
from collections import Counter

def part1(inputs: list[str]) -> int:
    stuff = [[] for _ in range(8)]
    cat = 0
    for line in inputs:
        m = re.findall(r'\d+', line)
        if line.startswith('\n'):
            cat += 1
        if len(m) > 0:
            stuff[cat] += [m]
                   
    return stuff
    
def part2(inputs):
    ...


def main():
    inputs_1 = list(open('test_input').readlines())
    # inputs_2 = list(open('input').readlines())
    print(f'part 1: {part1(inputs_1)}')
    # print(f'part 2: {part2(inputs_2)}')

if __name__ == '__main__':
    main()
