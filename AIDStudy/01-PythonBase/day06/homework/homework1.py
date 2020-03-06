#  在控制台循环录入字符串 如果录入的是空字符串 退出循环
#  打印所有录入的内容

list_result = []
while True:
    str_input = input('请输入:')
    if str_input == '':
        break
    list_result.append(str_input)
list_result = '\n'.join(list_result)
print(list_result)
