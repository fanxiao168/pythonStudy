# 练习：
# 在控制台 录入一个商品单价 input()
# 再录入一个数量 input()
# 最后获取金额 输入100 input()
# 计算应找零多少钱 print()

# 如：
# 请输入商品单价: 10
# 请输入商品数量: 2
# 找零: 80

price = input('请输入商品的单价:')
price = float(price)
count = int(input('请输入商品的数量:'))
money = float(input('请输入金额:'))
result = money - price * count
print('找零:', result)
