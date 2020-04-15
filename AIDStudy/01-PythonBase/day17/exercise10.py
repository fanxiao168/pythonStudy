class Skill:
    def __init__(self, id, name=None, atk=None, duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

        # 对象 ----> 字符串
        def __str__(self):
            return self.name


list01 = [
    Skill(101, '乾坤大挪移', 8000, 30),
    Skill(102, '九阳神功', 9000, 50),
    Skill(103, '九阴白骨爪', 500, 10),
    Skill(104, '黑虎掏心', 9800, 40),
    Skill(105, '葵花宝典', 6000, 2)
]


def find01():
    for item in list01:
        if item.duration > 10:
            yield item


def find02():
    for item in list01:
        if 102 <= item.id <= 105:
            yield item


def condition01(item):
    return item.duration > 10


def condition02(item):
    return 102 <= item.id <= 105


def find(func_condition):
    for item in list01:
        if func_condition(item):
            yield item


for item in find(condition01):
    print(item.name, item.duration, item.id, item.atk)
