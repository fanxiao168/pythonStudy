'''
    生成器（函数/表达式）练习
'''


class Skill:
    def __init__(self, id, name=None, atk=None, duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

    # 对象---> 字符串
    def __str__(self):
        return self.name


list01 = [
    Skill(101, '乾坤大挪移', 8000, 30),
    Skill(102, '九阳神功', 9000, 50),
    Skill(103, '九阴白骨爪', 500, 10),
    Skill(104, '黑虎掏心', 9800, 40),
    Skill(105, '葵花宝典', 6000, 2)
]


# 通过生成器函数/生成器表达式实现：
# 1. 在技能列表中，查找攻击力大于8000的所有技能对象。
# def find01():
#     for item in list01:
#         if item.atk > 8000:
#             yield item  # 返回多个结果
#
# for item in find01():
#     print(item)
#
# for item in (item for item in list01 if item.atk > 8000):
#     print(item)

# 2.在技能列表中，查找编号是103的技能对象
# def find02():
#     for item in list01:
#         if item.id == 103:
#             yield item  # 返回一个结果

def find02():
    for item in list01:
        if item.id == 103:
            return item  # 返回一个结果


re = find02()
print(re.name)


# 练习3：在技能列表中，获取所有技能的名称
def find03():
    for item in list01:
        yield item.name  # 返回多个结果


for item in find03():
    print(item)

for item in (item.name for item in list01):
    print(item)
