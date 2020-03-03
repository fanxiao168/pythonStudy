# 1.在控制台获取输入的月份 显示对于的季度 或提示月份错误
month = int(input('请输入月份:'))

if month < 1 or month > 12:
    print('月份错误')
elif month < 4:
    print('春季')
elif month < 7:
    print('夏季')
elif month < 10:
    print('秋季')
else:
    print('冬季')
