from collections import *
from functools import *
import itertools
import sys


def knot_hash(s):

    s = [ord(x) for x in s]
    s.extend([17, 31, 73, 47, 23])
    nums = list(range(256))
    skip, pos = 0, 0
    for _ in range(64):
        for i in s:
            nums = nums[pos:] + nums[:pos]
            nums[:i] = reversed(nums[:i])
            nums = nums[-pos:] + nums[:-pos]
            pos = (pos + i + skip) % len(nums)
            skip += 1
            
    dense = [reduce(lambda x,y: x ^ y, nums[i*16:(i*16)+16]) for i in range(16)]
    return ''.join([('0' + format(h,'x') if len(format(h,'x')) < 2 else format(h,'x')) for h in dense])

def count_bits(num):
    num_bits = 0
    while num:
        num_bits += num & 1
        num >>= 1
    return num_bits



def solve(seed):

    def bit_grid(sd):
        bits = ['{:0128b}'.format(int(knot_hash(sd + str(i)),16)) for i in range(128)]
        return [list(map(int,b)) for b in bits]

    grid = bit_grid(seed)
    print('part 1: {}'.format(sum(sum(i for i in g) for g in grid)))

    # Found this function on the advent of code subreddit
    # I had the same algorithm in mind but much less elegant.
    visited = set()
    islands = 0
    def flood_dfs(i, j):
        if(i, j) in visited:
            return
        if not grid[i][j]:
            return
        visited.add((i, j))
        if i > 0:
            flood_dfs(i-1, j)
        if j > 0:
            flood_dfs(i, j-1)
        if i < 127:
            flood_dfs(i+1, j)
        if j < 127:
            flood_dfs(i, j+1)

    for i in range(128):
        for j in range(128):
            if (i, j) in visited:
                continue
            if not grid[i][j]:
                continue
            islands += 1
            flood_dfs(i, j)

    print('part 2: {}'.format(islands))

def main():
    seed = 'hfdlxzhv-'
    solve(seed)

if __name__ == '__main__':
    main()
