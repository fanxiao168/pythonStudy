"""
    核心数据类型
"""

# 1.None
name = 'shibw'
# 解除变量与数据的绑定
name = None
print(name)
# 使用None占位
stu_name = None

# 2.整形 int
# 十进制  0 ~ 9
num1 = 10
# 二进制 0  1
# 百   十   个
#     1   0   0b11   0b100  0b1000
# 1    0   0
print(0b10)
# 八进制  0 ~ 7
# 百   十   个
#     1   0   0b11   0b100
#     1   1
# 1   1   1
print(0o10)
# 十六进制  0 ~ 9  a(10) ~ f(15)
# 百   十   个
#     1   0   0b11   0b100
# 1   0   0
print(0x10)

# 3.浮点数
print(1.5)
print(3.0)
print(3.)  # 不建议使用
print(0.14)
print(.14)  # 不建议使用
# 科学计数法 用来明确表示过小或过大的值
# e 表示指数  乘 10 的几次方
print(1.23e10)
print(1.23e-25)

# 4.字符串
print('hello world')
print("hello world")
# 他说:"今天有雨,出门记得带伞"
print('他说:"今天有雨,出门记得带伞"')
print(""" 第一行
    这是三个双引号的字符串
    第三行""")

# 5.复数
# 由实部和虚部两部分组成
print(0 + 1j)
print(1j)
print(1 + 1j)
print(1 - 1j)
