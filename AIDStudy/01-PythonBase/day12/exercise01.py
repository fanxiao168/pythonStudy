# 小明去银行取钱
class Persion:
    def __init__(self, name, money=None):
        self.name = name
        self.money = money


class Bank:
    def __init__(self, money=None):
        self.money = money

    def draw_money(self, target, value):
        if value <= 0:
            raise ValueError('value不能小于0')
            # return 'value不能小于0'
        print(target.name, '在取', value, '钱')
        self.money -= value
        target.money += value
        print('%s现在有%s钱' % (target.name, target.money))


xm = Persion('小明', 0)
zs = Bank(100000)
zs.draw_money(xm, 1000)
print(zs.draw_money(xm, -1000))
zs.draw_money(xm, 1000)
