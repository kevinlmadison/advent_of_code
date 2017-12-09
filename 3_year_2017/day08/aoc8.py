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
        reg, inc, num, iff, regc, op, numc = line.split()
        if ops[op](regs[regc], int(numc)):
            num = int(num)
            inc = inc == 'inc'
            regs[reg] += num if inc else -num
        if regs[reg] > overall_max:
            overall_max = regs[reg]

    print('Part1: {}'.format(max(regs.values())))
    print('Part2: {}'.format(overall_max))


def main():
    f = open('input.txt').readlines()
    solve(f)

if __name__ == '__main__':
    main()
