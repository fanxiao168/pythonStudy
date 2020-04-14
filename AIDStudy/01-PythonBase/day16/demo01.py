# coding=utf-8
# coding:utf-8
# -*- coding:utf-8 -*-

# 包
#   模块
#       类
#           函数
#               语句

import sys
import model01
#
# # from model01 import *
#
# print(model01.a)
# model01.fun01()
# c = model01.MyClass01()
# c.fun02()
# model01.MyClass01.fun03()

from model01 import a, fun01

print(a)

fun01()


def fun01():
    print('in demo01')


# __name__ 自己运行时（作为主程序执行）就叫__main__
# 当别人调用模块时__name__的值为模块名

if __name__ == '__main__':
    print(__name__)
    print(sys.path)
