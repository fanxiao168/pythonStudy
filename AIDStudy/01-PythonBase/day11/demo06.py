# 老张开车去东北
# 老张   车
# 数据   行为

class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, postion, type):
        '''
        :param postion: 地名
        :param type: 去的方法
        :return:
        '''
        print('去:' + postion)
        type.run()


class Car:
    def run(self):
        print('走你~')


c01 = Car()
lz = Person('老张')
lz.go_to('东北', c01)
