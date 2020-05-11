'''
套接字属性介绍
'''

from socket import *

s = socket()

# 设置端口立即重用
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.bind(('10.1.3.54', 8989))
s.listen(3)
c, addr = s.accept()
print('地址类型:', s.family)
print('套接字类型:', s.type)
print('绑定地址:', s.getsockname())
print('文件描述符', s.fileno())

# 使用链接套接字调用
print('获取连接端的地址', c.getpeername())

c.recv(1024)
