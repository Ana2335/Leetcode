def first(nums):

    cont = nums[0]
    for i in range(len(nums)):
        cont *= nums[i]

    cont2 = int(cont / len(nums))
    for i in range(1, cont + 1):
        if i > 6 and i % cont2 == 0:
            nums.sort()
            temporal = nums[0]
            nums[0] = nums[(i // cont2) - 1]
            nums[(i // cont2) - 1] = temporal


def second(nums):
    total = []
    cont = nums[0]

    for i in range(len(nums)):
        cont *= nums[i]

    cont2 = int(cont / len(nums))

    for i in range(cont2, cont + cont2, cont2):
        nums = nums.copy()
        nums.sort()
        temporal = nums[0]
        nums[0] = nums[(i // cont2) - 1]
        nums[(i // cont2) - 1] = temporal
        total.append(nums)
        print(total)
        for i in range(cont2 - 1):
            if i % 2 == 0:
                temporal = nums[0]


def third(nums):
    m = nums[0]
    for i in range(len(nums)):
        m *= nums[i]
    print(m)

    lst = []
    cont = len(nums)
    a = m
    while cont != 0:
        lst.append(a)
        a //= cont
        cont -= 1

    total = [nums]
    for i in range(1, m):
        nums = nums.copy()
        if i % 6 == 0:
            nums.sort()
            if i % 120 == 0:
                temp = nums[-6]
                nums[-6] = nums[i//120]
                nums[i // 120] = temp
                total.append(nums)

            elif i % 24 == 0:
                temp = nums[-5]
                nums[-5] = nums[(i // 24) + 1]
                nums[(i // 24) + 1] = temp
                total.append(nums)

            else:
                print(i // 6)
                temp = nums[-4]
                nums[-4] = nums[(i // 6) + 2]
                nums[(i // 6) + 2] = temp
                total.append(nums)
        else:
            if i % 2 == 0:
                temp = nums[-3]
                nums[-3] = nums[-1]
                nums[-1] = temp
                total.append(nums)
            else:
                temp = nums[-2]
                nums[-2] = nums[-1]
                nums[-1] = temp
                total.append(nums)


    print(total)
    print(len(total))


def fourth(nums):
    m = nums[0]
    for i in range(len(nums)):
        m *= nums[i]

    lst = []
    cont = len(nums)
    while cont != 0:
        lst.append(m)
        m //= cont
        cont -= 1

    marcapasos = 1
    a = lst[0]
    total = [nums]

    for i in range(1, a):
        if len(lst) > 4 and marcapasos == 120:
            marcapasos = 1
        nums = nums.copy()
        if i % 6 == 0:
            nums.sort()
            for j in range(1, len(lst) - 1):
                if marcapasos % lst[j] == 0 and marcapasos//lst[j] < len(nums):
                    temp = nums[j - 1]
                    nums[j - 1] = nums[marcapasos//lst[j]]
                    nums[marcapasos//lst[j]] = temp
                    total.append(nums)
        else:
            if i % 2 == 0:
                temp = nums[-3]
                nums[-3] = nums[-1]
                nums[-1] = temp
                total.append(nums)
            else:
                temp = nums[-2]
                nums[-2] = nums[-1]
                nums[-1] = temp
                total.append(nums)
        marcapasos += 1
        print(total)

    print(len(total))


nums = [1, 2, 3, 4, 5]
fourth(nums)