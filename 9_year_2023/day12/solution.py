#!/usr/bin/env pypy3
from itertools import combinations

def count(cfg, nums):
    if cfg == '':
        return 1 if nums == () else 0
    if nums == ():
        return 0 if '#' in cfg else 1
    result = 0
    if cfg[0] in '.?':
        result += count(cfg[1:], nums)
    if cfg[0] in '#?':
        if nums[0] <= len(cfg) and '.' not in cfg[:nums[0]] \
        and (nums[0] == len(cfg) or cfg[nums[0]] != '#'):
            result += count(cfg[nums[0] + 1:], nums[1:])

    return result

def part1(f):
    f = f.splitlines()
    total = 0
    for line in f:
        cfg, nums = line.split()
        nums = tuple(map(int, nums.split(',')))
        total += count(cfg, nums)

    return total


    
def part2(f):
    ...



def main():
    inputs_1 = open('input').read()
    # inputs_2 = open('input').read()
    print(f'part 1: {part1(inputs_1)}')
    # print(f'part 2: {part2(inputs_2)}')


if __name__ == '__main__':
    main()
