def BubbleSort(list_num):
    for a in range(len(list_num) - 1):
        for b in range(len(list_num) - 1):
            if list_num[b] > list_num[b + 1]:
                list_num[b], list_num[b + 1] = list_num[b + 1], list_num[b]
    return list_num

def ShakerSort(list_num):
    left = 0
    right = len(list_num) - 1
    while left <= right:
        for i in range(left, right, 1):
            if list_num[i] > list_num[i + 1]:
                list_num[i], list_num[i + 1] = list_num[i + 1], list_num[i]
        right -= 1
        for i in range(right, left, -1):
            if list_num[i - 1] > list_num[i]:
                list_num[i], list_num[i - 1] = list_num[i - 1], list_num[i]
        left += 1
    return list_num

def GnomeSort(list_num):
    i = 1
    j = 2
    while i < len(list_num):
        if list_num[i - 1] < list_num[i]:
            i = j
            j = j + 1
        else:
            list_num[i - 1], list_num[i] = list_num[i], list_num[i - 1]
            i = i - 1
            if i == 0:
                i = j
                j = j + 1
    return list_num

def MergeSort(list_num):
    if len(list_num) == 1 or len(list_num) == 0:
        return list_num
    L = MergeSort(list_num[:len(list_num) // 2])
    R = MergeSort(list_num[len(list_num) // 2:])
    n, m, k = 0, 0, 0
    C = [0] * (len(L) + len(R))
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(list_num)):
        list_num[i] = C[i]
    return list_num

def SelectSort(list_num):
    for i in range(len(list_num) - 1):
        min_index = i
        for k in range(i + 1, len(list_num)):
            if list_num[k] < list_num[min_index]:
                min_index = k
        list_num[i], list_num[min_index] = list_num[min_index], list_num[i]
    return list_num

def CombSort(list_num):
    n, step = len(list_num), len(list_num)
    while step > 1 or q:
        if step > 1:
            step -= 3
        q, i = False, 0
        while i + step < n:
            if list_num[i] > list_num[i + step]:
                list_num[i], list_num[i + step] = list_num[i + step], list_num[i]
                q = True
            i += step
    return list_num

def BogoSort(list_num):
    print("Вы реально этим воспользовались?")
    print("Пожалуйста подтвердите то, что вы психически здоровы:")
    if input() == True:
        print("Не верю.")
        return False
    else:
        print("Это как-раз всё и объясняет.")
        return None
