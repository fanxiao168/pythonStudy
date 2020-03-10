# Global 全局作用域
a = 100  # 全局变量 在文件内部都可以访问到


def change():
    # Local 局部作用域
    # 对于inner_fun来说 外部嵌套作用域
    a = 10  # 局部变量 只能在函数内部使用

    # 当函数调用时创建局部变量 函数结束后销毁
    def inner_fun():
        # Local 局部作用域
        # a = 1
        print(a)

    inner_fun()
    print(a)


change()
