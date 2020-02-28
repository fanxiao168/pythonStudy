# 练习：
# 在控制台输入分钟
# 再输入小时
# 再输入天
# 计算总秒数
# 总秒数 = 分*60 + 时*3600 + 天*24*3600
# 输出结果

minute = int(input('请输入分钟:'))
hour = int(input('请输入小时:'))
day = int(input('请输入天数:'))
result = minute * 60 + hour * 60 * 60 + day * 24 * 60 * 60
print('总秒数为:', result)

