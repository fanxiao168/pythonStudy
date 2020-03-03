'''
字符串格式化
'''

student = '麦奇'
number = 1
age = 18
print('第' + str(number) + '位同学的姓名为' + student + ',年龄为' + str(age))
print('第%d位同学的姓名为%s,年龄为%d' % (number, student, age))

name = '哪吒'
age = 3
score = 99.9

print('我叫:%s,年龄%d岁,成绩为%.2f' % (name, age, score))
