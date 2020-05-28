"""
编写一个http服务端程序
     如果浏览器的请求内容 /
     响应码为  200  OK,将index.html内容作为响应内容

     如果浏览器的请求是其他的
     响应码为  404  Not Found  内容为 "Sorry.."
"""

 from socket import *


 # 与客户端交互
 def handle(connfd):
     # 获取http请求
     data = connfd.recv(4096).decode()
     request_line = data.split('\n')[0]  # 请求行
     info = request_line.splict(' ')[1]  # 请求内容

     # 看一下请求内容是不是/
     if info == '/':
         with open('index.html') as f:
             # 组织http响应
             response = 'HTTP/1.1 200 OK\r\n'
             response += 'Content-Type:text/html\r\n'
             response += '\r\n'
             response += f.read()
     else:
         response = 'HTTP/1.1 404 Not Found\r\n'
         response += 'Content-Type:text/html\r\n'
         response += '\r\n'
         response += '<h1>Sorry...</h1>'

     # 发送给浏览器
     connfd.send(response.encode())


 # 搭建网络
 def main():
     sockfd = socket()
     sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
     sockfd.bind(('0.0.0.0', 8000))
     sockfd.listen(3)
     while True:
         connfd, addr = sockfd.accept()
         print("Connect from", addr)
         # 处理客户端请求
         handle(connfd)


 main()
