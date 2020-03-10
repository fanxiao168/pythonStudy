'''
函数参数传递
形参
'''


# 打印矩形 要求传递行数和列数 还有填充字符
# 如果用户不传递填充字符 默认使用*
# 默认形参 实参可以不传递数据 使用形参的默认值
# 当实参传递数据时 会覆盖默认值
# def fun01(row,col,char='*'):
#     for r in range(row):
#         for c in range(col):
#             print(char,end=' ')
#         print()
#
# fun01(3,3)
# fun01(3,3,'-')

def fun01(a=0, b=1, c=2):
    print(a)
    print(b)
    print(c)


# 传参方式更灵活
fun01()
fun01(1, 'b')
fun01(b='bbbb')


# 星号元素形参
# 接受不定数量的实参 让实参的数量可以无限多
def fun02(p1, p2, *args):
    print(p1)
    print(p2)
    print(*args)


fun02(1, 2, 3, 4, 6, 6, 7, 8, 9, 10)
fun02(1, 2)


# 在星号元组形参以后的形参叫做命名关键字形参
# 传递实参的过程中，必须指定形参的名字
def fun03(*args, p1='', p2):
    print(*args)
    print(p1)
    print(p2)


fun03(1, 2, 3, 4, 5, 6, p2=20)


# 案例
# print()
# sep是在两个值中间输出的字符串
# end是在最后的一个值后面输出的字符串
def myprint(*args, sep=' ', end='\n', file=None):
    print(*args, sep=sep, end=end)


myprint(1, 2, 3, 4)
myprint(10, 20, 30, sep='+')


# 星号以后的位置形参是命名关键字形参
# 传递实参只接受关键字实参
def fun04(*, p1=0, p2):
    print(p1)
    print(p2)


fun04(p1=100, p2=200)
fun04(p2=200)


# 双星号字典形参 让关键字实参的的数量无限
# 将关键字实参的变量名作为字典的键 值作为字典中对应键的值保存
def fun05(**kwargs):
    print(kwargs)


fun05(a=10)
fun05(a=10, b=20, c=30)


# 混合使用
# 语法 位置形参要在关键字形参前面定义
# 只要出现关键字形参 后面的参数也要带有关键字
# def fun06(a=10,b,c):# 报错 SyntaxError: non-default argument follows default argument
#     print(a)
#     print(b)
#     print(c)
#
# fun06(20,30)

# 定义一个函数 函数中包含位置形参、星号元组形参、默认形参、命名关键字形参和双星号字典形参
def fun07(a, *args, b='bbb', c, **kwargs):
    print(a)
    print(args)
    print(b)
    print(c)
    print(kwargs)


fun07(1, c='ccc')
fun07(5, 6, 7, c='abc', d='789')


# 定义一个函数 接受任意的参数 并输出结果
def fun08(*args, **kwargs):
    for item in args:
        print(item)
    for k, v in kwargs.items():
        print(k, v)


fun08()
fun08(5, 6, 7, a=123, b='789')
