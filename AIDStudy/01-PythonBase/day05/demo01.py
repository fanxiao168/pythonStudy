'''
内建函数
'''

str1 = '123456'
print(len(str1))  # 长度
print(max(str1))  # 最大值
print(min(str1))  # 最小值

# 求和
# print(sum(str1))  # 字符串里面的字符不能直接相加
list1 = []
for ch in str1:
    list1.append((int(ch)))
print(sum(list1))

