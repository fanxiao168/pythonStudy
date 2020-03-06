# 在控制台输入商品信息（名称和单价）
# 如果名称为空 停止输入
# 将商品的名称与单价打印在控制台
# 如果录入了"游戏机"  单独打印 游戏机的价格是xxx

dict_info = {}
while True:
    name = input('请输入商品的名称:')
    if name == '':
        break
    price = float(input('请输入商品价格:'))
    dict_info[name] = price
for key,value in dict_info.items():
    print('%s的单价为%.1f' % (key,value))
if '游戏机' in dict_info:
    print('游戏机的价格是%.1f' % dict_info['游戏机'])

