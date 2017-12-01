
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

grid = []
for i in range(51):
    grid.append(['.' for _ in range(51)])

for i in range(51):
    for j in range(51):
        q = i*i + 3*i + 2*i*j + j + j*j
        q += 1352
        if bin(q).count("1") % 2 != 0:
            grid[i][j] = '#'

graph = dict()
for r in range(51):
    for c in range(51):
        if grid[r][c] != '#':
            graph[(r,c)] = set()
            if (r+1) < 51:
                if grid[r+1][c] != '#':
                    graph[(r,c)].add((r+1,c))
            if (r-1) >= 0:
                if grid[r-1][c] != '#':
                    graph[(r,c)].add((r-1,c))
            if (c+1) < 51:
                if grid[r][c+1] != '#':
                    graph[(r,c)].add((r,c+1))
            if (c-1) >= 0:
                if grid[r][c-1] != '#':
                    graph[(r,c)].add((r,c-1))
start = (1, 1)
paths = []
for i in range(51):
    for j in range(51):
        if grid[i][j] == '.':
            sp = shortest_path(graph, start, (i, j))
            if sp is not None:
                if (len(sp) - 1) <= 50:
                    paths.append(sp)

print(len(paths))
