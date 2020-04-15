'''
    函数式编程 语法
'''


def fun01():
    print('fun01执行啦')


# 1. 将函数赋值给变量
a = fun01
a()  # 通过变量调用函数


def fun02():
    print('fun02执行啦')


# 通过参数调用函数，目的就是灵活（定义函数不决定逻辑，执行函数再决定逻辑）
# 2.函数可以作为参数传递
def fun03(func):
    print('fun03执行喽')
    func()


fun03(fun01)
fun03(fun02)
