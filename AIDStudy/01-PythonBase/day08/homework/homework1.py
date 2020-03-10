list01 = [
    [0,1,2,3,4],
    [1,28,45,6,7],
    [20,7,3,65,2]
]

# 根据list01 生成list02
# 要求list02中的每一行是list01中的每一列
# list02 = [
#     [0,1,20],
#     [1,28,7],
#     ...
# ]

list02 = []
# 获取list01中的第一列 形成列表 放入list02中
# list01[0][0]    0
# list01[1][0]    1
# list01[2][0]    20

line = []
for r in range(len(list01)):
    line.append(list01[r][0])
list02.append(line)
print(list02)

# list01[0][1]    1
# list01[1][1]    28
# list01[2][1]    7
line = []
for r in range(len(list01)):
    line.append(list01[r][1])
list02.append(line)
print(list02)

# list01[0][2]    1
# list01[1][2]    28
# list01[2][2]    7
line = []
for r in range(len(list01)):
    line.append(list01[r][2])
list02.append(line)
print(list02)

list02 = []
for c in range(len(list01[0])):
    line = []
    for r in range(len(list01)):
        line.append(list01[r][c])
    list02.append(line)
print(list02)

list02 = []
for c in range(len(list01[0])):
    list02.append([])
    for r in range(len(list01)):
        list02[c].append(list01[r][c])
print(list02)



