import re


def part1(rows):
    sum = 0
    for line in rows:
        sum += max(line) - min(line)
    print(str(sum))


def part2(rows):
    sum = 0
    for line in rows:
        line = [x//y for x in line for y in line if (x != y and x%y == 0)]
        sum += line[0]
    print(str(sum))


def main():
    f = open('input.txt')
    rows = []
    for line in f:
        rows.append([int(x) for x in line.split()])
    part1(rows)
    part2(rows)


if __name__ == '__main__':
    main()
