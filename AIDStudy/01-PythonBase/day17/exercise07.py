'''
    练习3：
    自定义生成器函数 my_enumerate, 实现下列效果

    list01 = ['无忌','翠山','翠翠']
    for item in enumerate(list01):
        print(item) #
'''


def my_enumerate(iterable_target):
    index = 0
    for item in iterable_target:
        yield (index, item)
        index += 1


list01 = ['无忌', '翠山', '翠翠']
for item in my_enumerate(list01):
    print(item)  # item 是元组类型（索引 元素）

for index, element in enumerate(list01):
    print(index)
    print(element)
