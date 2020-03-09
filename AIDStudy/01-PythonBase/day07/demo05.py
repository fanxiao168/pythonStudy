'''
函数：表示一个功能
参数：使用功能时提供的信息
'''


# 做功能
def attack(count):
    '''
    攻击敌人
    :param count: int 攻击次数
    :return:
    '''

    for i in range(count):
        print('左钩拳')
        print('右钩拳')
        print('黑虎掏心')
        print('天马流星拳')
        print('临门一脚')
        # ...


# 用功能
# 函数名保存的是对应功能的代码地址
print(attack)

# 当函数定义完成后 程序不会马上执行
# 当函数调用者用函数名()的方式调用函数时
# 函数中的代码才会被执行
attack(1)
attack(2)
