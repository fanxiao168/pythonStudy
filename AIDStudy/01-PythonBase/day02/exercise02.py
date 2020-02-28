# 练习2
# 在控制台获取两个变量
# 然后交换数据
# 最后显示结果

# 获取值 input()
data01 = input('请输入第一个变量:')
data02 = input('请输入第二个变量:')

# 处理过程
# 所有语言通用思想
# temp = data01
# data01 = data02
# data02 = temp
# 变量一的值等于变量二的值，变量二的值等于变量一的值
data01, data02 = data02, data01
# 显示值 print()
print('第一个变量是:', data01)
print('第二个变量是:', data02)
