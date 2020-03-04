'''
列表的基础操作
'''

# 1.创建列表
# 空列表
# list01 = []
# list(可迭代对象) 使用可迭代对象快速创建列表
list01 = list()
print(list01)

# 具有值的列表
list02 = ['shibw', 18, True, [1, 2, 3]]
print(list02)

list02 = list(range(4))
print(list02)
list02 = list('我是小妖怪')
print(list02)

# 增加
# 需要借助列表的相关函数
# 追加元素 append()
# 向列表末尾添加一个元素
list02 = list(range(4))  # [0.1,2,3]
list02.append(4)
print(list02)

for i in range(5, 8):
    list02.append(i)
print(list02)

# extend() 使用可迭代对象扩展列表(向列表末尾添加一系列元素)
list02.extend(range(5, 8))
print(list02)
# insert(索引，元素) 插入[0,1,2,3,4,5,6,7]
list02.insert(0, 0)
print(list02)

# 列表的索引和切片
list01 = [0, 1, 2, 3, 4, 5]
print(list01[0:5])  # [0, 1, 2, 3, 4]
print(list01[::-1])  # [5, 4, 3, 2, 1, 0]
print(list01[-1])

# 修改
list01[-1] = 5.0
print(list01)
print(list01[-2:])  # 倒数第二个 到最后一个

# 获取列表的所有元素
list01 = [0, 1, 2, 3, 4]
for item in list01:
    print(item)

# 删除
# 根据元素删除
list01 = [0, 1, 2, 3, 4]
list01.remove(4)
print(list01)
# 根据索引
del list01[3]
print(list01)
