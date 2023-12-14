import re
import math

def process(line):
    if not any(line):
        return 0
    m = [b - a for a, b in zip(line, line[1:])]
    return line[-1] + process(m)


def part1(f):
    input = [[int(x) for x in n.split()] for n in f.split('\n') if n.strip()]
    return sum(process(i) for i in input)

def part2(f):
    input = [[int(x) for x in n.split()] for n in f.split('\n') if n.strip()]
    return sum(process(i[::-1]) for i in input)


def main():
    # inputs_1 = open('input').read()
    inputs_2 = open('input').read()
    # print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')


if __name__ == '__main__':
    main()
