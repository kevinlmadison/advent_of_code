import re

def part1(inputs):
    total = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for input in inputs:
        for c in input:
            if c in digits:
                total += int(c) * 10
                break
            else:
                continue
        for c in input[::-1]:
            if c in digits:
                total += int(c)
                break
            else:
                continue
    return total
                     
    
def part2(inputs):
    total = 0
    strs = { "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,\
             "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,\
             "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,\
             "7": 7, "8": 8, "9": 9 }
    pattern_f = r'(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)'
    pattern_b = r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9)'
    for input in inputs:
        match_f = re.search(pattern_f, input, re.IGNORECASE)
        match_b = re.search(pattern_b, input[::-1], re.IGNORECASE)
        first, last = strs[match_f.group(0)], strs[match_b.group(0)[::-1]]
        total += (first * 10) + last
    return total

def main():
    inputs_1 = list(open('test_input_1').readlines())
    inputs_2 = list(open('input').readlines())
    print(f'part 1: {part1(inputs_1)}')
    print(f'part 2: {part2(inputs_2)}')

if __name__ == '__main__':
    main()
