def first(nums):
    single = 0
    right = 0
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            single = nums[i]
            right = nums[i + 1]
        print(single, right)


def second(nums):
    left = 0
    right = 1
    unique = 0

    while right < len(nums):
        if nums[left] != nums[right]:
            unique = nums[left]
            right += 1
        else:
            left += 1
            right = left + 1

    print(unique)


def third(nums):
    lst = []
    lst2 = []
    for i in nums:
        if i not in lst:
            lst.append(i)
        elif i in lst:
            lst2.append(i)
    for i in lst:
        if i not in lst2:
            print(i)


nums = [2,2,3,3,4,1,5,8,5,4,8]
third(nums)
