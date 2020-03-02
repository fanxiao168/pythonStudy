'''
while循环
'''

# 重复执行这段代码
# 当用户输入exit再退出
while True:
    dol = float(input('请输入美元:'))
    print(dol * 6.9)
    if input('输入exit退出,回车继续') == 'exit':
        break
