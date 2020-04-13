# 创建exercise01.py 使用三种方法导入模块model02
# 调用函数my_fun 创建实例 变量a 实例方法  类方法
# 方法一
import model02

model02.my_fun()
c = model02.MyClass02(10)
print(c.a)
c.fun02()
model02.MyClass02.fun03()

# 方法二
from model02 import my_fun
from model02 import MyClass02

my_fun()
c = MyClass02(10)
print(c.a)
c.fun02()
MyClass02.fun03()

# 方法三
from model02 import *

my_fun()
c = MyClass02(10)
print(c.a)
c.fun02()
MyClass02.fun03()

# 将学生管理系统分为4个模块
# model.py   class xxxModel
# bll.py     class xxxController
# usl.py     class xxxView
# main.py    调用View的代码
# 运行main.py 启用学生管理系统
