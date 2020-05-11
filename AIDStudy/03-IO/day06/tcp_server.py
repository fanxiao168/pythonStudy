'''
tcp_server.py  tcp套接字服务端流程
重点代码

注意: 功能性代码，注重流程和函数使用
'''

import socket

# 创建套接字对象
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('0.0.0.0',9999))

# 设置监听
sockfd.listen(5)

# 等待处理客户端连接请求
while True:
    print('Waiting for connect...')
    try:
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        # ctrl-c 退出程序
        print("Server exit")
        break
    except Exception as e:
        print(e)
        continue

    # 消息收发
    while True:
        data = connfd.recv(1024)
        # 如果data为空意味着客户端断开
        if not data:
            break
        print("Receive:",data.decode())
        if data == b'Q':
            break
        n = connfd.send(b'Thanks')
        print('Send %d bytes' % n)
    connfd.close()

# 关闭套接字
sockfd.close()

