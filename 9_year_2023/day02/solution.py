import re

MAX_RED   = 12
MAX_GREEN = 13
MAX_BLUE  = 14

def part1(inputs):
    total = 0
    for index, input in enumerate(inputs):
        input = input.split(' ')[2:]
        impossible = False
        for i in range(0, len(input), 2):
            if impossible:
                break
            if input[i + 1].startswith('red'):
                if int(input[i]) > MAX_RED:
                    impossible = True
                    break
            if input[i + 1].startswith('green'):
                if int(input[i]) > MAX_GREEN:
                    impossible = True
                    break
            if input[i + 1].startswith('blue'):
                if int(input[i]) > MAX_BLUE:
                    impossible = True
                    break
        if not impossible:
            total += (index + 1)
    return total
    
def part2(inputs):
    total = 0
    for index, input in enumerate(inputs):
        input = input.split(' ')[2:]
        min_red, min_green, min_blue = 0, 0, 0
        for i in range(0, len(input), 2):
            if input[i + 1].startswith('red'):
                if int(input[i]) > min_red:
                    min_red = int(input[i])
            if input[i + 1].startswith('green'):
                if int(input[i]) > min_green:
                    min_green = int(input[i])
            if input[i + 1].startswith('blue'):
                if int(input[i]) > min_blue:
                    min_blue = int(input[i])
        total += (min_red * min_green * min_blue)
    return total

def main():
    inputs_1 = list(open('input').readlines())
    inputs_2 = list(open('input').readlines())
    print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')

if __name__ == '__main__':
    main()
