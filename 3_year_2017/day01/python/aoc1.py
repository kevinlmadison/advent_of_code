def part1(nums):
    sum = 0
    if nums[-1] == nums[0]:
        sum += nums[-1]
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            sum += nums[i]

    print(str(sum))

def part2(nums):
    j = len(nums) // 2
    a = nums[:j]
    b = nums[j:]
    sum = 0
    for i in range(j):
        if a[i] == b[i]:
            sum += (2 * a[i])

    print(str(sum))


def main():
    f = open('input.txt')
    nums = list(f.read().strip())
    nums = [int(x) for x in nums]
    part1(nums)
    part2(nums)

if __name__ == '__main__':
    main()
