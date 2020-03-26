class Vector1:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector1(self.x + other)

    def __sub__(self, other):
        return Vector1(self.x - other)

    def __str__(self):
        return str(self.x)

    def __radd__(self, other):
        return Vector1(self.x + other)

    def __iadd__(self, other):
        self.x += other
        return self


v01 = Vector1(10)
print(v01 + 2)
print(2 + v01)
# v01 +=2
# v01 = v01 + 2
# 默认使用 __add__ 一般会产生新对象
# 重写__iadd__ 实现在原对象基础上变化值
v01 += 2
print(v01, id(v01))
v03 = Vector1(10)
# print(v03 * 2)  # 报错 TypeError: unsupported operand type(s) for *: 'Vector1' and 'int'
