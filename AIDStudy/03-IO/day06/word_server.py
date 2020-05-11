'''
使用udp完成，可客户端循环输入单词，得到单词解释，直到摁回车退出查询，可以满足同时启动多个客户端一起查询
'''

from socket import *


def find_word(word):
    # 打开文件
    f = open('dict.txt')

    for line in f:
        w = line.split(' ')[0]
        # 遍历的单词已经大于目标，说明找不到
        if w > word:
            break
        elif w == word:
            f.close()
            return line
    f.close()
    return '没有找到该单词'


# 创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

# 绑定地址
server_addr = ('127.0.0.1', 8888)
sockfd.bind(server_addr)

# 循环收发消息
while True:
    word, addr = sockfd.recvfrom(1024)
    # 得到单词解释
    data = find_word(word.decode())
    sockfd.sendto(data.encode(), addr)

# 关闭套接字
sockfd.close()
