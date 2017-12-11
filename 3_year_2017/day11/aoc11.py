def solve(steps):
    stop = {'x':0,'y':0}
    x, y = 'x', 'y'
    highest = 0
    for i in steps:
        if i == 'n':
            stop[y] -=1
        if i == 'nw':
            if stop[x] % 2 == 0:
                stop[y] -=1
            stop[x] -=1
        if i == 'ne':
            if stop[x] % 2 == 0:
                stop[y] -=1
            stop[x] += 1
        if i == 's':
            stop[y] +=1
        if i == 'sw':
            if stop[x] % 2 != 0:
                stop[y] +=1
            stop[x] -=1
        if i == 'se':
            if stop[x] % 2 != 0:
                stop[y] +=1
            stop[x] +=1
        dist = stop[x] + (abs(stop[y]) - ((stop[x] // 2) + (0 if stop[x] % 2 == 0 else 1)))
        if dist > highest:
            highest = dist

    print("part 1: {}".format(dist))
    print("part 2: {}".format(highest))

#  Quick and dirty for now.

def main():
    f = open('input.txt').readline().rstrip().split(',')
    solve(f)

if __name__ == '__main__':
    main()
