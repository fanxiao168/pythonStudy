class CommodityModel:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class OrderModel:
    def __init__(self, commodity, count, id=0):
        self.id = id
        self.commodity = commodity
        self.count = count


class ShoppingCartController:
    __init_order_id = 0

    def __init__(self):
        self.__list_order = []
        self.__list_commodity_info = self.__load_commodity()

    @property
    def list_order(self):
        return self.__list_order

    @property
    def list_commodity_info(self):
        return self.__list_commodity_info

    def __load_commodity(self):
        '''
        加载商品信息
        :return: 商品列表
        '''

        return [
            CommodityModel(101, '倚天剑', 10000),
            CommodityModel(102, '屠龙刀', 10000),
            CommodityModel(103, '九阳神功', 10000),
            CommodityModel(104, '九阴白骨爪', 9999),
            CommodityModel(105, '乾坤大挪移', 8888),
            CommodityModel(106, '七伤拳', 7777),
        ]

    def add_order(self, order_info):
        '''
        添加订单
        :param order_info: 获取订单信息，生成id
        :return:
        '''
        order_info.id = self.__generate_order_id()
        self.__list_order.append(order_info)

    def __generate_order_id(self):
        ShoppingCartController.__init_order_id += 1
        return ShoppingCartController.__init_order_id

    def get_total_price(self):
        total_price = 0
        for item in self.__list_order:
            total_price += item.count * item.commodity.price
        return total_price

    # 获取指定的商品
    def get_commodity_by_id(self, id):
        for item in self.list_commodity_info:
            if item.id == id:
                return item


class ShoppingConsoleView:
    def __init__(self):
        self.__controller = ShoppingCartController()

    def __select_menu(self):
        while True:
            option = input('1键购买，2键结算，q键退出')
            if option == 'q':
                break
            elif option == '1':
                self.__buying()
                self.__create_order()
            elif option == '2':
                self.__settlement()

    def __buying(self):
        # 打印商品信息
        self.__print_commodity()

    def __print_commodity(self):
        for item in self.__controller.list_commodity_info:
            print('编号:%d,名称:%s,单价:%d' % (item.id, item.name, item.price))

    # 创建订单
    def __create_order(self):
        while True:
            cid = int(input('请输入商品编号:'))
            # 如果商品存在就退出 不存在就重新输入
            commodity = self.__controller.get_commodity_by_id(cid)
            if commodity:
                break
            else:
                print('商品不存在，请重新输入')

        count = int(input('请输入商品数量:'))
        order = OrderModel(commodity, count, cid)
        self.__controller.add_order(order)

    def __settlement(self):
        # 打印订单
        self.__print_order()
        # 计算总价格
        total_price = self.__controller.get_total_price()
        # 支付
        self.__pay(total_price)

    def __pay(self, total_price):
        # 接收用户输入 结算
        while True:
            money = float(input('总价%d元,请输入:' % total_price))
            if money >= total_price:
                print('购买成功,找零%.2f' % (money - total_price))
                break
            else:
                print('金额不足 请重新输入')

    def __print_order(self):
        for item in self.__controller.list_order:
            print('商品:%s,单价:%d,数量:%d' % (item.commodity.name, item.commodity.price, item.count))

    def main(self):
        # 选择菜单
        self.__select_menu()


shoppingView = ShoppingConsoleView()
shoppingView.main()
