# 1.在控制台获取一个字符串
# 打印这个字符串的每一个字符的编码值
# 字--->数  ord('a')
# 数--->字  chr(97)
str = input('请输入文字:')
for ch in str:
    print(ord(ch))

# 2.在控制台重复录入编码值 将编码值转为字符打印
# 如果录入的是空字符串 则退出程序
while True:
    str2 = input('请输入编码值:')
    if str2 == '':
        break
    code_value = int(str2)
    print(chr(code_value))
