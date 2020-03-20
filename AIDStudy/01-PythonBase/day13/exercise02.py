# 定义车类  数据（品牌 速度）  行为  跑
# 定义电动车  电动车（品牌  速度  电池容量） 行为跑
# 画内存图

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def run(self):
        print('走你')


class Electrocar(Car):
    def __init__(self, branch, speed, battery):
        super().__init__(branch, speed)
        self.battery = battery


c01 = Car('奔驰', 230)
c01.run()

e01 = Electrocar('BYD', 120, 15000)
e01.run()
