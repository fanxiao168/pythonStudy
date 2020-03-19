# 张无忌  教   赵敏   乾坤大挪移
# 赵敏  教  张无忌   化妆
# 张无忌  上班  挣了  10000
# 赵敏  上班   挣了   6000

class Person:
    def __init__(self, name=None):
        self.name = name

    def teach(self, other, skill):
        print(self.name, '教', other, skill)

    def work(self, money):
        print(self.name, '上班赚了', money)


zwj = Person('张无忌')
zm = Person('赵敏')
zwj.teach(zm.name, '乾坤大挪移')
zm.teach(zwj.name, '化妆')
zwj.work(10000)
zm.work(6000)
