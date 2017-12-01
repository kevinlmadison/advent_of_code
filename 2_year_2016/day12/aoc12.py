# part 1


def reggies(file):
    reg = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    inst = []
    for line in file:
        inst.append(line)
    end = len(inst)
    i = 0
    print(inst[i].strip().split(' '))
    while i < end:
        move = inst[i].strip().split(' ')
        print(move)
        if move[0] == 'cpy':
            if move[1] not in 'abcd':
                reg[move[2]] = int(move[1])
            else:
                reg[move[2]] = reg[move[1]]
            i += 1
        if move[0] == 'inc':
            reg[move[1]] += 1
            i += 1
        if move[0] == 'dec':
            reg[move[1]] -= 1
            i += 1
        if move[0] == 'jnz':
            if move[1] not in 'abcd':
                if int(move[1]) != 0:
                    i += int(move[2])
                else:
                    i += 1
            elif reg[move[1]] != 0:
                i += int(move[2])
            else: 
                i += 1
        print(reg)
    return reg

def main():
    f = open('input.txt')
    a = reggies(f)
    print(a)

if __name__ == '__main__':
    main()

