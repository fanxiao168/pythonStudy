class StudentModel:
    def __init__(self, name='', age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id

    # 对象-->字符串（格式随意）
    def __str__(self):
        return '编号:%d,姓名:%s' % (self.id, self.name)

    # 对象--->字符串（解释器可识别的，有格式要求）
    def __repr__(self):
        return "StudentModel('%s',%d,%d,%d)" % (self.name, self.age, self.score, self.id)


s01 = StudentModel('zhangsan', 19, 100, 1000)
print(s01)
str01 = str(s01)
print(str01)

# 将字符串当做一句代码去执行
# eval() 只能执行一行表达式
print(eval("1+2*5"))
# eval('del s01') # 报错 SyntaxError: invalid syntax

# 将字符串当做一块代码去执行
# 用换行符或分号 分隔每一个语句
str02 = '''a = 10
b = 10
print(a+b)
'''
exec(str02)
exec("a=11\nb=20;print(a+b)")

# 克隆对象
s01 = StudentModel('哪吒', 3000, 59, 1)
print(repr(s01))
# repr 返回Python格式的字符串
# eval 执行字符串
s02 = eval(repr(s01))
print(s02)
s02.name = '小李'
print(s01)
print(s02)
