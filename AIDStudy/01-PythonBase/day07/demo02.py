'''
集合的基础操作
'''

# 创建空集合
set01 = set()  # set()空集合
print(set01)

# 创建有两个元素的集合
set02 = {'a', 'b'}
print(set02)

# 集合中不包含重复的元素
set02 = set('abcabc')
print(set02)  # {'b', 'c', 'a'}

# 添加元素
# {'a'，'b', 'c'}
set02.add('lvze')
print(set02)

# add 将一个对象放入集合
# 列表是可变类型 不能放入集合（字符串，元组、数字）
# set02.add([0,1,2]) # TypeError: unhashable type: 'list'

# {'c', 'a', 'lvze', 'b'}
# 删除元素
set02.remove('a')
print(set02)

# 如果删除的元素不存在 报错
# set02.remove('x') # KeyError: 'x'

# 获取所有
for item in set02:
    print(item)
