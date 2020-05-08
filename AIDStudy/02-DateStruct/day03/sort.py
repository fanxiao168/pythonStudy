'''
sort.py 排序训练
'''


# 冒泡
def bubble(l):
    n = len(l)
    # 循环 n -1 次，每次确定一个最大值
    for i in range(n - 1):
        # 两两比较交换
        for j in range(n - 1 - i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


l = [4, 5, 7, 1, 2, 9, 6, 8]
bubble(l)
print(l)
