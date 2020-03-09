# 3行5列的二维列表
list01 = [
    [0, 1, 2, 3, 4],
    [1, 28, 45, 6, 7],
    [20, 7, 3, 65, 2]
]

# 将第二行元素打印出来
for item in list01[1]:
    print(item, end=' ')

# 将第一列打印出来
print(list01[0][0])
print(list01[1][0])
print(list01[2][0])
for i in range(len(list01)):
    print(list01[i][0])

# 将全部元素打印出来
for i in range(len(list01)):
    for item in list01[i]:
        print(item, end=' ')
    print()
