# 输入一个数字
# 再输入一个运算符 + - * /
# 最后输入另外一个数字
# 根据运算符计算两个数字
# 要求 如果运算符 不是加减乘除 提示运算符有误

num1 = float(input('请输入第一个数:'))
op = input('请输入运算符:')
num2 = float(input('请输入第二个数:'))
# 判断 如果用户输入的内容是+
if op == '+':
    print(num1 + num1)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print('运算符有误')
