from functools import reduce

def part1(lengths):
    lengths = [int(x.strip()) for x in lengths]
    nums = list(range(256))
    skip, pos = 0, 0
    for i in lengths:
        '''In order to reverse a section of numbers that might cycle back
        to the front of the list I decided we would just rotate the list
        to eliminate the cycle.
        '''
        nums = nums[pos:] + nums[:pos]
        nums[:i] = reversed(nums[:i])
        nums = nums[-pos:] + nums[:-pos]
        pos = (pos + i + skip) % len(nums)
        skip += 1

    print(str(nums[0] * nums[1]))

def part2(lengths):
    '''Convert the characters, including commas, into ASCII values using
    python's handy ord() built-in function.
    '''
    lengths = [ord(x) for x in lengths]
    lengths.extend([17, 31, 73, 47, 23])
    nums = list(range(256))
    skip, pos = 0, 0
    for _ in range(64):
        for i in lengths:
            nums = nums[pos:] + nums[:pos]
            nums[:i] = reversed(nums[:i])
            nums = nums[-pos:] + nums[:-pos]
            pos = (pos + i + skip) % len(nums)
            skip += 1

    '''Python's functools.reduce was made for exactly this purpose.'''
    dense = []
    for i in range(16):
        dense.append(reduce(lambda x,y: x ^ y, nums[i*16:(i*16)+16]))

    '''Our final value has to be 32 characters long so any hexadecimal value
    of our 16 numbers in the dense hash that is only 1 character long gets 
    padded on the left with one '0'.
    '''
    knot = ''
    for i in dense:
        h = format(i,'x')
        knot += ('0' + h) if len(h) < 2 else h
    print(knot)


def main():
    f1 = open('input.txt').readline().split(',')
    f2 = open('input.txt').readline().strip()
    part1(f1)
    part2(f2)

if __name__ == '__main__':
    main()
