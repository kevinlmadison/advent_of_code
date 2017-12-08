from collections import defaultdict
import operator


def solve(lines):

    ops = {
            '==': operator.eq,
            '!=': operator.ne,
            '>=': operator.ge,
            '<=': operator.le,
            '>': operator.gt,
            '<': operator.lt
            }

    regs = defaultdict(int)
    overall_max = 0

    for line in lines:
        line = line.split()
        if ops[line[5]](int(regs[line[4]]), int(line[6])):
            regs[line[0]] += ((int(line[2])) if line[1] == 'inc' else (-1 * int(line[2])))
        if regs[line[0]] > overall_max:
            overall_max = regs[line[0]]

    print('Part1: {}'.format(max(regs.values())))
    print('Part2: {}'.format(overall_max))


def main():
    f = open('input.txt').readlines()
    solve(f)

if __name__ == '__main__':
    main()
