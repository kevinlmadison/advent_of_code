from collections import Counter
from functools import cmp_to_key


def cmp(ha: str, hb: str) -> int:
    c = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    p = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1),
         (3, 1, 1), (3, 2), (4, 1), (5, )]
    ca, cb = list(Counter(ha).values()), list(Counter(hb).values())
    ca.sort(reverse=True), cb.sort(reverse=True)
    ca, cb = tuple(ca), tuple(cb)
    if ca == cb:
        for i in range(5):
            if c.index(ha[i]) > c.index(hb[i]):
                return 1
            elif c.index(ha[i]) < c.index(hb[i]):
                return -1
        return 0
    else:
        if p.index(ca) > p.index(cb):
            return 1
        elif p.index(ca) < p.index(cb):
            return -1
    return 0

def sort_hand(a: str, b: str) -> int:
    c = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    if c.index(a) > c.index(b):
        return 1
    elif c.index(a) < c.index(b):
        return -1
    else:
        return 0


def replace_j(s: str, c: str):
    return "".join([c if x == 'J' else x for x in s])


def get_w(ca):
    fa = {k: v for k, v in ca.items() if k != 'J'}
    if fa:
        return max(fa, key=fa.get)
    else:
        return 'J'


def cmp2(ha: str, hb: str) -> int:
    c = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    p = [(1, 1, 1, 1, 1), (2, 1, 1, 1), (2, 2, 1),
         (3, 1, 1), (3, 2), (4, 1), (5, )]
    ca, cb = Counter(ha), Counter(hb)
    ka, kb = get_w(ca), get_w(cb)
    na, nb = replace_j(ha, ka), replace_j(hb, kb)
    ca, cb = Counter(na), Counter(nb)
    va, vb = list(ca.values()), list(cb.values())
    va.sort(reverse=True), vb.sort(reverse=True)
    va, vb = tuple(va), tuple(vb)

    # print(f'va: {va}, vb: {vb}')
    # print(f'na: {na}, nb: {nb}')
    
    if p.index(va) > p.index(vb):
        return 1
    elif p.index(va) < p.index(vb):
        return -1
        
    else:
        if va == vb:
            for i in range(5):
                if c.index(ha[i]) > c.index(hb[i]):
                    return 1
                elif c.index(ha[i]) < c.index(hb[i]):
                    return -1
            return 0
    return 0


def part1(inputs: list[str]) -> int:
    inputs = [x.split(' ') for x in inputs]
    inputs = {x[0]: int(x[1]) for x in inputs}
    sorted_inputs = sorted(inputs, key=cmp_to_key(cmp))
    return sum([(i + 1) * inputs[c] for i, c in enumerate(sorted_inputs)])


def part2(inputs):
    inputs = [x.split(' ') for x in inputs]
    inputs = {x[0]: int(x[1]) for x in inputs}
    sorted_inputs = sorted(inputs.keys(), key=cmp_to_key(cmp2))
    return sum([(i + 1) * inputs[c] for i, c in enumerate(sorted_inputs)])


def main():
    # inputs_1 = list(open('input').readlines())
    inputs_2 = list(open('input').readlines())
    # print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')


if __name__ == '__main__':
    main()
