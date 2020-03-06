# 生成1～10的数字 将数字的平方放入list01
list01 = []
for i in range(1,11):
    list01.append(i**2)
print(list01)

list01 = [i**2 for i in range(1,11)]
print(list01)

# 将list01中所有的奇数放入list02
list02 = []
for item in list01:
    if item % 2:
        list02.append(item)
print(list02)
list02 = [item**2 for item in range(1,11) if item % 2]
print(list02)

# 将list01中所有的偶数加10放入list03
list03 = []
for item in list01:
    if item % 2 == 0:
        list03.append(item+10)
print(list03)

list03 = [item + 10 for item in list01 if item % 2 == 0]
print(list03)
