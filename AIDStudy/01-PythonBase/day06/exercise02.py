# 获取用户输入的年份和月份 打印这个月份有多少天
# 使用容器的思想取处理代码
year = int(input('请输入年份:'))
month = int(input('请输入月份:'))
if month < 1 or month > 12:
    print('月份输入错误')
elif month == 2:
    # 平年28 闰年29
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('29天')
    else:
        print('28天')
elif month == 4 or month == 6 or month == 9 or month == 11:
    print('30天')
else:
    print('31天')

# 1.判断条件 多个条件时 考虑用容器保存所有可能的结果 然后在判断
if month < 1 or month > 12:
    print('月份输入错误')
elif month == 2:
    # 平年28 闰年29
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('29天')
    else:
        print('28天')
elif month in (4, 6, 9, 11):
    print('30天')
else:
    print('31天')

# 2.当结果值确定时，考虑将结果保存到容器中，然后根据条件取容器中取对应结果
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('29天')
# else:
#     print('28天')
if month < 1 or month > 12:
    print('月份输入错误')
else:
    month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    days_of_month = (31, month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(str(days_of_month[month - 1]) + '天')
