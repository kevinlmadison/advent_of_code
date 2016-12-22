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
    return len(buffer)

def part2(line):
    buffer = 0
    while line:
        marker = re.match(r'(.*?)\((\d+)x(\d+)\)', line)
        if not marker:
            break
        text, num, mult = marker.groups()
        buffer += len(text)
        num, mult = int(num), int(mult)
        add = part2(line[marker.end():marker.end() + num])
        buffer += add * mult
        line = line[marker.end() + num:]
    buffer += len(line)
    return buffer

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        line = next(file).strip()
        print(part1(line))
        print(part2(line))

