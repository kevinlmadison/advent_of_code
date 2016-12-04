def part1():
    file = open("aoc2.txt")
    total = 0
    for line in file:
        d = line.strip('\n').split('x')
        sides = []
        sides.append(int(d[0]) * int(d[1]))
        sides.append(int(d[0]) * int(d[2]))
        sides.append(int(d[1]) * int(d[2]))
        smallest = min(sides)
        total += ((sides[0]*2) + (sides[1]*2) + (sides[2]*2) + smallest)
    print("Total sqft: ", total)
part1()

def part2():
    file = open("aoc2.txt")
    total = 0
    for line in file:
        d = line.strip('\n').split('x')
        sm = []
        for i in range(3):
            sm.append(int(d[i]))
        sm.sort()
        total += (sm[0]*2 + sm[1]*2 + sm[0]*sm[1]*sm[2])
    print(total)

part2()
