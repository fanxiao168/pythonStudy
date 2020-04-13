# 方法一
# 语法  import 模块
# 本质使用变量model01存储模块的地址
# 优点： 不担心成员命名冲突
# import model01
# 模块名.成员
# def fun01():
#       print('demo02的fun01')

# model01.fun01()
# model01.MyClass()
# fun01()

# 为了简化代码 可以考虑为一个长的模块名取别名
# 在当前文件中 别名等同于模块名
# import model01 as m
# m.fun01()


# 方法二
# 语法  from 模块名  import 成员
# 本质：将模块指定成员直接导入到当前模块作用域
# 缺点：可能会造成成员冲突
# from model01 import fun01
# from model01 import MyClass
# from model01 import fun01, MyClass
#
# # def fun01():
# #   print('demo02的fun01')
#
# fun01()


# 方法三
# 语法  from 模块名  import *
# 缺点：可能会造成成员冲突几率更大
from model01 import *

fun01()
MyClass().fun02()
