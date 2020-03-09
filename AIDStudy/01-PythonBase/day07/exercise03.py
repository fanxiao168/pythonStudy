# 在控制台绘制图形
# 四行五列
# 索引是偶数行输出 *
# 索引是技术行输出 #

# *****   0
# #####   1
# *****   2
# #####   3

for c in range(4):
    for i in range(5):
        if c % 2 == 0:
            print('*', end='')
        else:
            print('#', end='')
    print()
