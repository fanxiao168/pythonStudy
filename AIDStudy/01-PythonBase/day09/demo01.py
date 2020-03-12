'''
函数
'''


# def 函数名称(形参):
#     函数体

# 调用函数
# 函数名称(实参)

# 参数 调用者传递给定义者的信息
# 返回值 定义者传递给调用者的结果

# 形式参数
# 位置参数
# 默认形参 给形参定义默认值 实参可以不传递
# 星号元组形参 *args 让位置实参理论上无限
# 命名关键字形参 放在*后面 所有的参数都需要用关键字传递
# 双星号字典形参 **kwargs 让关键字实参理论上无限

def fun(*args, **kwargs):
    pass


# 实际参数
# 位置实参 实参与形参位置对应
# 序列实参 参数过多 可以将参数储存到序列 用*将序列拆分然后传值
fun(*[1, 2, 3, 4])


# 关键字实参 实参与形参按名称对应 可以不按顺序传递
# 字典实参 参数过多 可以将参数储存到字典 用** 将字典拆分成键值对 然后传值

def fun01(a, b, c):
    print(a)
    print(b)
    print(c)


fun01(1, 2, 3)
list01 = [1, 2, 3]
fun01(*list01)
fun01(a=1, c=3, b=2)
dict01 = {'a': 1, 'b': 2, 'c': 3}
fun01(**dict01)


def fun02(a=0, b=0, c=0):
    print(a)
    print(b)
    print(c)


fun02()
fun02(c=10)


def fun03(*args):
    print(args)
    print(*args)


fun03(1, 2, 3, 4, 5, 6)


def fun04(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


fun04(a=1, b=2, c=3)


def fun05(*, name):
    print(name)


fun05(name=123)
