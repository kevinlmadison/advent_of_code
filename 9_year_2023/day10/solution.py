#!/usr/bin/env pypy3
from collections import deque

class _(tuple):

    def __add__(self, other):
        return _(x + y for x,y in zip(self, other))

    def __neg__(self):
        return _(-x for x in self)

ADJ = {
    '.': [],
    '|': [(1, 0), (-1,0)],
    '-': [(0, 1), (0,-1)],
    'F': [(1, 0), (0, 1)],
    '7': [(1, 0), (0,-1)],
    'L': [(-1,0), (0, 1)],
    'J': [(-1,0), (0,-1)]    
}
ADJ = {k: [_(x) for x in v] for k, v in ADJ.items()}
ALL = ADJ['-'] + ADJ['|']

def part1(f):
    # We want to create a dict of each coordinate pair
    arr = f.splitlines()
    arr = {_((i, j)): s for i, line in enumerate(arr)
           for j, s in enumerate(line)}
    s = next(k for k, v in arr.items() if v == 'S')
    s_adj = [dp for dp in ALL if -dp in ADJ[arr.get(s + dp, '.')]]
    arr[s] = next(k for k, v in ADJ.items() if set(v) == set(s_adj))
              
    bfs = deque([(s, 0)])
    dists = {}
    while bfs:
        p, d = bfs.popleft()
        if p not in arr or p in dists:
            continue
        dists[p] = d
        for dp in ADJ[arr[p]]:
            bfs.append((p + dp, d + 1))
    return max(dists.values()), dists, arr, s


def part2(f):
    _, dists, arr, s = part1(f)
    f = [list(s) for s in f.splitlines()]
    f = [''.join(ch if (r,c) in dists else '.'
        for c, ch in enumerate(row)) for r, row in enumerate(f)]
    
    outside = set()
    for r, row in enumerate(f):
        within = False
        up = None
        for c, ch in enumerate(row):
            if (r, c) == s:
                ch = arr[s]
            if ch == '|':
                assert up is None
                within = not within
            elif ch == '-':
                assert up is not None
            elif ch in 'LF':
                assert up is None
                up = ch == 'L'
            elif ch in '7J':
                assert up is not None
                if ch != ('J' if up else '7'):
                    within = not within
                up = None
            elif ch == '.':
                pass
            else:
                raise RuntimeError(f'unexpected character: {ch}')
            if not within:
                outside.add((r,c))

    return (len(f) * len(f[0]) - len(outside | dists.keys()))
            



def main():
    # inputs_1 = open('input').read()
    inputs_2 = open('input').read()
    # print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')


if __name__ == '__main__':
    main()
