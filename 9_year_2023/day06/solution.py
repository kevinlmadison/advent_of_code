import re
def part1(inputs: list[str]) -> int:
    time = list(map(int, re.findall(r'\d+', inputs[0])))
    dist = list(map(int, re.findall(r'\d+', inputs[1])))
    rv = 1
    for i in range(len(time)):
        pos, pre  = 0, 0
        while pre < time[i]:
            if pre * (time[i] - pre) > dist[i]:
                pos += 1
            pre += 1
        rv *= pos
    return rv

    
def part2(inputs):
    time = int("".join(re.findall(r'\d+', inputs[0])))
    dist = int("".join(re.findall(r'\d+', inputs[1])))
    pos, pre = 0, 0
    while pre < time:
        if pre * (time - pre) > dist:
            pos += 1
        pre += 1
    return pos
    ...

def main():
    # inputs_1 = list(open('input').readlines())
    inputs_2 = list(open('input').readlines())
    # print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')

if __name__ == '__main__':
    main()
