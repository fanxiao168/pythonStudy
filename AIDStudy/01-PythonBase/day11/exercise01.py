# 创建敌人类 (名字 血量 00--100 攻击力1-50)
class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        # self.__hp = hp
        self.set_hp(hp)
        self.set_atk(atk)

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            raise ValueError('血量不在范围内')

    def get_atk(self):
        return self.__atk

    def set_atk(self, value):
        if 1 <= value <= 50:
            self.__atk = value
        else:
            raise ValueError('攻击力不在范围内')


e01 = Enemy('灭霸', 100, 50)
print(e01.get_hp())
print(e01.get_atk())
