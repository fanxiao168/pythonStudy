# 在控制台获取学生姓名 （循环输入 一个一个录入）
# 将输入结果保存到列表
# 如果输入的是空字符串 则停止录入
# 打印所有学生姓名

# 空列表 保存数据
name_list = []
while True:
    name = input('请输入姓名:')
    if name == '':
        break
    name_list.append(name)
# 打印列表的每一个元素
print(name_list)
