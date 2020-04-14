from demo06 import AgeError


class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 23 <= value <= 30:
            self.__age = value
        else:
            raise AgeError('我不要', '23<=value<=30', 101)


try:
    w01 = Wife(20)
    print(w01.age)
except AgeError as e:
    print(e.id)
    print(e.message, e.code)
