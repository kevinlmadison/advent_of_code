import re
from multiprocessing import Process, Queue

def part1(inputs: list[str]) -> int:
    seeds = [[] for _ in range(8)]
    cat = 0
    for line in inputs:
        m = re.findall(r'\d+', line)
        if line.startswith('\n'):
            cat += 1
        if len(m) > 0:
            seeds[cat] += [m]

    locs = []
    for seed in seeds[0]:
        seed = list(map(int, seed))
        for s in seed:
            for instrs in seeds[1:]:
                for instr in instrs:
                    instr = list(map(int, instr))
                    if (instr[1]) <= s <= (instr[1] + instr[2]):
                        s = instr[0] + (s - instr[1])
                        break
            locs += [s]

    return min(locs)
    
def part2(inputs):
    seeds = [[] for _ in range(8)]
    cat = 0
    for line in inputs:
        m = re.findall(r'\d+', line)
        if line.startswith('\n'):
            cat += 1
        if len(m) > 0:
            seeds[cat] += [m]

    seed = list(map(int, seeds[0][0]))
    seed_ranges = []
    for x in range(0, len(seed), 2):
        seed_ranges.append((seed[x], seed[x] + seed[x + 1]))
    print(seed_ranges)

    for i in range(10000000000):
        rv = i
        for instrs in seeds[:0:-1]:
            for instr in instrs:
                instr = list(map(int, instr))
                if (instr[0]) <= i <= (instr[0] + instr[2]):
                    i = instr[1] + (i - instr[0])
                    break
        for (x, y) in seed_ranges:
            if x <= i <= y:
                return rv
######## I DIDN'T WRITE THIS, IT'S TO LEARN FROM ###############
def pairs(l):
    it = iter(l)
    return zip(it, it)

def p2(f):
    seeds, *mappings = f.read().split("\n\n")
    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]
    seeds = [range(a, a + b) for a, b in pairs(seeds)]

    for m in mappings:
        _, *ranges = m.splitlines()
        ranges = [[int(x) for x in r.split()] for r in ranges]
        ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]
        new_seeds = []

        for r in seeds:
            for tr, fr in ranges:
                offset = tr.start - fr.start
                if r.stop <= fr.start or fr.stop <= r.start:
                    continue
                ir = range(max(r.start, fr.start), min(r.stop, fr.stop))
                lr = range(r.start, ir.start)
                rr = range(ir.stop, r.stop)
                if lr:
                    seeds.append(lr)
                if rr:
                    seeds.append(rr)
                new_seeds.append(range(ir.start + offset, ir.stop + offset))
                break
            else:
                new_seeds.append(r)

        seeds = new_seeds

    return min(x.start for x in seeds)
######## I DIDN'T WRITE THIS, IT'S TO LEARN FROM ###############

def main():
    # inputs_1 = list(open('input').readlines())
    # inputs_2 = list(open('input').readlines())
    # print(f'part 1: {part1(inputs_1)}')
    # print(f'part 2: {part2(inputs_2)}')
    f = open('input')
    print(f'test p2: {p2(f)}')

if __name__ == '__main__':
    main()
