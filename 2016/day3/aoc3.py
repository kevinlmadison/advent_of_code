import re
def part1():
    file = open("aoc3.txt")
    possible_triangles = 0
    for line in file:
        sides = re.split('[\D]+',line)
        ts = []
        for i in range(3):
            ts.append(int(sides[i + 1]))
        if  ts[0] + ts[1] > ts[2] and ts[0] + ts[2] > ts[1] and ts[2] + ts[1] > ts[0]:  
            possible_triangles += 1
    print("part 1 possible triangles: ", possible_triangles)

def part2():
    file = open("aoc3.txt")
    possible_triangles = 0
    file_index = 0
    ts = [[], [], []]
    for line in file:
        sides = re.split('[\D]+',line)
        for i in range(3):
            ts[i].append(int(sides[i + 1]))
        file_index += 1 
        if file_index == 3:
            for i in range(3):
                if ts[i][0] + ts[i][1] > ts[i][2] and ts[i][0] + ts[i][2] > ts[i][1] and ts[i][2] + ts[i][1] > ts[i][0]:
                    possible_triangles += 1
            ts = [[], [], []]
            file_index = 0
    print("part 2 possible triangles: ", possible_triangles)

part1()
part2()
