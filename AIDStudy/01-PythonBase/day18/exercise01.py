'''
    练习1：
        需求：在技能列表中，查找编号是102的技能对象
             在技能列表中，查找名称是九阳神功的技能
        封装：将变化点与通用代码定义到函数中
        继承：在通用代码中抽象变化点
        将通用代码写到ListHelper中
        在当前模块中调用
'''

from common.list_helper import ListHelper


class Skill:
    def __init__(self, id, name=None, atk=None, duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

    # 对象-->字符串
    def __str__(self):
        return self.name


list01 = [
    Skill(101, '乾坤大挪移', 8000, 30),
    Skill(102, '九阳神功', 9000, 50),
    Skill(103, '黑虎掏心', 9800, 10),
    Skill(104, '葵花宝典', 6000, 2)
]

'''
def find01():
    for item in list01:
        if item.duration > 10:
            yield item

def find02():
    for item in list01:
        if 102<=item.id<=105:
            yield item
'''


def condition01(item):
    return item.duration > 10


def condition02(item):
    return 102 <= item.id <= 105


# def find(func_condition):
#     for item in list01:
#         if func_condition(item):
#             yield item
#
# for item in find(condition01):
#     print(item)


for item in ListHelper.find_all(list01, condition01):
    print(item)

# 练习2
'''
def find03():
    for item in list01:
        if item.id == 102:
            return item

def find04():
    for item in list01:
        if item.name == '九阳神功':
            return item
'''


def condition03(item):
    return item.id == 102


def condition04(item):
    return item.name == '九阳神功'


# def find(func):
#     for item in list01:
#         # if item.name == '九阳神功':
#         # if condition04(item):
#         if func(item):
#             return item
# print(find(condition03).name)

re = ListHelper.find_single(list01, condition04)
print(re.name)

# 练习：将之前调用find_all和find_single,改为lambda写法
for item in ListHelper.find_all(list01, lambda item: item.duration > 10):
    print(item)

re = ListHelper.find_single(list01, lambda item: item.name == '九阳神功')
print(re.name)

# 练习3：
# 需求：在技能列表中，计算所有技能攻击力总和
#      在技能列表中，计算所有技能持续时间总和
# 封装: 将变化点与通用代码定义到函数中
# 继承: 在通用代码中抽象变化点
# 将通用代码写到ListHelper中
# 在当前模块调用

# def sum01():
#     sum_value = 0
#     for item in list01:
#         sum_value += item.atk
#     return sum_value
#
# def sum02():
#     sum_value = 0
#     for item in list01:
#         sum_value += item.duration
#     return sum_value
#
# def condition04(item):
#     return item.atk
#
# def condition05(item):
#     return item.duration
#
# def sum(func):
#     sum_value = 0
#     for item in list01:
#         # sum_value += item.duration
#         # sum_value += condition05(item)
#         sum_value += func(item)
#     return sum_value
#
# print(sum(condition04))

re = ListHelper.sum(list01, lambda item: item.duration)
print(re)

# 练习4
# 需求：在技能列表中，获取所有技能的名称与持续时间
#      在技能列表中，获取所有技能的名称与攻击力
# 封装: 将变化点与通用代码定义到函数中
# 继承: 在通用代码中抽象变化点
# 将通用代码写到ListHelper中
# 在当前模块调用
for item in ListHelper.select(list01, lambda item: (item.name, item.duration)):
    print(item)

# 练习5
# 需求：在技能列表中，计算攻击力最大的技能
#      在技能列表中，计算持续时间最大的技能
# 封装: 将变化点与通用代码定义到函数中
# 继承: 在通用代码中抽象变化点
# 将通用代码写到ListHelper中
# 在当前模块调用
re = ListHelper.get_max(list01, lambda e: e.atk)
print(re.name)

# 练习6
# 需求:  对技能列表, 根据攻击力进行升序排列.
#       对技能列表, 根据持续时间进行升序排列.
# 封装: 将变化点与通用代码定义到函数中.
# 继承: 在通用代码中抽象变化点
# 将通用代码写到ListHelper中
# 在当前模块中调用.
ListHelper.order_by(list01, lambda e: e.duration)
for item in list01:
    print(item.name)
