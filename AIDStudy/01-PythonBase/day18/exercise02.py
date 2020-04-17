'''
    1.获取可迭代对象中长度最大的元素(列表)
     ([1,1],[2,2,2,2],[3,3])
    2.在技能列表中，获取所有技能的名称与持续时间与攻击力
    3.在技能列表中，获取攻击力最小的技能
    4.对技能列表根据持续时间进行降序排列
    要求：使用两种方式实现ListHelper.py
                       内置高阶函数
'''

from common.list_helper import ListHelper


class Skill:
    def __init__(self, id, name=None, atk=None, duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

    # 对象----> 字符串
    def __str__(self):
        return self.name


list01 = [
    Skill(101, '乾坤大挪移', 8000, 30),
    Skill(102, '九阳神功', 9000, 50),
    Skill(103, '黑虎掏心', 9800, 10),
    Skill(104, '葵花宝典', 6000, 2)
]

# 1.
tuple01 = ([1, 1], [2, 2, 2, 2], [3, 3])
print(ListHelper.get_max(tuple01, lambda item: len(item)))
print(max(tuple01, key=lambda item: len(item)))

# 2.
for item in ListHelper.select(list01, lambda item: (item.name, item.duration, item.atk)):
    print(item)
for item in map(lambda item: (item.name, item.duration, item.atk), list01):
    print(item)

# 3.
print(min(list01, key=lambda item: item.atk))

# 4.
for item in sorted(list01, key=lambda item: item.duration, reverse=True):
    print(item)
