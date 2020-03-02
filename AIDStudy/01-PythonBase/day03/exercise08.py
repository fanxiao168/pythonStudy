# 在控制台输出0 1 2 3 4 5
count = 0
while count < 6:
    print(count)
    count += 1
print('---------------')

# 在控制台输出2 3 4 5 6 7
count = 2
while count < 8:
    print(count)
    count += 1
print('---------------')

# 在控制台输出0 2 4 6 8
count = 0
while count <= 8:
    print(count)
    count += 2
print('---------------')


# 在控制台输出 1～20之间的偶数
# 循环找到1～20的数字
# 判断 如果是偶数就输出
count = 1
while count < 21:
    if count % 2 == 0:
        print(count)
    count += 1