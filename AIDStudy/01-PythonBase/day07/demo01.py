# 从列中依次取 10 20 30 放入max 函数中 求最大值
max_value = max([10, 20, 30])
print(max_value)

# 从列表中依次取name shibw 放入dict函数 创建字典
# 单独的name 无法创建字典 需要指定键值对
# dict01 = dict(['name','shibw'])  ValueError: dictionary update sequence element #0 has length 4; 2 is required
# print(dict01)

# 从列表中取['name','shibw'] 将'name'作为键 'shibw'作为值 创建字典
dict01 = dict([['name', 'shibw']])
print(dict01)
dict02 = dict([('name', 'shibw')])
print(dict02)
