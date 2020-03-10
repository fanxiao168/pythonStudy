# 将homework改为函数
# 定义矩阵转置函数
list01 = [
    [0, 1, 2, 3, 4],
    [1, 28, 45, 6, 7],
    [20, 7, 3, 65, 2]
]


def transpose(list):
    result = []
    for c in range(len(list[0])):
        result.append([])
        for r in range(len(list)):
            result[c].append(list[r][c])
    return result


print(transpose(list01))
