# 定义老婆类
# __init__ name
# 创建3个老婆对象
# 用类变量统计老婆对象的数量
# 定义一个类方法 打印老婆数量
# 画图

class Wife:
    # 定义类变量 统计数量
    count = 0

    # 定义类方法 打印数量
    @classmethod
    def print_count(cls):
        print(cls.count)

    def __init__(self, name):
        self.name = name
        Wife.count += 1


w01 = Wife('大乔')
w01 = Wife('小乔')
w01 = Wife('貂蝉')
Wife.print_count()
