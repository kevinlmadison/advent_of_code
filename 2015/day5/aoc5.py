def part1():
    file = open("aoc5.txt")
    nice = 0
    vowels = 'aeiou'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for line in file:
        if 'ab' in line: 
            continue
        if 'cd' in line: 
            continue
        if 'pq' in line:
            continue 
        if 'xy' in line:
            continue
        vowel_count = 0
        for i in range(5):
            if vowels[i] in line:
                vowel_count += line.count(vowels[i])
        if vowel_count >= 3:
            for i in range(26):
                if alpha[i]+alpha[i] in line:
                    nice += 1
                    break
                    print(line,alpha[i]+alpha[i], vowel_count, nice)
    print(nice)

part1()
def part2():
    file = open("aoc5.txt")
    nice = 0
    linecount = 0
    for line in file:
        l_nice = 0
        for i in range(len(line) - 1):
            if line.count(line[i]+line[i+1]) >= 2 and not (line[i] == line[i+1] and line[i+1] == line[i+2]):
                    l_nice = 1
        if l_nice == 1:
            for i in range(len(line) - 2):
                if line[i] == line[i+2]:
                    l_nice = 2
        linecount += 1
        if l_nice == 2:
            nice += 1
    print(nice)
    print(linecount)
part2()
            
                

