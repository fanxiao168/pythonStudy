# 在控制台循环录入字符串
# 如果输入空字符串 停止
# 打印所有不重复的字符串

set_result = set()
while True:
    str_input = input('请输入:')
    if str_input == '':
        break
    set_result.add(str_input)

for item in set_result:
    print(item)