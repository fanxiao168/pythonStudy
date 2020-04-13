# 创建model02.py
# 定义一个函数 my_fun()
# 定义一个类 MyClass02
    # 构造函数  self.a = a
    # 实例方法  def fun02()
    # 类方法  def fun03()

def my_fun():
    print('my_fun')


class MyClass02:
    def __init__(self, a):
        self.a = a

    def fun02(self):
        print('fun02')

    @classmethod
    def fun03(cls):
        print('fun03')
