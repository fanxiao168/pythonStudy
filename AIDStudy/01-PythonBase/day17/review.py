'''
    祁天暄
    qq:1986086334
    内容：迭代器/生成器/函数式编程/2048

    可迭代对象
'''

tuple01 = (1, 2, 3, 4, 5)
for item in tuple01:
    print(item)

iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
