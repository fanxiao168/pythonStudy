'''
发送一个文件
思路: 循环读取文件内容，发送
'''

from socket import *

s = socket()
s.connect(('127.0.0.1', 8888))

f = open('timg.jpeg', 'rb')
while True:
    # 边读 边发
    data = f.read(1024)
    if not data:  # 文件结尾
        break
    s.send(data)

f.close()
s.close()
