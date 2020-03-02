'''
规定次数的循环
'''

count = 0
totalMoney = 0
while count < 3:
    dol = float(input('请输入美元:'))
    print(str(dol * 6.9) + '人民币')
    count += 1
    totalMoney += dol*6.9

print('总金额为' + str(totalMoney) + '人民币')
