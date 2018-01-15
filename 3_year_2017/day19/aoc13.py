from collections import *
from functools import reduce
import itertools
from string import ascii_uppercase as uc

def solve(lines):
    grid = []
    letters = []
    d = [(1,0), (0,-1), (-1,0), (0,1)]
    for line in lines:
        grid.append([c for c in line.strip()])
    start = grid[1].index('|')
    print(grid[1][98])
    print('start {}'.format(start))
    i, j = 1, start
    while True:
    #for _ in range(10):
        ki, kj = d[0]
        if grid[i][j] == '-' or grid[i][j] == '|' or grid[i][j] in uc:
            if grid[i][j] in uc:
                letters.append(grid[i][j])
            i += ki
            j += kj
        elif grid[i][j] == '+':
            ti, tj = d[1]
            if grid[i+ti][j+tj] != ' ':
                d = d[1:] + d[:1]
            else:
                d = d[-1:] + d[:-1]
            ki, kj = d[0]
            i += ki
            j += kj
        print(letters)


def main():
    f = open('input.txt').readlines()
    solve(f)

if __name__ == '__main__':
    main()
