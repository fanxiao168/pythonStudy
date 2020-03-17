# 读写age
class Wife:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 25 <= value < 30:
            self.__age = value
        else:
            raise ValueError('我不要！')


# 只读 (只能获取)age
class Wife01:
    def __init__(self, name):
        self.name = name
        self.__age = 25

    @property
    def age(self):
        return self.__age


w01 = Wife01('小乔')
print(w01.age)


# w01.age = 18

# 只能写age
class Wife02:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, value):
        if 25 <= value <= 30:
            self.__age = value
        else:
            raise ValueError('我不要!')

    age = property(None, set_age)


w03 = Wife02('大乔', 28)

print(w03.__dict__)
# print(w03.age) # AttributeError: unreadable attribute
# print(w03._Wife__age) # AttributeError: 'Wife02' object has no attribute '_Wife__age'
