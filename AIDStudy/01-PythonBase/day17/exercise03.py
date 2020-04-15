'''
    练习：定义MyRange类，实现下列功能
    for item in MyRange(5):
        print(item) # 0 1 2 3 4
'''


class MyRangeIterator:
    def __init__(self, stop):
        self.__start = -1
        self.__stop = stop

    def __next__(self):
        if self.__start >= self.__stop - 1:
            raise StopIteration
        self.__start += 1
        return self.__start


class MyRange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        return MyRangeIterator(self.__stop_value)


# 循环一次  计算一次  返回一次
for item in MyRange(99999):
    print(item)
