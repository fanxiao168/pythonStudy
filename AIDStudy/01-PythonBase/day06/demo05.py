'''
字典推导式
'''

# 需求 range(10) 作为key 值为key的平方
dict01 = {}
for i in range(10):
    dict01[i] = i ** 2
print(dict01)

# 字典推导式
dic01 = {i: i ** 2 for i in range(10)}
print(dict01)

# 需求 range(10) 大于5的作为key  值为key的平方
dict02 = {}
for i in range(10):
    if i > 5:
        dict02[i] = i ** 2
print(dict02)

dict02 = {i: i ** 2 for i in range(10) if i > 5}
print(dict02)
