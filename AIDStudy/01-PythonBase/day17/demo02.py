'''
    迭代器 ---> yield
    练习：exercise04.py

    目标：让自定义类所创建的对象，可以参与for.
    iter价值：可以被for
    next价值：返回数据/抛出异常

    class  自定义类的迭代器：
        def __next__(self):
            pass

    class  自定义类:
        def __iter__(self):
            pass
    for item in  自定义类():
        pass
'''


class SkillIterator:
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
        # return SkillIterator(self.__skills)

        # 执行过程：
        # 1. 调用__iter__()不执行
        # 2. 调用__next__()才执行当前代码
        # 3. 执行到yield语句暂时离开
        # 4. 再次调用__next__()继续执行
        # ....

        # yield作用: 标记着下列代码会自动转换为迭代器代码。
        # 转换大致过程：
        # 1. 将yield关键字以前的代码，放到next方法中
        # 2. 将yield关键字后面的数据，作为next返回值

        # print('准备数据:')
        # yield '降龙十八掌'
        #
        # print('准备数据:')
        # yield '黑虎掏心'
        #
        # print('准备数据:')
        # yield '六脉神剑'

        for item in self.__skills:
            yield item


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
