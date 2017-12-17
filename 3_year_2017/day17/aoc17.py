from collections import *
from functools import reduce
import itertools

'''Part 1 was pretty straight forward but it did actually create the full
list as it went unlike part 2 where we're just doing raw calculations.
'''

def solve(s):
    i = 0
    val = 0
    for j in range(1,50000001):
        i = (i + s) % j 
        if i == 0:
            val = j
        i += 1
    print('part 2: {}'.format(val))

def main():
    f = 376
    solve(f)

if __name__ == '__main__':
    main()
