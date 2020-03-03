# 在控制台输入长和宽 求矩形的周长和面积
# 打印格式如下
# 矩形的长为xx 宽为xx 周长是xx 面积是 xxx
unit1 = int(input('请输入矩形的长'))
unit2 = int(input('请输入矩形的宽'))

length = (unit1 + unit2) * 2
area = unit1 * unit2
print('矩形的长为%d 宽为%d 周长是%d 面积是%d' % (unit1, unit2, length, area))
