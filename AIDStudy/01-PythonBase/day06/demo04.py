'''
字典的基本操作
'''

# 创建字典
dict01 = {}  # 空字典
dict01 = dict()
print(dict01)

# 'shibw':20
#   键     值   键值对
dict02 = {'shibw': 1311794174}
# 字典的数据以键值对的形式保存
# 多个键值对用逗号分割
dict02 = {'shibw': 20, 'wwc': 30}

# 通过函数创建字典
dict02 = dict([['name', 'shibw']])
print(dict02)  # {'name': 'shibw'}
dict02 = dict([['name', 'shibw'], ('age', 20)])
print(dict02)  # {'name': 'shibw', 'age': 20}

# 添加元素
dict01 = {'name': 'shibw', 'age': 20}
# 如果字典中没有对应的键存在
# 可以直接对不存在的键赋值 向字典中添加该键值对
dict01['address'] = 'beijing'
print(dict01)

# 修改
# 如果对已经存在的赋值 相当于修改原本键的值
dict01['address'] = 'qiaowan'
print(dict01)

# 删除
del dict01['address']
print(dict01)

# 查找字典中的元素
dict01 = {'name': 'shiwb', 'age': 20}
print(dict01['name'])
# print(dict01['address']) # KeyError: 'address'
if 'name' in dict01:
    print(dict01['name'])
if 'address' in dict01:
    print(dict01['address'])

# 字典的常用方法
# 使用get 获取字典指定的值
print(dict01.get('name'))
# 如果键不存在 可以指定返回默认值
print(dict01.get('address'), 'beijing')
print(dict01)
# 同get 但是键不存在时 会添加键值对
print(dict01.setdefault('address'), 'beijing')
print(dict01)
dict01.popitem()  # 删除最后一个键值对
print(dict01)
dict01.popitem()
print(dict01)

dict01 = {'name': 'shibw', 'age': 20}
dict02 = {'name': 'laowang', 'address': '北京'}
# 使用02更新字典01 如果02中的键在01中不存在 添加
# 如果02中不存在01中的键 保留01中的键值对
# 如果02中的键在01中存在 使用02的值
dict01.update(dict02)
print(dict01)  # {'name': 'laowang', 'age': 20, 'address': '北京'}

# 获取字典所有元素
for key in dict01:
    print(key)  # 获取的是字典中所有的键
    print(dict01[key])

# 获取键值对（键，值）
for value in dict01.values():
    print(value)

dict01 = {1: "1.0", 2: "2.0"}
print(dict01)
dict01 = {(1, 2, 3): 3, (1, 2, 3, 4): 4}
print(dict01)

# 可变类型无法通过哈希算法运算
# 所以字典的键都是不可变类型
# dict01 = {[1,2,3]:3} # TypeError: unhashable type: 'list'
print(dict01)
