import copy

def part1(nums):
    q = len(nums)
    steps = 1
    i = 0
    while i + nums[i] >= 0 and i + nums[i] < q:
        temp = i
        i += nums[i]
        nums[temp] += 1
        steps += 1
    print(steps)


def part2(nums):
    q = len(nums)
    steps = 1
    i = 0
    while i + nums[i] >= 0 and i + nums[i] < q:
        temp = i
        i += nums[i]
        if nums[temp] >= 3:
            nums[temp] -= 1
        else:
            nums[temp] += 1
        steps += 1
    print(steps)

def main():
    f = open('input.txt')
    nums = []
    for line in f:
        nums.append(int(line))
    nums2 = copy.copy(nums)
    part1(nums)
    part2(nums2)

if __name__ == '__main__':
    main()
