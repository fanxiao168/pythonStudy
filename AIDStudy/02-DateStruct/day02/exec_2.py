'''
逆波兰表达式练习
'''

from sstack import *

st = SStack()

while True:
    exp = input()
    tmp = exp.split(' ')
    for i in tmp:
        if i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x+y)
        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x-y)
        elif i == '*':
            y = st.pop()
            x = st.pop()
            st.push(x*y)
        elif i == '/':
            y = st.pop()
            x = st.pop()
            st.push(x/y)
        elif i == 'p':
            print(st.top()) # 查看栈顶元素
        else:
            st.push(int(i))


