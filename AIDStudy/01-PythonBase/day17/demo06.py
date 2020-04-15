'''
    函数式编程  应用 --- 将函数作为参数
'''

list01 = [4, 5, 5, 65, 5, 6]


def fun01():
    for item in list01:
        if item % 2:
            yield item


def fun02():
    for item in list01:
        if item > 10:
            yield item


def fun03():
    for item in list01:
        if 3 < item < 10:
            yield item


# 面向函数：
# '封装'：分
def condition01(item):
    return item % 2 == 1


def condition02(item):
    return item > 10


def condition03(item):
    return 3 < item < 10


# '继承'：隔离（通过参数，抽象具体函数）
# '万能查找'
def fun(func_condition):
    for item in list01:
        # if 3 < item < 10:
        # if condition03(item):
        # # '多态'：做
        if func_condition(item):
            yield item


re = fun(condition01)
for item in re:
    print(item)

# 练习：
# 在技能列表中，获取持续时间大于10的所有技能
# 在技能列表中，获取编号在102--105之间的所有技能
# 步骤1：实现功能
# 步骤2：封装--提取变化与不变的代码
# 步骤3：定义'万能查找'方法
# 步骤4：将不变与变化的方法相互结合
