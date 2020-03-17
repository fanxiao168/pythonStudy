'''
封装
'''


# 数据角度：wife(名字，身高，体重) Student(姓名，年龄，成绩)
# {姓名:[年龄，成绩]}

class Wife:
    def __init__(self, name, age):
        self.name = name
        # 私有成员:以双下划线开头
        # self.__age = age
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 25 <= value <= 30:
            self.__age = value
        else:
            # 抛出异常
            raise ValueError("我不要！")


w01 = Wife('甄宓', 25)
# 不能访问私有变量
# print(w01.__age)
# w01.set_age(25)
print(w01.get_age())
