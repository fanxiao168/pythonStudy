# 定义 Dog类
# Dog中的数据有 name kinds color
# Dog的行为有
# eat 打印   狗吃xx
# run 打印   狗正在以xxkm/h的速度飞奔

class Dog:
    def __init__(self, name, kinds, color):
        self.name = name
        self.kinds = kinds
        self.color = color

    def eat(self, food):
        print('%s正在吃%s' % (self.name, food))

    def run(self, speed):
        print('%s的%s正在以%skm/h的速度飞奔' % (self.color, self.kinds, speed))


# 创建两个Dog对象
# 调用__init__
wangcai = Dog('旺财', '中华田园犬', '黄色')
wangcai.eat('骨头')
wangcai.run(40)

# 将Dog对象的地址赋值给doudou(两个变量指向一个对象)
doudou = wangcai
# doudou.eat('狗粮')
# doudou.eat('火腿肠')
doudou.name = '豆豆'
wangcai.eat('排骨')  # 豆豆正在吃排骨

list01 = [wangcai, doudou, Dog('儿子', '哈士奇', '灰色')]
list02 = list01
list01[2].color = '白色'
print(list02[2].color)  # ? 白色
