# 继承
# 财产：钱不用自己挣  但是可以花
# 王位：江山不用自己打 但可以坐
# 代码：功能不是自己写的 但是可以直接用

# 多个子类在概念上一致时 考虑抽象出一个父类
# 多个子类中共性提取到父类中
# 从设计角度：继承先有子类 再有父类
# 从编码角度：先有父类  再有子类

class Persion:
    def say(self):
        print('balabala')


class Student(Persion):
    def study(self):
        print('学习')


class Teacher(Persion):
    def teach(self):
        print('上课')


stu01 = Student()
# 子类可以直接调用父类成员
stu01.say()

p01 = Persion()
p01.say()
# 父类不能调用子类成员
# p01.study()

t01 = Teacher()

# python内置函数
# isinstance()判断对象是否属于一个类
# 老师对象是不是属于老师类型
print(isinstance(t01, Teacher))
# 老师对象是不是属于人类型
print(isinstance(t01, Persion))
# 老师对象是不是属于学生类型
print(isinstance(t01, Student))

# issubclass() 判断一个类是不是另一个类的子类
print(issubclass(Teacher, Persion))
print(issubclass(Teacher, Student))
print(issubclass(Persion, Teacher))
