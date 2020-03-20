# 老张开车去东北  day11/demo06.py
# 需求变化： 坐飞机
#           坐火车
#           骑车

class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, postion, type):
        '''
        :param postion:地名
        :param type: 去的方法
        :return:
        '''
        print('去' + postion)
        # 判断怎么走
        # 如果是车就跑
        if isinstance(type, Car):
            type.run()
        elif isinstance(type, Airplane):
            type.fly()
        


class Car:
    def run(self):
        print('走你～')


class Airplane:
    def fly(self):
        print('嗖～')


c01 = Car()
a01 = Airplane()
lz = Person('老张')
lz.go_to('东北', c01)
lz.go_to('东北', a01)
