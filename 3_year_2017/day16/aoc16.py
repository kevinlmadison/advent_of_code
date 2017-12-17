from collections import *
from functools import reduce
import itertools
def solve(moves):
    d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    seen = set()
    for idx in range(40):  # the pattern repeats every 60 iterations so 1 billion % 60 = 40
        for m in moves:
            if m[0] == 's':
                s = int(m[1:])
                d = d[-s:] + d[:-s]
            if m[0] == 'x':
                x = m[1:].split('/')
                x1, x2 = int(x[0]), int(x[1])
                d[x1], d[x2] = d[x2], d[x1]
            if m[0] == 'p':
                p = m[1:].split('/')
                i, j = d.index(p[0]), d.index(p[1])
                d[i], d[j] = p[1], p[0]
                
        if idx == 0:
            print('part 1: {}'.format(''.join(d)))

        ''' This was used to figure out how long it took to repeat a permutation

        D = ''.join(d)
        if D not in seen:
            seen.add(D)
        else:
            print('iter: {}'.format(idx))

        '''

    print('part 2: {}'.format(''.join(d)))

def main():
    f = open('input.txt').readline().split(',')
    solve(f)

if __name__ == '__main__':
    main()
