# 练习
# 古代称一斤16两    33两   2斤1两
# 在控制台获取两 input()
# 计算 斤 和 两
# 输出几斤几两 print()

weight = int(input('请输入总两:'))
jin = weight // 16
liang = weight % 16
print(str(jin) + '斤零' + str(liang) + '两')
