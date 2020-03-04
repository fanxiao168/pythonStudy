# 定义列表 存储八大行星
# 水 金 地 火 木 土 天王 海王
# 打印 距离太阳最近的行星是xx
# 打印 距离太阳最远的行星是xx
# 打印 太阳到地球之间的行星
# 打印 八大行星（一行一个）
# 倒叙打印 八大行星（一行一个）

list_planets = ['水星', '金星', '地球', '火星', '木星', '土星', '天王星', '海王星']
print('距离太阳最近的行星是%s' % list_planets[0])
print('距离太阳最远的行星是%s' % list_planets[-1])
print('太阳到地球之间的行星%s' % list_planets[0:2])
for item in list_planets:
    print(item)

# 倒叙获取所有行星
for item in list_planets[::-1]:
    print(item)

# ['水星','金星','地球','火星','木星','土星','天王星','海王星']
#   0    1      2     3      4       5    6
#   7
#   7~-1
# 建议通过索引 在原列表直接查找对应位置的值
for item in range(len(list_planets) - 1, -1, -1):
    print(list_planets[item])
