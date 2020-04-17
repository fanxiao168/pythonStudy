'''
    闭包：外部函数执行完毕后，不立即释放内存。
         而是等着内部函数使用外部嵌套变量
    练习：exercise03
'''


def fun01():
    a = 10

    def fun02():
        print(a)

    return fun02  # 返回内部函数（没有执行）


# re 存储的是fun02
re = fun01()
re()  # 调用fun02 10
