def part1():
    file = open("aoc5.txt")
    nice = 0
    vowels = 'aeiou'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for line in file:
        print(line)
        nice_count = 0
        if 'ab' not in line and 'cd' not in line and 'pq' not in line and 'xy' not in line:
            nice_count += 1
            vowel_count = 0
            for i in range(5):
                if vowels[i] in line:
                    vowel_count += 1
            if vowel_count >= 3:
                for i in range(26):
                    if alpha[i]+alpha[i] in line:
                        nice += 1
    print(nice)

part1()
