# 1.在控制台输入整数作为边长 打印如下
# 如果输入4
# ****
# *  *
# *  *
# ****
# 如果输入5
# *****
# *   *
# *   *
# *   *
# *****

number = int(input('请输入一个整数:'))
# 上边
print('*' * number)
# 中间
for item in range(number - 2):
    print('*%s*' % (' ' * (number - 2)))
# 下边
print('*' * number)
