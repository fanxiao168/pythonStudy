import time

# 获取当前时间戳 从1970年1月1日到现在的总秒数
print(time.time())  # 1586849933.3404648
# 获取当前的时间元组
# (年  月  日 时 分  秒  一周的第几天（0 1，2...）一年的第几天 夏令营时)
print(time.localtime())
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=14, tm_hour=15, tm_min=38, tm_sec=53, tm_wday=1, tm_yday=105, tm_isdst=0)
# 获取指定时间戳的时间元组
print(time.localtime(123456789))
# time.struct_time(tm_year=1973, tm_mon=11, tm_mday=30, tm_hour=5, tm_min=33, tm_sec=9, tm_wday=4, tm_yday=334, tm_isdst=0)

time_tuple = time.localtime()
# 将时间元组变成时间戳
print(time.mktime(time_tuple))  # 1586850175.0

# 将时间元组转换成时间字符串
print(time.strftime('%y/%m/%d %H:%M:%S', time_tuple))  # 20/04/14 15:45:22
print(time.strftime('%Y-%m-%d %H:%M:%S', time_tuple))  # 2020-04-14 15:45:22

# 将日期字符串转换为时间元组
print(time.strptime('19/08/21 11:31:30', '%y/%m/%d %H:%M:%S'))
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=21, tm_hour=11, tm_min=31, tm_sec=30, tm_wday=2, tm_yday=233, tm_isdst=-1)
print(time.strptime('2019/08/21 11:31:30', '%Y/%m/%d %H:%M:%S'))
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=21, tm_hour=11, tm_min=31, tm_sec=30, tm_wday=2, tm_yday=233, tm_isdst=-1)


print('开始运行')
time.sleep(5)
print('程序结束')
