'''
udp_client.py udp 客户端
'''

from socket import *

# 服务器地址
ADDR = ('127.0.0.1',8888)

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环收发消息
while True:
    data = input("Msg>>")
    if not data:   # 退出
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)
    print("From server:",msg.decode())

sockfd.close()

