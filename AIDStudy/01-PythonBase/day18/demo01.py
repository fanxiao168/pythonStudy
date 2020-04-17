'''
    lambda: 匿名函数
    作用：充当实参
'''


def fun01():
    print('fun01')


fun01()

# 无参数 无返回值
a = lambda: print('fun01')
a()


def fun02(func):
    print('fun02')
    func()


# 将函数作为参数，建议使用lambda
fun02(lambda: print('fun01'))


def fun03(a, b, c):
    print('fun03')


# 有参数lambda
b = lambda a, b, c: print('fun03')

fun03(1, 1, 1)


def fun04():
    print('fun04')
    print('fun04又执行喽')


fun04()

# lambda 函数体只能又一句话
# fun02(lambda:print('fun04++'); print('fun04又执行啦'))
# 不支持赋值语句
# fun02(lambda a:a.name='zs')
