# 老张开自己的车去东北
class Person:
    def __init__(self, name):
        self.name = name
        self.car = Car()

    def go_to(self, postion):
        # 需要车
        print(self.name + '去' + postion)
        Car.run()


class Car:
    def run():
        print('走你~')


lz = Person('老张')
lz.go_to('东北')
ll = Person('老李')
ll.go_to('河南')

'''
class Person:
    def __init__(self, name):
        self.name = name
        self.car = Car(self.name)

    def go_to(self, postion, type):
        # 需要车
        # Car().run()
        print(self.name + '去' + postion)
        type.run()

    # def go_to(self, postion):
    #     # 需要车
    #     # Car.run()
    #     print(self.name + '去' + postion)


class Car:
    def __init__(self, owner):
        self.owner = owner

    def run(self):
        print('这是%s的车' % self.owner)
        print('走你~')


# c01 = Car('fan')
lz = Person('老张')
ll = Person('老李')
lz.go_to('东北', ll.car)

'''
