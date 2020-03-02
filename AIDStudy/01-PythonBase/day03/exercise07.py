# 重复执行exercise01.py代码 直到按e键退出
# 死循环 条件永远满足
while True:
    season = input('请输入季度:')
    if season == '春':
        print('1月2月3月')
    elif season == '夏':
        print('4月5月6月')
    elif season == '秋':
        print('7月8月9月')
    elif season == '冬':
        print('10月11月12月')
    else:
        print('输入不合法')

    if input('输入e退出,回车继续') == 'e':
        break
