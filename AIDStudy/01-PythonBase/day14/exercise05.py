# 实现字符串的减法操作

# '123456' - '123' = '456'
# '123456'.replace('34','')

class Str01(str):
    def __sub__(self, other):
        return self.replace(other, "")


# str(1234)--> '1234'
s1 = Str01(123456)
s2 = Str01(123)
print(s1 - s2)
