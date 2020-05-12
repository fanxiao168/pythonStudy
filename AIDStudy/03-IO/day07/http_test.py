'''
http请求响应演示
'''

from socket import *

# tcp 服务器
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) # 端口立即重用
s.bind(('127.0.0.1',8000))
s.listen()

c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096).decode()
print(data)   # http请求

html = '''HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello World</h1>
'''

c.send(html.encode())
c.close()
s.close()

