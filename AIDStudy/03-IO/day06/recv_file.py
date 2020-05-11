'''
接受一个文件
思路: 接收文件内容，将其写入到一个文件里
'''

from socket import *

s = socket()
s.bind(('127.0.0.1', 8888))
s.listen(3)

c, addr = s.accept()
print("Connect from", addr)

# 打开文件
f = open('mm.jpg', 'wb')

# 循环接收内容，写入文件
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()
