# 创建敌人类  name  hp   atk
# 将敌人类的数据打印到控制台
# 克隆敌人对象 修改克隆对象数据  体会修改克隆对象数据不影响原对象

class Enemy:
    def __init__(self, name='', atk=100, hp=200):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __str__(self):
        return '%s--%d--%d' % (self.name, self.atk, self.hp)

    def __repr__(self):
        return 'Enemy("%s",%d,%d)' % (self.name, self.atk, self.hp)


e01 = Enemy('王五', 100, 50)
print(e01)

e02 = eval(repr(e01))
e02.name = '老王'
print(e02)
print(e01)
