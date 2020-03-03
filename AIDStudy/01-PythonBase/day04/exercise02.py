# # 打印数字 0 1 2 3
# # for + range(次数) 执行预定的次数
# for i in range(4):
#     print(i)
#
# # 累加 0 1 2 3
# sum_value = 0
# for i in range(4):
#     sum_value += i
# print(sum_value)
#
# # 累加3 5 7 9
# sum_value = 0
# for i in range(3, 10, 2):
#     sum_value += i
# print(sum_value)
#
# # 输出数字4 3 2 1 0
# for i in range(4, -1, -1):
#     print(i)

# 假设一张纸0。0001米
# 折纸10次 求厚度
# 珠穆朗玛峰 8848米 求一张纸对折多少次能达到8848米

thickness = 0.0001
# for i in range(10):
#     thickness *= 2
# print(thickness)

count = 0  # 统计次数
while thickness < 8848:
    count += 1
    thickness *= 2
print('对折' + str(count) + '次,厚度为' + str(thickness) + '米')
