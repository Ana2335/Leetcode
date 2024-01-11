def first(nums):
    lst = []
    for i in nums:
        if i != 0:
            lst.append(i)
    for i in range(nums.count(0)):
        lst.append(0)
    nums = lst
    return nums


def second(nums):
    for i in range(nums.count(0)):
        nums.append(0)
        nums.remove(0)
    return nums


nums = [0, 4, 3, 0, 12]
print(second(nums))