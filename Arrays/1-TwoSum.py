def first(nums):
    cont = 1
    discount = -1

    for i in range(len(nums) + discount):
        for j in range(len(nums) - 2):
            return nums[i] + nums[i + cont]


def second(nums, target):
    discount = -1

    for i in range(len(nums) + discount):
        for j in range(len(nums) + discount - 1):
            if (nums[i] + nums[j + 1]) == target:
                return [i, (j + 1)]
            discount -= 1


def third(nums, target):
    discount = -1
    count = 0

    for i in range(len(nums) + discount):
        cont = 1
        while (cont + count) < len(nums):
            if (nums[count] + nums[count + cont]) == target:
                lista = [count, count + cont]
                return lista
            cont += 1
        discount -= 1
        count += 1


nums = [1, 2, 3, 8, 7]
target = 8
print(third(nums, target))
