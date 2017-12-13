from collections import *
from functools import reduce
from itertools import *

def solve(lines):
    t = [line.split(': ') for line in lines]
    s = {int(i): int(j) for i, j in t}

    def scan(height, time):
        offset = time % ((height - 1) * 2)
        return (2 * (height - 1) - offset) if offset > (height - 1) else offset

    '''This solution was based on one of the ones on reddit, after I solved it on my own 
    using a terribly inefficient method. This method is just a more elegant way of doing
    exactly the same thing that I was doing but it uses a generator for part2.
    '''
    part1 = sum(s[i] * i for i in s if scan(s[i], i) == 0)
    print('part1: {}'.format(part1))
    part2 = next(pause for pause in count() if not any(scan(s[i], i + pause) == 0 for i in s))
    print('part2: {}'.format(part2))


def main():
    f = open('input.txt').readlines()
    solve(f)

if __name__ == '__main__':
    main()
