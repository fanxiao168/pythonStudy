'''
    要求：速度
        自行调试程序
    题目：将之前的图形管理器，由迭代器改为yield实现
'''


class GraphicManager:
    '''
        图形管理器  可迭代对象
    '''

    def __init__(self):
        self.__graphics = []

    def add_graphic(self, str_skill):
        self.__graphics.append(str_skill)

    def __iter__(self):
        for item in self.__graphics:
            yield item


manager = GraphicManager()
manager.add_graphic('圆形')
manager.add_graphic('矩形')
manager.add_graphic('三角形')

# 遍历 方法一
for item in manager:
    print(item)

# 遍历 方法二
iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
