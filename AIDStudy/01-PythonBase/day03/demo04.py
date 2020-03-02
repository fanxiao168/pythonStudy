# 练习：当钱不够时提示金额不足
# 钱够时 提示应找回xx

# 输入商品的单价
price = float(input('请输入商品单价:'))
# 输入数量
count = int(input('请输入商品数量:'))
# 输入金额
money = float(input('请输入金额:'))
# 增加判断逻辑
# res计算结果 如果不大于0 说明钱不够用 提示
res = money - price * count
if res>=0:
    # 大于0要执行的
    result = '应找回:' + str(res)
else:
    # 不大于0要执行的
    result = '金额不足'

# 输出结果
print(result)