'''
    迭代器
    练习：exercise01.py
         exercise02.py
         exercise03.py
'''


class SkillIterator:
    '''
        迭代器
    '''

    def __init__(self, data):
        self.__target = data
        self.__index = -1

    def __next__(self):
        # 如果没有数据则抛出异常
        if self.__index >= len(self.__target) - 1:
            raise StopIteration
        # 返回数据
        self.__index += 1
        return self.__target[self.__index]


class SkillManager:
    '''
        技能管理器  可迭代对象
    '''

    def __init__(self):
        self.__skills = []

    def add_skill(self, str_skill):
        self.__skills.append(str_skill)

    def __iter__(self):
        return SkillIterator(self.__skills)


manager = SkillManager()
manager.add_skill('降龙十八掌')
manager.add_skill('黑虎掏心')
manager.add_skill('六脉神剑')

# 错误：manager必须是可迭代对象__iter__()
for item in manager:
    print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
