'''
    day18复习
    迭代
        可迭代对象：__iter__() 可以for
        迭代器: __next__() 可以迭代（取元素）

    class 迭代器:
        def __next__():
            pass

    class 自定义类:
        def __iter__():
            return 迭代器()

    for item in 自定义类():
        pass

    生成器
        价值:惰性/延迟操作(省内存)
        生成器函数
            def 函数名():
                yield 数据

        yield:返回多个数据
        return:返回一个数据

        生成器表达式
            for item in (变量 for in 可迭代对象 if 条件):

    class 生成器本质:
        def __iter__():
            return self

        def __next__():
            pass


    函数式编程
        函数作为参数

        def 功能1():
            不变的代码
            变化点1

        def 功能2():
            不变的代码
            变化点2

        思想1：'封装'：变化/不变
        def 变化点1():
            ...
        def  变化点2():
            ...

        思想2：'继承'：抽象变化/隔离变化
        def 不变的代码(变量):
            # 变化点1()
            变量()

        思想3：'多态'：执行变化
        不变的代码(变化点2)
'''

