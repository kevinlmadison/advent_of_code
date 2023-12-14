import re
import math


def part1(f):
    steps, *maps = f.split('\n\n')

    maps = {m[0]: (m[1], m[2]) for m in
            [re.findall(r'[A-Z]+', n) for n in maps[0].strip().split('\n')]}

    def cycle():
        i = 0
        while True:
            if i >= len(steps):
                i = 0
            else:
                if steps[i] == 'L':
                    yield 0
                else:
                    yield 1
                i += 1

    start, stop, count = 'AAA', 'ZZZ', 0
    for i in cycle():
        start = maps[start][i]
        count += 1
        if start == stop:
            break
    return count


def part2(f):
    steps, *maps = f.split('\n\n')

    maps = {m[0]: (m[1], m[2]) for m in
            [re.findall(r'[A-Z0-9]+', n) for n in maps[0].strip().split('\n')]}

    def cycle():
        i = 0
        while True:
            if i >= len(steps):
                i = 0
            else:
                if steps[i] == 'L':
                    yield 0
                else:
                    yield 1
                i += 1

    count = 0
    start = [x for x in maps.keys() if x[2] == 'A']
    multi = []
    # z = [x for x in maps.keys() if x[2] == 'Z']
    # print(z)
    for s in start:
        j = s
        for i in cycle():
            j = maps[j][i]
            count += 1
            if j[2] == 'Z':
                multi.append(count)
                count = 0
                break
            
    return math.lcm(*multi)


def main():
    # inputs_1 = open('input').read()
    inputs_2 = open('input').read()
    # print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')


if __name__ == '__main__':
    main()
