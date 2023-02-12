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
