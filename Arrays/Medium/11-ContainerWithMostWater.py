def first(height):
    l = height[0]
    r = height[-1]
    a = height.index(r) - height.index(l)
    cap = 0
    while height.index(r) > height.index(l):
        if r > l:
            if a * r > cap:
                cap = a * r
            l = height[height.index(l) + 1]
            a = height.index(r) - height.index(l)
        elif l > r:
            if a * l > cap:
                cap = a * l
            r = height[height.index(l) - 1]
            a = height.index(r) - height.index(l)
        else:
            if a * r > cap:
                cap = a * r
            if height[height.index(r) - 1] > height[height.index(l) + 1]:
                l = height[height.index(l) + 1]
            else:
                r = height[height.index(r) - 1]
            a = height.index(r) - height.index(l)
    return cap


def second(height):
    l = height[0]
    r = height[-1]
    il = 0
    ir = len(height) - 1
    a = ir - il
    cap = 0
    while ir > il:
        if r > l:
            if a * l > cap:
                cap = a * l
            il += 1
            l = height[il]
            a = ir - il
        elif l > r:
            if a * r > cap:
                cap = a * r
            ir -= 1
            r = height[ir]
            a = ir - il
        else:
            if a * r > cap:
                cap = a * r
            if height[ir - 1] > height[il + 1]:
                il += 1
                l = height[il]
            else:
                ir -= 1
                r = height[ir]
            a = ir - il
    return cap


def third(height):
    l = height[0]
    r = height[-1]
    il = 0
    ir = len(height) - 1
    a = ir - il
    cap = 0
    while ir > il:
        if l > r:
            if a * r > cap:
                cap = a * r
            ir -= 1
            r = height[ir]
            a = ir - il
        else:
            if a * l > cap:
                cap = a * l
            il += 1
            l = height[il]
            a = ir - il
    return cap


def fourth(height):
    l = 0
    r = len(height) - 1
    cap = 0
    while r > l:
        if height[l] > height[r]:
            if (r - l) * height[r] > cap:
                cap = (r - l) * height[r]
            r -= 1
        else:
            if (r - l) * height[l] > cap:
                cap = (r - l) * height[l]
            l += 1
    return cap


height = [1,1]
print(fourth(height))
