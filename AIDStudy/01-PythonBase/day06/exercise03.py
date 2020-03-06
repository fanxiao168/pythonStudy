# 获取用户输入的年份和月份、和日期
# 计算这是一年的第几天
# 2019年3月10日 31+28+10
year = int(input('请输入年份:'))
month = int(input('请输入月份:'))
day = int(input('请输入日期:'))

if month < 1 or month > 12:
    print('月份输入错误')
else:
    month02 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    day_of_month = (31, month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    print(day_of_month[month - 1])

    # 先累加前几个月的天数
    # 再累加当月的天数
    # 方法一:
    total_day = 0
    for i in range(month - 1):
        total_day += day_of_month[i]
    total_day += day
    print(total_day)

    # 方法二:
    # 使用sum函数 获取day_of_month中索引值从0到月份-1的所有值的和
    total_day = 0
    total_day = sum(day_of_month[:month - 1])
    total_day += day
    print(total_day)
