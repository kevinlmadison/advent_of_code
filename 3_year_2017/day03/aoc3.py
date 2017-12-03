def rotate(A):
    return A[1:] + A[:1]

def part1(n):
    s = [(0,0,1)]
    x, y = 0, 0
    i = 2
    j = 1
    while i <= n:
        for _ in range(j):
            if i > n:
                break
            if j%2 == 0:
                x -= 1
            else:
                x += 1
            s.append((x,y,i))
            i += 1
        for _ in range(j):
            if i > n:
                break
            if j%2 == 0:
                y -= 1
            else:
                y += 1
            s.append((x,y,i))
            i += 1
        j += 1
    print(s[-1])

def part2(n):
    s = {(0,0):1}
    x, y = 0, 0
    i = 2
    j = 1
    while i <= n:
        for _ in range(j):
            if i > n:
                print(str(i))
                break
            if j%2 == 0:
                x -= 1
            else:
                x += 1
            i = 0
            for q in range(-1, 2):
                for v in range(-1, 2):
                    if (x+q,y+v) in s:
                        i += s[(x+q,y+v)]
            s[(x,y)] = i
        for _ in range(j):
            if i > n:
                print(str(i))
                break
            if j%2 == 0:
                y -= 1
            else:
                y += 1
            i = 0
            for q in range(-1, 2):
                for v in range(-1, 2):
                    if (x+q,y+v) in s:
                        i += s[(x+q,y+v)]
            s[(x,y)] = i
        j += 1

def main():
    part1(368078)
    part2(368078)


if __name__ == '__main__':
    main()
