def part1():
    file = open("aoc3.txt")
    line = file.read()
    x = 0; y = 0
    visited = []
    for i in line:
        if i == '<':
            x -= 1
        if i == '>':
            x += 1
        if i == 'v':
            y -= 1
        if i == '^':
            y += 1
        t = (x, y)
        if t not in visited:
            visited.append(t)
    print(len(visited))

def part2():
    file = open("aoc3.txt")
    line = file.read()
    x = 0; y = 0; xr = 0; yr = 0
    visited = []
    count = 0
    for i in line:
        if count % 2 == 0:
            if i == '<':
                x -= 1
            if i == '>':
                x += 1
            if i == 'v':
                y -= 1
            if i == '^':
                y += 1
            t = (x, y)
            if t not in visited:
                visited.append(t)
        if count % 2 != 0:
            if i == '<':
                xr -= 1
            if i == '>':
                xr += 1
            if i == 'v':
                yr -= 1
            if i == '^':
                yr += 1
            t = (xr, yr)
            if t not in visited:
                visited.append(t)
        count += 1
    print(len(visited))
part2()
