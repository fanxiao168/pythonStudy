# 在控制台录入一个四位数
# 计算每一位相加的和
# 显示结果
# 1234 --> 1+2+3+4 --> 10

num = int(input('请输入4位的整数:'))

# 方法1
# 1234 % 10 -> 123  4
ge = num % 10
# 1234 // 10 -> 123 % 10 -> 12 3
shi = num // 10 % 10
# 1234 // 100 -> 12 % 10 -> 1 2
bai = num // 100 % 10
# 1234 // 1000 -> 1
qian = num // 1000
result = ge + shi + bai + qian
print('方法一的结果是:', result)

# 方法2
result = num % 10
result += num // 10 % 10
result += num // 100 % 10
result += num // 1000
print('方法二的结果是:' + str(result))
