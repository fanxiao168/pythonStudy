g01 = "悟空"
g02 = "八戒"


def fun01():
    num1 = 100
    print(num1)

    g02 = "老朱"
    print(g02)

    global g03
    g03 = '老沙'
    print(g03)

    # 先定义了局部变量
    # 再声明全局变量 有歧义
    # 3.6版本后报错
    # global g02   #SyntaxError: name 'g02' is used prior to global declaration
    # g02 = '猪八戒'
    # print(g02)


fun01()
print(g03)
print(g02)


def fun02():
    a = 10

    def inner_fun():
        # a = 2
        nonlocal a
        a += 1
        print(a)

    inner_fun()
    print(a)


fun02()


def user_info():
    user_name = 'shibw'
    user_age = 20
    user_email = 'shibw@tedu.com'
    gender = '男'
    address = '北京市东城区'
    # return (user_name,user_age,user_email,gender,address)
    # return user_age
    # return {
    #     'user_name':user_name,'user_age':user_age,'gender':gender,'address':address
    # }
    # locals() 收集当前的局部变量 保存到字典
    return locals()


# 获取到返回的元组
print(user_info())
inofs = user_info()
# 输出详细信息
print('姓名:%s,年龄:%s,邮箱:%s,性别:%s,地址:%s' % (
inofs['user_name'], inofs['user_age'], inofs['user_email'], inofs['gender'], inofs['address']))
