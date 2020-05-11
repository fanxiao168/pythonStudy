'''
tcp_server.py  tcp套接字服务器流程
重点代码

注意：功能性代码，注重流程和函数使用
'''

import socket

# 创建tcp套接字对象
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0', 9999))

# 设置监听
sockfd.listen(5)

# 等待处理客户端连接请求
print("waiting for connect....")
connfd, addr = sockfd.accept()
print('Connect from', addr)

# 消息收发
data = connfd.recv(1024)
print('Receive:', data.decode())
n = connfd.send(b'Thanks')
print('Send %d bytes' % n)

# 关闭套接字
connfd.close()
sockfd.close()
