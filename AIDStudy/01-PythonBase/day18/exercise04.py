'''
    练习：使用装饰器，为下列函数添加验证权限的功能
'''


def verif_permissions(func):
    def wrapper(*args, **kwargs):
        print('验证权限')
        return func(*args, **kwargs)

    return wrapper


@verif_permissions
def enter_background():
    print('进入后台')


@verif_permissions
def delete_order():
    print('删除订单')


enter_background()
delete_order()




