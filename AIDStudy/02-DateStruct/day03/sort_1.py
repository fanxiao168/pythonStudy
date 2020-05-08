'''
快速排序算法
'''


def sub_sort(l, low, high):
    x = l[low]  # 基准
    while low < high:
        # 如果后边的数比x大high向前走
        while l[high] > x and high > low:
            high -= 1
        l[low] = l[high]  # 比x小的往前甩
        # 如果前面的数比x小则low往后走
        while l[low] <= x and low < high:
            low += 1
        l[high] = l[low]  # 比x大的往后甩
    l[low] = x  # 将x插入最终位置
    return low  # 每一轮最终基数确定的位置


# low : 每一个元素索引号，high:最后一个元素索引号


'''
该写法表示希望low传入一个整形，high传入一个整形，返回值为None类型
但是没有强制要求必须这样做
'''


def quick(l: list, low: int, high: int) -> None:
    if low < high:
        key = sub_sort(l, low, high)
        quick(l, low, key - 1)
        quick(l, key + 1, high)


l = [8, 1, 12, 7, 6, 10, 3, 4, 8, 5, 9, 2, 11, 5, 13]
quick(l, 0, len(l) - 1)
print(l)
