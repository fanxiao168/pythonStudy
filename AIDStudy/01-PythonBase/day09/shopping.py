shang_pin_info = {
    101: {'name': '倚天剑', 'price': 10000},
    102: {'name': '屠龙刀', 'price': 10000},
    103: {'name': '九阳神功', 'price': 10000},
    104: {'name': '九阴白骨爪', 'price': 9999},
    105: {'name': '乾坤大挪移', 'price': 8888},
    106: {'name': '七伤拳', 'price': 7777},
}

# 定义购物车清单
cart_info = []

prompt = '''**********
商品
***********
按1购买
按2结算
按q退出
***********
'''

while True:
    item = input(prompt)
    if item == 'q':
        break
    if item == '1':
        print('*' * 50)
        for key, value in shang_pin_info.items():
            print('%d         %s     %d' % (key, value['name'], value['price']))
        print('*' * 50)
        # 买东西
        # 接受用户输入的商品编号 如果编号不存在 接着输入
        while True:
            cid = int(input('请输入商品编号:'))
            if cid in shang_pin_info:
                break
            else:
                print('商品不存在，请重新输入!')
        count = int(input('请输入商品数量:'))
        # 如果商品编号正确 加入购物车
        cart_info.append({'cid': cid, 'count': count})
        print('添加购物车成功')

    elif item == '2':
        zong_jia = 0  # 计算购物车商品总价
        print('*' * 50)
        print('购物车')
        print('*' * 50)
        # 购物车清单价格 = 数量 * 商品单价
        # 商品单价需要用cid去shang_pin_info查找
        for item in cart_info:
            price = shang_pin_info[item['cid']]['price']
            print('%d   %d    %d' % (item['cid'], item['count'], item['count'] * price))
            #  购物车总价格  += 每条商品总价
            zong_jia += item['count'] * price
        print('*' * 50)

        # 告诉用户当前购物车总价
        # 接受用户输入判断是否找零
        while True:
            money = float(input('总价为%d元，请输入金额:' % zong_jia))
            # 如果money>= zongjia 找零
            # 如果money<zongjia 重新输入
            if money >= zong_jia:
                print('购买成功，找零%.2f' % (money - zong_jia))
                # 清空购物车清单
                cart_info.clear()
                break
            else:
                print('金额不足，请重新输入')
