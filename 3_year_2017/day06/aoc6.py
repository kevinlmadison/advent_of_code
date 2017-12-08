import copy

def part1(nums):
    nums = nums.split()
    print(nums)
    seen = set()
    nums = [int(x) for x in nums]
    while True:
        strs = ",".join([str(x) for x in nums])
        print(strs)
        SL = len(seen)
        seen.add(strs)
        if len(seen) == SL:
            print(str(len(seen)))
            break
        max_index = nums.index(max(nums))
        m = nums[max_index]
        nums[max_index] = 0
        i = max_index
        while m > 0:
            i = (i + 1)% len(nums)
            nums[i] += 1
            m -= 1
            

def part2(nums):
    nums = nums.split()
    print(nums)
    seen = set()
    nums = [int(x) for x in nums]
    secondn = copy.copy(nums)
    seconds = set()
    first = ''
    count = 0
    while True:
        strs = ",".join([str(x) for x in nums])
        print(strs)
        SL = len(seen)
        seen.add(strs)
        if len(seen) == SL:
            print(str(len(seen)))
            first = strs
            break
        max_index = nums.index(max(nums))
        m = nums[max_index]
        nums[max_index] = 0
        i = max_index
        while m > 0:
            i = (i + 1)% len(nums)
            nums[i] += 1
            m -= 1
    while True:
        strs = ",".join([str(x) for x in secondn])
        print(strs)
        seconds.add(strs)
        if strs == first:
            print(str(len(seen) - len(seconds) + 1))
            break
        max_index = secondn.index(max(secondn))
        m = secondn[max_index]
        secondn[max_index] = 0
        i = max_index
        while m > 0:
            i = (i + 1)% len(secondn)
            secondn[i] += 1
            m -= 1
        
def main():
    f = open("input.txt").readline()
    
    #part1(f)
    part2(f)
    #part2('0 2 7 0')


if __name__ == '__main__':
    main()
