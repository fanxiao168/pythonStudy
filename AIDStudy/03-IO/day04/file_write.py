'''
file_write.py
文件写操作演示
'''

f = open('text','w')
# f = open('text','ab')

# 写操作
# f.write(b'hello,diegui\n') # 如果希望换行则自己添加
# f.write('哎呀，干啥'.encode())

# 写入列表内容
l = ['hello world \n','哈哈哈\n']
f.writelines(l)

f.close()

