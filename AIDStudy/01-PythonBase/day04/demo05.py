# 字符串通用操作

# + * += *=
# < > ...

str1 = 'this is a test string .....'
print('this' not in str1)

month = input('输入月份:')
if month in '123':
    print('春')
elif month in '456':
    print('夏')
elif month in '789':
    print('秋')
elif month in '101112':
    print('冬')
else:
    print('输入有误')

str = 'abcdef'
for ch in str:
    print(ch)

# 正向索引从0开始依次递增
print(str[0])
# 反向索引从-1开始依次递减
print(str[-1])

# 切片 切片方式参考range
print(str[0:4:1])
print(str[:4:])
print(str[:4])

print(str[:])  # 开始默认:结束默认
print(str[::2])

print(str[-1:-4:-1])
print(str[::-1])  # 反转字符串
