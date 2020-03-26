# 手雷炸了 伤害敌人/玩家的姓名
# 还可能伤害未知生命（动物，花草...）
# 要求 使用面向对象的方式实现场景
# 增加事物时 不影响手雷
# 画设计图

# 手雷
class Granade:
    def __init__(self, atk=99):
        self.atk = atk

    def explode(self, target):
        # 如果传入的不是可受伤的 报错
        if not isinstance(target, Demageable):
            raise ValueError('对象不能受伤')
        print('手雷爆炸啦--%d' % self.atk)
        target.damage(self.atk)


class Demageable:
    def damage(self, value):
        # 如果子类不重写 则异常
        raise NotImplementedError()


# ----------------------------------------
# 敌人
class Enemy(Demageable):
    def __init__(self, hp=100):
        self.hp = hp

    def damage(self, value):
        print('敌人受伤咯')
        self.hp -= value
        if self.hp <= 0:
            print('敌人死了')


# 玩家
class Player(Demageable):
    def __init__(self, hp=100):
        self.hp = hp

    def damage(self, value):
        print('玩家受伤啦')
        self.hp -= value
        if self.hp <= 0:
            print('你真菜')


# 小动物
class Animal:
    def damage(self, value):
        print('小动物受伤啦')


a01 = Animal()

g01 = Granade(100)

e01 = Enemy(200)
p01 = Player(10)

g01.explode(e01)
g01.explode(e01)
g01.explode(p01)
# g01.explode(a01)
