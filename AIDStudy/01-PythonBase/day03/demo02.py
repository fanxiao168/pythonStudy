'''
身份运算符
'''

a = 800
b = 1000
# id函数 获取变量储存对象的地址
print(id(a))
print(id(b))

# is运算本质时通过id函数进行判断的
print(a is b)

c = a
print(id(c))
print(c is a)

d = 1000
print(b is d)

e = 10
f = 10
print(id(e))
print(id(f))
print(e is f)
f = 12
print(id(e))
print(id(f))
print(e is f)