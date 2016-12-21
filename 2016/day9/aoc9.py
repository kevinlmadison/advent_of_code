import re


def part1(line):
    buffer = ""
    while line:
        marker = re.match(r'(.*?)\((\d+)x(\d+)\)', line)
        if not marker:
            break
        text, num, mult = marker.groups()
        buffer += text
        num, mult = int(num), int(mult)
        add = line[marker.end():marker.end() + num]
        buffer += add * mult
        line = line[marker.end() + num:]
    buffer += line
    return len(buffer.strip())


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        line = next(file).strip()
        print(part1(line))

