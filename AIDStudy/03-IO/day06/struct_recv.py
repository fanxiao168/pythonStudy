'''
udp完成，从客户端输入学生信息，循环录入
    学号:
    姓名: 不会超过16字节
    年龄:
    分数: 保留一位小数

    将信息发送给服务端，在服务端写入到一个文件里,
    每个学生信息占一行
'''

from socket import *
import struct

# 与客户端格式一致
st = struct.Struct('i16sif')

# udp套接字
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))

# 打开一个保存信息的文件
f = open('student.txt', 'a')

while True:
    data, addr = s.recvfrom(1024)
    # (1,b'Lily',14,94.5)
    data = st.unpack(data)

    # 写入文件
    info = '%d %-10s %d %.1f\n' % data
    f.write(info)
    f.flush()

f.close()
s.close()
