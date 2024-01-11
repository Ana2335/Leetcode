def first(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    else:
        for i in range(n - 1):
            cont = 0
            for j in range(i + 1, n - 2):
                if nums[i] == nums[j]:
                    cont += 1
            if cont > n // 2:
                return nums[i]


def second(nums):
    lst = []
    if len(nums) == 1:
        return nums[0]
    else:
        for i in nums:
            if i not in lst:
                lst.append(i)
        for i in lst:
            if nums.count(i) > (len(nums) // 2):
                return i


def third(nums):
    lst = []
    for i in nums:
        if i not in lst:
            lst.append(i)
    for i in lst:
        if nums.count(i) > (len(nums) // 2):
            return i


def fourth(nums):
    for i in set(nums):
        if nums.count(i) > (len(nums) // 2):
            return i


nums = [2,2,1,1,1,2,2]
print(fourth(nums))