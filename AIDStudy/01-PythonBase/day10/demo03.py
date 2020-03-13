class ICBC:
    # 类变量 总行的钱
    total_money = 1000000
    # 类方法
    @classmethod
    # cls 保存当前类的地址
    def print_total_money(cls):
        print(id(cls),id(ICBC))
        print(cls.total_money)

    def __init__(self,name,money):
        self.name = name
        self.money = money
        # 从总行扣除钱数
        ICBC.total_money -= money

    # 查询/操作类中的数据 不要用实例方法
    # def print_total_money(self):
    #     print(ICBC.total_money)


i01 = ICBC('北京天坛支行',100000)
i02 = ICBC('北京万寿路支行',100000)
ICBC.print_total_money()

# 非主流：通过对象访问类成员
# i02.print_total_money()
