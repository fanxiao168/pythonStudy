# 使用for循环原理打印元组中的所有元素
tuple01 = (4, 5, 66, 7, 2)
iterator = tuple01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key)
    except StopIteration:
        break

# 不使用for循环 打印字典中所有的数据
dict01 = {'张翠山': 101, '殷素素': 102, '张无忌': 103}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
