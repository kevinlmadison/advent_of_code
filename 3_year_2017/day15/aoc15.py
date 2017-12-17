from collections import *
from functools import reduce
import itertools

def solve1(a, b):
    fa, fb = 16807, 48271
    div = 2147483647
    matches = 0
    for i in range(40000000):
        a *= fa
        b *= fb
        a %= div
        b %= div

        if format(a, 'b')[-16:] == format(b, 'b')[-16:]:
            matches += 1

    print('part 1 matches: {}'.format(matches))

def solve2(a, b):
    fa, fb = 16807, 48271
    div = 2147483647
    matches = 0
    def genA(a):
        while True:
            a *= fa
            a %= div
            if a % 4 == 0:
                yield a

    def genB(b):
        while True:
            b *= fb
            b %= div
            if b % 8 == 0:
                yield b

    ga, gb = genA(a), genB(b)
    for _ in range(5000000):
        if format(next(ga), 'b')[-16:] == format(next(gb), 'b')[-16:]:
            matches += 1

    print('part 2 matches: {}'.format(matches))

def main():
    gen_A, gen_B = 516, 190
    solve1(gen_A, gen_B)
    gen_A, gen_B = 516, 190
    solve2(gen_A, gen_B)

if __name__ == '__main__':
    main()
