def first(nums, target):
    cont = 0

    if target not in nums:
        for i in range(len(nums) - 1):
            if (nums[i] < target) and (target < nums[i + 1]):
                return i + 1
        return len(nums)
    else:
        for i in nums:
            if i == target:
                return cont
            else:
                cont += 1


def second(nums, target):
    if target not in nums:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums) - 1):
                if nums[i] < target < nums[i + 1]:
                    return i + 1
    else:
        for i in range(len(nums)):
            if nums[i] == target:
                return i


def third(nums, target):
    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    else:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        for i in range(len(nums) - 1):
            if (nums[i] < target) and (target < nums[i + 1]):
                return i + 1


def fourth(nums, target):
    if target < nums[0]:
        return 0
    elif target > nums[-1]:
        return len(nums)
    else:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target < nums[i + 1]:
                return i + 1


nums = [1, 3, 5, 6]
target = 7
print(fourth(nums, target))
