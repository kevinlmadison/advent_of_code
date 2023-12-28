#!/usr/bin/env pypy3
from itertools import combinations

def _(tuple):


    def __sub__(self, other):
        return _(abs(x - y) for x,y in zip(self, other))


def expand(f):
    nf = []

    for l in f:
        if '#' in l:
            nf += [l]
        else:
            nf += 2 * [l]
    return nf

def part1(f):


    f = f.splitlines()
    nf = expand(f)
    nf = expand(zip(*nf))
    coords = [(r, c) for r, row in enumerate(nf)
             for c, ch in enumerate(row) if ch == '#']

    combs = combinations(coords, 2)
    return sum([abs(x-i) + abs(y-j) for ((x,y), (i,j)) in combs])

def expand_big(f):
    return [i for i, l in enumerate(f) if '#' not in l]


def part2(f):


    f = f.splitlines()
    rows = expand_big(f)
    cols = expand_big(zip(*f))
    print(f'{f}, {rows}, {cols}')
    coords = [(r, c) for r, row in enumerate(f)
             for c, ch in enumerate(row) if ch == '#']
    combs = combinations(coords, 2)

    def get_big_dist(a, b):
        (x,y), (i,j) = a, b
        small_dist = abs(x - i) + abs(y - j)
        for row in rows:
            if row in (range(x, i) if x < i else range(i, x)):
                small_dist += 999999

        for col in cols:
            if col in (range(y, j) if y < j else range(j, y)):
                small_dist += 999999
        return small_dist
 
    return sum([get_big_dist(x, y) for x,y in combs])



def main():
    inputs_1 = open('test_input').read()
    # inputs_2 = open('input').read()
    print(f'part 1: {part1(inputs_1)}')
    # print(f'part 2: {part2(inputs_2)}')


if __name__ == '__main__':
    main()
