# 定义一个图形管理器类
# 1.保存所有的图形
# 2.提供计算 所有图形总面积的功能

class GraphicManager:
    def __init__(self):
        self.__list_graphic = []

    @property
    def list_graphic(self):
        return self.__list_graphic

    def add_graphic(self, graphic):
        if not isinstance(graphic, Graphic):
            raise ValueError()
        else:
            self.__list_graphic.append(graphic)

    def calc_total_area(self):
        total_area = 0
        for item in self.__list_graphic:
            total_area += item.calc_area()
        return total_area


class Graphic:
    def calc_area(self):
        # 如果子类不重写父类的功能 异常
        raise NotImplementedError()


# 原形 pi*r**2
# 矩形 长*宽
# 要求增加新图形时 不影响管理器代码

class Circle(Graphic):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return 3.14 * self.radius ** 2


class Rectange(Graphic):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width


c01 = Circle(5)
r01 = Rectange(10, 20)
mananger = GraphicManager()
mananger.add_graphic(c01)
mananger.add_graphic(r01)
print(mananger.list_graphic)
print(mananger.calc_total_area())
