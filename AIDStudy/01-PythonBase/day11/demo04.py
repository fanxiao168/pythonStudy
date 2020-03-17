'''
封装
'''


# 数据角度：Wife(名字，身高，体重) Student(姓名，年龄，成绩)
# {姓名:[年龄，成绩]}
# 创建敌人类 (名字 血量0-100 攻击力1-50)

class Wife:
    def __init__(self, name, age):
        self.name = name
        # 私有成员: 以双下划线开头
        # self.__age = age
        # self.set_age(age)
        self.age = age

    @property  # 拦截读取 age = property(get_age,None)
    def age(self):
        return self.__age

    # 设置写入方法age.setter(写入方法)
    @age.setter  # 拦截写入
    def age(self, value):
        if 25 <= value <= 30:
            self.__age = value
        else:
            # 抛出异常
            raise ValueError('我不要！')

    # property 拦截对age对读写操作
    # age = property(get_age,set_age)


w01 = Wife('甄宓', 25)
# 不能访问私有变量
# print(w01.__age)
# w01.set_age(25)
# print(w01.get_age())
print(w01.age)
print(w01.__dict__)
print(w01._Wife__age)
