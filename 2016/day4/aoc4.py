def dec_sorted(list):
    for i in range(len(list) - 1):
        if list[i] < list[i+1]:
            return False
    return True
def alphabetical(list):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(list) - 1):
        if alpha.index(list[i]) > alpha.index(list[i+1]):
            return False
    return True
def count_cpr(a, b):
    count_b = []
    max_b = []
    for i in range(len(b)):
        count_b.append(b.count(b[i]))
    for i in range(5):
        max_b.append(max(count_b))
        count_b.pop(max(count_b))
    if a == max_b:
        return True
    return False

def part1():
    file = open("aoc4.txt")
    lines = 0
    nice = 0
    for line in file:
        key = []
        str = []
        fixed = []
        lines += 1
        for i in range(5):
            key.append(line[-7 + i])
        for i in range(len(line[:-12])):
            if line[i] != '-':
                str.append(line[i])
        for i in range(len(str)):
            arr = []
            if str[i] not in arr:
                arr.insert(str.count(str[i]),(str.count(str[i]), str[i]))
            if len(arr) > 0:
                fixed.append(arr)
            nice += int(line[-11:-8])
        print(str, "end of str")
        print(key, "end of key")
        print(fixed, "end of fixed")
    print(nice)

        
            
    print(nice)



part1()

def part2():
    file = open("aoc4.txt")

part2()
