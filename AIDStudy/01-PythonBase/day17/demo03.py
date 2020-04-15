'''
    yield ----> 生成器函数
    练习：exercise05.py
         exercise06.py
         exercise07.py
         exercise08.py
'''


class MyRange:
    def __init__(self,stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        number = -1
        while number < self.__stop_value - 1:
            number += 1
            yield number

for item in MyRange(7):
    print(item)


def my_range(stop):
    number = -1
    while number < stop - 1:
        number += 1
        yield number

# 惰性操作/延迟操作
# 返回值是生成器对象（可迭代对象 + 迭代对象）
iterator = my_range(99999)
for item in iterator:
    print(item)