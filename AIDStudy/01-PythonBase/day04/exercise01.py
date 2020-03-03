# 猜数字
# 导入随机模块
import random

# 产生一个从1到100之间的随机数
random_number = random.randint(1, 100)
print(random_number)

"""
# 用户输入一个数字 电脑随机生成一个数字
# 判断用户输入的数字和电脑随机生成的数字是否相同
# 如果相同 提示猜对了
# 如果输入的大 提示猜大了
# 否则 提示猜小了

input_number = int(input('请输入1～100的数字:'))
if input_number == random_number:
    print('猜对了')
elif input_number > random_number:
    print('猜大了')
else:
    print('猜小了')

# 1.重复执行以上代码 直到猜对为止
# 2.重复执行三次代码
# 如果用户猜对了，提示:"猜对了，总共猜了xx次"
# 如果用户三次没有猜对，提示用户 "你输了，正确的数字是xx"

# 1.重复执行以上代码 直到猜对为止
while True:
    input_number = int(input('请输入1～100的数字:'))
    if input_number == random_number:
        print('猜对了')
        break
    elif input_number > random_number:
        print('猜大了')
    else:
        print('猜小了')

# 2.重复执行三次代码
# 如果用户猜对了，提示:"猜对了，总共猜了xx次"
# 如果用户三次没有猜对，提示用户 "你输了，正确的数字是xx"
"""
count = 0
while count < 3:  # 0 1 2
    count += 1
    input_number = int(input('请输入1～100的数字:'))
    if input_number == random_number:
        print('猜对了，总共猜了' + str(count) + '次')
        break
    elif input_number > random_number:
        print('猜大了')
    else:
        print('猜小了')
else:
    print('你输了，正确的数字是' + str(random_number))
