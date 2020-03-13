# 创建Student类
# __init__
# name  age  score
# print_self
# 输出  name  age   score

class Student:
    def __init__(self, name, score, age):
        self.name = name
        self.age = age
        self.score = score

    def print_self(self):
        print(self.name, self.age, self.score)


# 创建一个列表 在列表中保存3条学生记录
# stu01 = Student('无忌',80,28)
# stu01.name

list01 = [
    Student('无忌', 80, 28),
    Student('赵敏', 99, 26),
    Student('芷若', 48, 24)
]


# 定义一个函数 查找赵敏同学
def find01(name):
    for item in list01:
        if item.name == name:
            return item


# 输出赵敏同学的成绩
stu01 = find01('敏敏')
# stu01 = None
# None.score
if stu01:
    print(stu01.score)


# 定义函数 查找所有年龄在30岁以下的学生
# 30岁以下的学生应该不止有一个
# 考虑到用容器保存查询到的学生  返回容器
def find02():
    result = []
    for item in list01:
        if item.age < 30:
            result.append(item)
    return result


list_result = find02()
for item in list_result:
    print(item.name)


# 删除所有不及格的学生
def delete01():
    for i in range(len(list01) - 1, -1, -1):
        if list01[i].score < 60:
            del list01[i]


delete01()
for item in list01:
    print(item.name)
