# 6.打印1000以内所有的"水仙花数"
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153 = 1的三次方 + 5的三次方 + 3的三次方

# 方法一
for i in range(100, 1000):
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100
    if (ge ** 3 + shi ** 3 + bai ** 3) == i:
        print(str(i) + '是水仙花数')

print('--------------------')

# 方法二
for bai in range(1, 10):
    for shi in range(0, 10):
        for ge in range(0, 10):
            i = ge + shi * 10 + bai * 100
            if (ge ** 3 + shi ** 3 + bai ** 3) == i:
                print(str(i) + '是水仙花数')

print('--------------------')

# 方法三
#  1     2     3
# 百位   十位  个位
# 123 ->'123'  int('1')**3 + int('2')**3 + int('3')**3
for i in range(100, 1000):
    # 记录每一位数字的立方累加值 默认为0
    sum_number = 0
    # 将数字转换为字符串 遍历获取每一个字符
    for ch in str(i):
        # 将每一位字符再转为数字 将立方值累加到sum_number
        sum_number += int(ch) ** 3
    # 当循环结束后sum_number保存的就是各个位的累加和
    # 判断
    if sum_number == i:
        print(str(i) + '是水仙花数')
