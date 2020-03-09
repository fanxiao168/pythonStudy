# 定义在终端打印矩形的函数
# 要求函数调用者提供行数 列数 和填充字符
# 3  3  *
# ***
# ***
# ***

# 先完成功能代码
row = int(input('请输入行数:'))
col = int(input('请输入列数:'))
char = input('请输入填充字符:')
for r in range(row):
    for c in range(col):
        print(char, end=' ')
    print()


# 再将功能代码变成函数
def print_rect(row, col, char):
    for r in range(row):
        for c in range(col):
            print(char, end=' ')
        print()


print_rect(3, 5, '*')
