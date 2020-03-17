# 创建敌人类 （名字 血量0-100 攻击力1-50）

class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        # self.__hp = hp
        # self.set_hp(hp)
        # self.set_atk(atk)
        self.hp = hp
        self.atk = atk

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise ValueError('血量不在范围内')

    hp = property(get_hp, set_hp)

    def get_atk(self):
        return self.__atk

    def set_atk(self, value):
        if 0 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError('攻击力不在范围内')

    atk = property(get_atk, set_atk)


e01 = Enemy('灭霸', 100, 50)
print(e01.hp)
# print(e01.get_hp())
# print(e01.get_atk())
print(e01.atk)
