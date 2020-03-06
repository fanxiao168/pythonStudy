# 在控制台录入人的信息(姓名、年龄、性别、体重)
# 如果名称为空字符串 停止
# 数据结构
# [
#     {'name':'shibw','age':20,'gender':'男','weight':80}
#     {.....}
# ]

list_info = []
while True:
    name = input('请输入姓名:')
    if name == '':
        break
    age = int(input('请输入年龄:'))
    gender = input('请输入性别:')
    weight = float(input('请输入体重:'))
    # 创建保存用户信息的字典
    dict_info = {'name': name, 'age': age, 'gender': gender, 'weight': weight}
    # 将字典添加到列表
    list_info.append(dict_info)
print(list_info)
# 获取列表中的每条数据
for dict_item in list_info:
    # 列表的每条数据都是字典 通过字典的键查找
    print('%s的年龄是%d,性别是%s,体重是%.1f' % (dict_item['name'], dict_item['age'], dict_item['gender'], dict_item['weight']))
