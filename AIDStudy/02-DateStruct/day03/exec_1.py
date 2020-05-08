'''
编写一个接口程序，去判断一段文字中括号的匹配是否正确，如果正确则告知
如果不正确则需要提示大概第多少个字符出现了匹配不正确的情况

思路: 左括号入栈，遇到右括号弹栈进行匹配
    出错情况：不匹配，缺少左括号，缺少右括号
'''

from day02.sstack import *

text = """Open source (software) [is] made better when {users} can easily (contribute) code and documentation to fix bugs and add features. ([Python] strongly) encourages community {involvement in (improving) the software}. Learn more about how to make Python better for everyone."""

# 将验证条件提前定义
parens = "()[]{}"
left_parens = "([{"
opposite = {')': '(', ']': '[', '}': '{'}  # 配对字典

st = SStack()  # 用于存储做括号


# 提供括号
def paren(text):
    # i: 字符串索引
    i, text_len = 0, len(text)

    # 遍历字符串
    while True:
        while i < text_len and text[i] not in parens:
            i += 1

        if i >= text_len:
            return
        else:
            yield text[i], i
            i += 1


# 只负责验证括号匹配情况
def ver():
    for pr, i in paren(text):
        if pr in left_parens:
            st.push((pr, i))  # 左括号入栈
        elif st.is_empty() or st.pop()[0] != opposite[pr]:
            print("在%d位置，没有匹配到'%s'字符" % (i, pr))
            break

    else:
        if st.is_empty():
            print('所有括号正确')
        else:
            pr, i = st.pop()
            print("在%d位置，没有匹配到'%s'字符" % (i, pr))
ver()

# def ver(text):
#     n = 0
#     for i in text:
#         if i in parens:
#             if i in left_parens:
#                 # 遇到左括号入栈
#                 st.push((i,n))
#             elif st.is_empty():
#                 # 右括号多了
#                 print("Error in",n)
#                 return
#             else:
#                 # 匹配错了
#                 val = st.pop()
#                 if val[0] != opposite[i]:
#                     print("Error in",val[1])
#                     return
#         n += 1
#
#     if st.is_empty():
#         print("OK")
#     else:
#         # 左括号多了
#         val = st.pop()
#         print("Error in",val[1])
#
#
# ver(text)
