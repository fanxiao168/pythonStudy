'''
str字面值
'''

name = '哪吒'
print(name)
name = "哪吒"
print(name)
# 所见即所得字符串
name = """哪吒"""
print(name)
name = """
哪
吒
"""
print(name)

str1 = '''我叫"齐'天'大圣"'''
print(str1)

# 在终端输出 C:\\newfile\\test.py
str2 = 'C:\\newfile\\test.py'
print(str2)

str3 = 'C:\newfile\test.py'
print(str3)

# 转义字符
# \"  表示 " ,  \n表示换行符， \t tab键
str4 = "我\n叫\"齐天\t大圣\""
print(str4)
print('*****************')

str3 = 'C:\newfile\test.py'
print(str3)
# 原始字符串 所有字符串都只有字面意思 没有转义
str3 = r'C:\newfile\test.py'
print(str3)
