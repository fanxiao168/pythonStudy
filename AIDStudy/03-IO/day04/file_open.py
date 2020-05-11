'''
file_open.py
文件打开方式训练
'''

# 打开文件

try:
    '''
    文本文件既可以使用文本方式打开，也能使用二进制方式打开
    二进制文件如果使用文本方式打开，读写时会报错
    '''
    # f = open('text.py','r') # 只读方式
    # f = open('text.py','w') # 只写方式
    f = open('text.py','a') # 追加方式

except Exception as e:
    print(e)

# 读写文件

# 关闭文件
f.close()
