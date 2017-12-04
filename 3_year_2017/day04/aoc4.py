def part1(f):
    valid = 0
    for line in f:
        line = line.split()
        s = []
        val = True
        for word in line:
            if word in s:
                val = False
                break
            else:
                s.append(word)
        if val:
            valid += 1
    print(valid)

def part2(f):
    valid = 0
    for line in f:
        valid += 1
        line = line.split()
        val = True
        for j,word1 in enumerate(line):
            for i,word2 in enumerate(line):
                if j != i and anagramSolution1(word1, word2) == True and len(word1) == len(word2):
                    valid -= 1
                    print('{} {}: count = {}'.format(word1, word2, valid))
                    val = False
                    break
            if val == False:
                break
    print(str(valid))

def anagramSolution1(s1,s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK   

def main():
    f = open('input.txt')
    #part1(f)
    part2(f)

if __name__ == '__main__':
    main()
