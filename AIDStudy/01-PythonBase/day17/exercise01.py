'''
    要求：速度
    题目：迭代图形管理器
    class GraphicManager:
        pass
    manager = GraphicManager()
    manager.add_graphic('圆形')
    manager.add_graphic('矩形')
    manager.add_graphic('三角形')
    for item in manager:
        print(item)
'''


class GraphicIterator:
    '''
        迭代器
    '''

    def __init__(self, data):
        self.__target = data
        self.__index = -1

    def __next__(self):
        # 如果没有数据则抛出异常
        if self.__index >= len(self.__target) - 1:
            raise StopIteration
        # 返回数据
        self.__index += 1
        return self.__target[self.__index]


class GraphicManager:
    '''
        图形管理器   可迭代对象
    '''

    def __init__(self):
        self.__graphics = []

    def add_graphic(self, str_skill):
        self.__graphics.append(str_skill)

    def __iter__(self):
        return GraphicIterator(self.__graphics)


manager = GraphicManager()
manager.add_graphic('圆形')
manager.add_graphic('矩形')
manager.add_graphic('三角形')

for item in manager:
    print(item)
