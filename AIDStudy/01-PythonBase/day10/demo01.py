# 类         类别       抽象
# 水果
# 类中的成员
# 数据（名词）成员  颜色/重量/味道...
# (方法) 行为（动词）成员   生长/腐烂...

# 狗
# 数据（名词） 成员  重量/颜色/体形...
# 行为（动词） 成员  跑/吃/....

# 万物皆对象
# 学生 sbw  空调 电脑  桌子  椅子....

# 对象  个体    具体实际存在的例子   实例
# 香蕉/苹果/哈密瓜         哈士奇/阿拉斯加/萨摩

# 类与类之间行为不同      对象与对象之间数据不同

# 类  抽象的概念    生活中的'类别'
# 水果是类
# 对象和实例：类的具体的实际例子 生活中某个类别的个体
# 水果中的对象是：苹果...

# 类中包含数据成员（名词）和方法成员（动词）
# 方法：指定是类中对象的行为

# 定义了一个Wife类
# 类名首字母大写
class Wife:
    # 数据成员
    # 身高  体重   姓名
    def __init__(self,height,weight,name):
        self.height = height
        self.weight = weight
        self.name = name

    # 行为成员
    # 唱歌 玩
    def sing(self):
        print('%s正在唱歌' % self.name)
    def play(self,game):
        print('%s正在玩%s' % (self.name,game))


# 自动调用__init__方法
w01 = Wife(2.2,90,'翠花')
print(w01.name)
w01.name = '翠翠'
print(w01.name)
w01.sing()
w01.play(2048)

# 思考为什么  如何解决？ 画内存图
w02 = Wife(2.1,20,'如花')
print(w02.height)
print(w02.weight)
print(w02.name)



#创建对象
# w01 = Wife()
# print(w01)
# #w01的身高 为 2.2
# w01.height = 2.2
# print(w01.height)
# w01.weight = 90
# print(w01.weight)
# w01.name = '翠花'
# print(w01.name)
