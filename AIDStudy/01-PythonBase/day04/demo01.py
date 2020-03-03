'''
for循环
用来遍历可迭代对象的数据元素。
range函数
range(开始，结束，间隔）
开始默认为0
间隔默认为1
取值范围从开始到结束 不包含结束的值
'''

# for 变量列表 in 可迭代对象:
#     语句
# else:
#     语句

# str 属于 可迭代对象
str = '我是小妖精，逍遥又自在'
# item 储存的是每个字符的地址
for item in str:
    print(item)

# 查看断点调试
# 打印数字0～9
str2 = '0123456789'
for i in str2:
    print(i)

# 打印数字10～15
str3 = '101112131415'
# 10 ~ (15-1)
for i in range(10, 16):
    print(i)
