'''
    练习4：
    自定义生成器my_zip,实现下列效果

    list01 = ['孙悟空','白雪公主','贾宝玉']
    list02 = [101,102,103]

    for item in zip(list01,list02):
        print(item) # 元组（第一个列表的元素，第二个列表的元素）
'''


def my_zip(iterable_target01, iterable_target02):
    for i in range(len(iterable_target01)):
        yield (iterable_target01[i], iterable_target02[i])


list01 = ['孙悟空', '白雪公主', '贾宝玉']
list02 = [101, 102, 103]

for item in my_zip(list01, list02):
    print(item)  # 元组（第一个列表的元素，第二个列表的元素）

for item in zip(list01, list02):
    print(item)
