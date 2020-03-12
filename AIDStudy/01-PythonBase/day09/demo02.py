# 矩阵转换
list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# 5           ---    2
# list01[1][0]   list01[0][1]
# list01[2][0]   list01[0][2]
# list01[3][0]   list01[0][3]

# for i in range(1,4):
#     list01[i][0] list01[0][i]

# list01[2][1]   list01[1][2]
# list01[3][1]   list01[1][3]

# for i in range(2,4):
#     list01[i][1] list01[1][i]

# list01[3][2]   list01[2][3]
# for i in range(3,4):
#     list01[i][2] list01[2][i]

for c in range(1, len(list01)):
    for i in range(c, len(list01)):
        # 交换值
        list01[i][c - 1], list01[c - 1][i] = list01[c - 1][i], list01[i][c - 1]

print(list01)
