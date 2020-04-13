# 规定其他模块 from model03 import *
# 可以导入的内容
# __all__ == ['fun01']

def fun01():
    print('in model03')


# 隐藏成员 使用单下划线命名
# 在其他模版不能使用
# 仅限 from xx import *
def _fun02():
    print('fun02')


