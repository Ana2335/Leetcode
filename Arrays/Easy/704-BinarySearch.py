def first(nums, target):
    l = 0
    r = len(nums) - 1
    m = (l + r) // 2
    if nums[0] > target or nums[len(nums) - 1] < target:
        return -1
    else:
        while target != nums[m]:
            if r < l:
                return -1
            if nums[m] > target:
                r = m - 1
                m = (l + r) // 2
            elif nums[m] < target:
                l = m + 1
                m = (l + r) // 2
        return m


def second(nums, target):
    l = 0
    r = len(nums) - 1
    m = (l + r) // 2
    if target in nums:
        while target != nums[m]:
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            m = (l + r) // 2
        return m
    return -1


nums = [-1,0,3,5,9,12]
target = 0
print(second(nums, target))