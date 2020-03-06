list01 = ['a', 'b', 'c']
list01[0] = ['A', 'B']
print(list01)  # [['A', 'B'], 'b', 'c']

# 将右边列表的值赋值给list01的第一个位值
list01[1:2] = ['哪吒']
print(list01)  # [['A', 'B'], '哪吒', 'c']

# 序列赋值
name, age = ['shibw', 18]
print(name, age)  # shibw 18

list02 = list01[::-1]
print(list02)  # ['c', '哪吒', ['A', 'B']]
print(list01[0] is list02[-1])  # True
list01[0] = '李靖'
print(list02[-1])  # ['A', 'B']
