# 定义一个两个数相加的函数
# 所有函数都有返回值
# 函数通过return 语句将返回值返回给函数调用者
# 返回的位置就是函数调用的位置
# 如果没有写return语句 默认返回None

def myadd(num1, num2):
    # result = num1 + num2
    # return result
    # 返回结果 退出函数
    return num1 + num2
    # return语句后的代码不会执行
    # print(num1 + num2)
    # 要不要写return语句取决于用户是否要再次处理函数的结果
    # 如果需要再次处理就必须通过return返回结果


print(myadd(10, 20))
result = myadd(10, 20)
# 输出 结果是30
print('结果是%s' % result)
