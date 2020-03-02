# 在控制台输入一个月份 打印对于的天数
# 1 3 5 7 8 10 12  --> 31天
# 4 6 9 11 ---->30天
# 2 ------> 28天
# 其他 提示输入有误

while True:
    month = int(input('请输入月份:'))
    if month < 1 or month > 12:
        print('输入有误')
        break
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print('30天')
    elif month == 2:
        print('28天')
    else:
        print('31天')
