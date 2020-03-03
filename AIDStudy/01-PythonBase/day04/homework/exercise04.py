# 在控制台获取一个整数
# 判断是否素数
# 素数：只能被1和自身整除的数
# 1 （2 3 4 5 6 7 8）9
# 1 (2 3 4 5 6) 7
# 判断11 从2～10之间的数字能不能整除
# if 11 % 2 == 0:
#     print('11不是素数')
# if 11 % 3 == 0:
#     print('11不是素数')
# if 11 % 4 == 0:
#     print('11不是素数')
# if 11 % 5 == 0:
#     print('11不是素数')
# ....

number = int(input('请输入一个整数:'))
for i in range(2, number):
    if number % i == 0:
        print(str(number) + '不是素数')
        # 如果发现满足条件的数字 就不用在判断后面的数字的
        break
else:
    print(str(number) + '是素数')
