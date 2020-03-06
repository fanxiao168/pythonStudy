'''
元组的基本操作
'''

# 创建元组
tuple01 = ()  # 空元组
tuple01 = tuple()
print(tuple01)

tuple02 = (0, 1, 'nihao', True)
print(tuple02)
# 预留空间的存储机制(列表)--->按需分配的存储机制(元组)
list01 = ['a', 'b']
tuple02 = tuple(list01)
print(tuple02)
list02 = list(tuple02)
print(list02)

tuple02 = ('a')  # 不是元组
print(type(tuple02))  # <class 'str'>
tuple02 = ('a',)  # 如果元组中只有一个元素 必须加逗号
print(type(tuple02))  # <class 'tuple'>
name, age = 'shibw', 18  # ('shibw',18)

# 获取元素
tuple01 = ('a', 'b', 'c', 'd')
print(tuple01[2])
# tuple01[2] = 'C' # 元组不可变 不能赋值 TypeError: 'tuple' object does not support item assignment
print(tuple01[1:3])
# 所有元素
for item in tuple01:
    print(item)

for i in range(len(tuple01) - 1, -1, -1):
    print(tuple01[i])

# del tuple01[3] # 元组不可变 不能删除 TypeError: 'tuple' object doesn't support item deletion

tuple01 = ([1, 2], 3, 4)
print(tuple01[0][1])

tuple01[0][1] = 2.0  # 元组无法改变 元组中的列表可以改变
print(tuple01)
