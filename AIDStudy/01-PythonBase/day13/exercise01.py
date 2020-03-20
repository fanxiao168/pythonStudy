# 定义Dog类  跑  叫  吃
# 定义Bird类 飞  叫  吃
# 抽象出一个父类
class Animal:
    def shout(self):
        print('叫')

    def eat(self):
        print('吃')


class Dog(Animal):
    def run(self):
        print('狂奔')


class Bird(Animal):
    def fly(self):
        print('俯冲')


animal = Animal()
bird = Bird()
dog = Dog()
# 体会 isinstance issubclass type
print(isinstance(bird, Animal))
print(isinstance(animal, Bird))
print(issubclass(Animal, Bird))
print(issubclass(Dog, Animal))
print(type(dog) == Dog)
print(type(dog) == Animal)
