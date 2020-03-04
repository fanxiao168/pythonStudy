# 在控制台输入一个字符串
# 打印 第一个字符是xx
# 打印 倒数第二个字符是xx
# 打印 前两个字符是xx
# 倒叙打印所有字符串
# 打印所有正向索引是奇数的字符
# 0 1 2 3 4 5
# 如果字符串的长度是奇数 则打印中间的字符
# 如 12345 --> 3

msg = input('请输入一个字符串:')
print('第一个字符是%s' % msg[0])
print('倒数第二个字符是%s' % msg[-2])
print('前两个字符是%s' % msg[:2])
print(msg[::-1])
# 打印所有正向索引是奇数的字符
print(msg[1::2])
count = 0
for i in msg:
    count += 1
print(count)

if len(msg) % 2 != 0:
    # 打印中间字符
    # 12345 5[2] 1234567 7[3]
    print(msg[len(msg) // 2])

length = len(msg)
if length % 2:
    # len(msg) % 2 == 1 是奇数时运行下面的代码
    print(msg[length // 2])
