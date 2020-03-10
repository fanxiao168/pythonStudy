'''
函数传参
实参传递方式
'''


def fun01(a, b, c):  # 形参 a b c
    print(a)
    print(b)
    print(c)


# 位置实参 实参是根据位置与形参对应的
# 如果实参位置发生改变 会影响函数结果
fun01(10, 20, 30)
fun01(30, 10, 20)

# 序列实参  用*将序列中的元素拆开然后与形参依次对应
# 序列 字符串 列表 元组
list01 = [10, 20, 30]
fun01(*list01)
str01 = 'abcd'
# fun01(*str01) # TypeError: fun01() takes 3 positional arguments but 4 were given

# 关键字实参
# 实参的值与形参的名称对应
fun01(a=10, b=20, c=30)
# 使用关键字实参 传参的顺序可以不固定
fun01(c=30, a=10, b=20)
# fun01(a=10,b=20,d=40) # TypeError: fun01() got an unexpected keyword argument 'd'

# 字典实参 使用**将字典拆开， 字典中的键值对以关键字的形式进行对应，传递值
dict01 = {'a': 10, 'b': 20, 'c': 30}
fun01(**dict01)  # 10 20 30
# 字典中的键的名称要与形参名对应
dict01 = {'a': 10, 'e': 20, 'd': 30}
# fun01(**dict01) # TypeError: fun01() got an unexpected keyword argument 'e'

# 混合使用
# 语法规定 先写位置参数 再写关键字参数
fun01(10, 20, c=30)
# fun01(c=30,b=20,10) # SyntaxError: positional argument follows keyword argument
fun01(10, c=30, b=20)
