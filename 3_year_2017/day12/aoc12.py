from collections import defaultdict, deque

def solve(lines):

    d = defaultdict(list)

    for line in lines:
        d[int(line[0])] = [int(x) for x in line[2:]]

    '''Part 1 of this challenge can be solved using breadth or depth first
    search and starting at node 0.
    '''

    def bfs(seed):
        v = list()
        q, count = deque([seed]), 0
        while q:
            x = q.popleft()
            v.append(x)
            count += 1
            for i in d[x]:
                if i not in v:
                    q.append(i) 
        return v

    '''Since the input adjacency list represents an undirected graph we know 
    that any one node can only belong to one group, so we only perform additional
    best first searches starting from nodes we have not yet visited.
    '''

    visited = list()
    groups = 0

    for i in range(len(lines)):
        if i not in visited:
            visited.extend(bfs(i))
            groups += 1
        if i == 0:
            print('part 1: {}'.format(len(visited)))
    print('part 2: {}'.format(groups))

def main():
    f = open('input.txt').readlines()
    f = [x.replace(',','').split() for x in f]  # No need for regex yet again.
    solve(f)

if __name__ == '__main__':
    main()
