class Person:
    def __init__(self, name):
        self.name = name

    def say(self):
        print('说话')


class Student(Person):
    # 子类若没有构造函数 使用父类的
    pass


class Teacher(Person):
    # 若子类有构造函数 会覆盖父类的构造函数
    # 要想使用父类的构造函数中的属性
    # 必须调用父类构造函数
    def __init__(self, age, name):
        super().__init__(name)
        self.age = age


s01 = Student('zs')
s01.say()
t01 = Teacher(29, 'ls')
print(t01.age)
print(t01.name)
