'''
udp_server.py udp套接字服务端流程
重点代码
'''

from socket import *

# 创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1', 8888)
sockfd.bind(server_addr)

# 循环收发消息
while True:
    data, addr = sockfd.recvfrom(1024)
    print('Msg from %s: %s' % (addr, data.decode()))
    sockfd.sendto(b'Thanks', addr)

# 关闭套接字
sockfd.close()
