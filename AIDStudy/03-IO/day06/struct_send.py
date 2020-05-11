import struct
from socket import *

# 设置数据结构
st = struct.Struct('i16sif')

# 创建udp套接字
s = socket(AF_INET, SOCK_DGRAM)
ADDR = ('127.0.0.1', 8888)

while True:
    print('=============')
    id = int(input('学号:'))
    name = input("姓名:").encode()
    age = int(input('年龄:'))
    score = float(input('得分:'))
    # 将数据打包
    data = st.pack(id, name, age, score)
    s.sendto(data, ADDR)  # 发送给服务端

s.close()
