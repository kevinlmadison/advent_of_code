import re

def get_neighbors(val: str, row: int, col: int) -> list[str]:
    length = len(val)
    rv = []
    for i in range(row - 1, row + 2):
        for j in range((col - length) - 1, col + 2):
            rv += [(i, j)]
    return rv
          

def part1(inputs: list[str]) -> int:
    total = 0
    max_h = len(inputs)
    max_w= len(inputs[0].strip())    
    num = ''
    nums = {}
    syms = []
    for i, input in enumerate(inputs):
        for j, char in enumerate(input.strip()):
            if char == ".":
                if num != '':
                    neighbors = get_neighbors(num, i, j)
                    nums[num] = neighbors
                    num = ''
                else:
                    continue
            elif char.isdigit():
                num += char
            else:
                syms += [(i, j)]

    for k, vs in nums.items():
        # print(f'key: {k}, val: {vs}')
        # print(f'syms: {syms}')
        for v in vs:
            if v in syms:
                # print(f'adding {k}')
                total += int(k)
                break
    return total
                   
    
def part2(inputs):
    ...

def main():
    inputs_1 = list(open('test_input_1').readlines())
    #inputs_2 = list(open('input').readlines())
    print(f'part 1: {part1(inputs_1)}')
    #print(f'part 2: {part2(inputs_2)}')

if __name__ == '__main__':
    main()
