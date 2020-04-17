'''
    装饰器
    练习：exercise04.py
'''


# def print_func_name(func):
#     def wrapper():
#         print(func.__name__)  # 打印函数名称
#         func()  # 调用函数
#
#     return wrapper
#
#
# @print_func_name
# def say_hello():
#     print('hello')
#
#
# # 拦截：新功能 + 旧功能
# say_hello = print_func_name(say_hello)
#
#
# def say_goodbye():
#     print('goodbye')
#
#
# say_hello()
# say_goodbye()

# 需求：在不改变原函数以及调用情况下，增加新功能（打印函数名称）

def print_func_name(func):
    # args 原函数参数可以无限制
    def wrapper(*args, **kwargs):
        print(func.__name__)  # 打印函数名称
        # return 原函数返回值
        return func(*args, **kwargs)  # 调用函数

    return wrapper


@print_func_name
def say_hello():
    print('hello')
    return 1


@print_func_name
def say_goodbye(name):
    print(name, '---goodbye')
    return 2


print(say_hello())  # 1
print(say_goodbye('qtx'))  # 2
