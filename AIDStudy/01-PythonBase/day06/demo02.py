'''
列表推导式
快速的将可迭代对象变成列表
'''

list01 = [10, 1, 15, 5, 6, 7]
# 将list01中的每一个数加一放到list02中
list02 = []
for item in list01:
    list02.append(item + 1)
print(list02)

# 从可迭代对象list01中获取元素
# 将元素带入到前面的表达是item+1
# 将结果保存到列表 继续从list01获取下一个元素 直到没有元素为止
list03 = [item + 1 for item in list01]
print(list03)

list04 = []
for item in list01:
    if item >= 10:
        list04.append(item + 1)
print(list04)

# 从可迭代对象list01中获取元素
# 先做判断 如果结果为False  取下一个元素继续判断
# 如果结果为True 将元素带入到前面的表达式
# 将结果保存到列表 重复执行
list05 = [item + 1 for item in list01 if item >= 10]
print(list05)

# 列表推导式嵌套
list01 = [1, 2, 3]
list02 = [4, 5, 6]
list03 = []
# 将两个列表中所有的值分别相加 将结果保存到list03
for item1 in list01:
    for item2 in list02:
        list03.append(item1 + item2)
print(list03)
list03 = [item1 + item2 for item1 in list01 for item2 in list02]
print(list03)
