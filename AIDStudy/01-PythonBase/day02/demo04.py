"""
    数据类型转换
"""

# 接受用户的输入
str_dol = input('请输入美元:')
# 处理业务逻辑
# 将str_dol转换为整形
# int()只能转换数字类型的字符串
int_dol = int(str_dol)

# 整数和浮点数运算 结果会自动转为浮点数
result = int_dol * 6.9  # 10*6.9 = 69.0
# 显示结果
str_result = str(result)
print('转换人民币的结果是:' + str_result)

# 任意数据类型转换为布尔类型时
# 如果有值就为True 没有值就为False
# 字符串中包含空白字符 True
print(bool(' '))
print(bool(''))  # 空字符串 False
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(None))  # False
