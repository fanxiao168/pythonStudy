# 定义函数 根据年月日计算星期几
# 时间元组
import time


def get_week(year, month, day):
    time_tuple = time.strptime('%d/%d/%d' % (year, month, day), '%Y/%m/%d')
    week_tuple = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日')
    return week_tuple[time_tuple[6]]


# 定义函数 根据生日 计算活了多少天
# 当前时间 - 出生日期
def life_days(birthday):
    time_tuple = time.strptime(birthday, '%Y/%m/%d')
    # 生活的总秒数 = 当前时间戳 - 出生时的时间戳
    life_second = time.time() - time.mktime(time_tuple)
    return life_second / 60 / 60 // 24


if __name__ == '__main__':
    print(get_week(2019, 8, 21))
    print(life_days('2000/01/01'))
