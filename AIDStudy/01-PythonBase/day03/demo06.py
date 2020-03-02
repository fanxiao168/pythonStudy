'''
if语句的真值表达式
'''

# if 100:
#     # if bool(100):
#     print('真值为True')
#
# if '':
#     print('yes')
# else:
#     print('no')
#
# name = input('请输入用户名:')
# if name:
#     # 说明用户有输入内容
#     print(name)
# else:
#     # 说明用户没有输入内容
#     print('用户没有输入')
#
# gender = None
# if input('请输入性别:') == '男':
#     gender = 1
# else:
#     gender = 0
#
# if gender:
#     print(name + '先生,你好！')
# else:
#     print(name + '女士,你好！')


# 性别为1 如果输入的值为'男' 否则为0
gender = 1 if input('请输入性别:') == '男' else 0
print(gender)
