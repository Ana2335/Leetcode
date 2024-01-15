def first(nums):
    s = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - i - 1):
            for k in range(j + 1, len(nums) - i):
                lst = []
                if (nums[i] + nums[j] + nums[k]) == 0:
                    lst.append(nums[i])
                    lst.append(nums[j])
                    lst.append(nums[k])
                    if len(s) == 0:
                        s.append(lst)
                    else:
                        for l in s:
                            s.append(lst)
                            if (nums[i] in l) and (nums[j] in l) and (nums[k] in l):
                                s.remove(lst)
                                break
    return s


def second(nums):
    nums.sort()
    s = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                lst = []
                if (nums[i] + nums[j] + nums[k]) == 0:
                    lst.append(nums[i])
                    lst.append(nums[j])
                    lst.append(nums[k])
                    if lst not in s:
                        s.append(lst)
    return s


def third(nums):
    s = []
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            a = - nums[i] - nums[j]
            if a in nums[j + 1:]:
                lst = [nums[i], nums[j], a]
                lst.sort()
                if lst not in s:
                    s.append(lst)
    return s


nums = [-1, 0, 1, 2, -1, -4]
print(third(nums))