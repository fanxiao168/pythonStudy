# 创建敌人类 （名字 血量0-100  攻击力1-50）
class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise ValueError('血量不在范围内')

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 1 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError('攻击力不在范围内')


e01 = Enemy('灭霸', 100, 50)
print(e01.hp)
print(e01.atk)
