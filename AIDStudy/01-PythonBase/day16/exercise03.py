# 定义敌人类  限定攻击力范围0～100之间
# 如果超出范围 在属性中抛出异常
# 传递错误消息（错误编码，错误代码，提示信息）
class AtkSetError(Exception):
    def __init__(self, id, code, message):
        self.id = id
        self.code = code
        self.message = message


class Enemy:
    def __init__(self, name, atk):
        self.atk = atk
        self.name = name

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise AtkSetError(101, '0<=value<=100', '攻击力不在范围内')


if __name__ == '__main__':
    try:
        mb = Enemy('灭霸', -10)
    except AtkSetError as e:
        print(e.id, e.code, e.message)
