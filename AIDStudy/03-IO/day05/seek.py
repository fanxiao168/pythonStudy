'''
seek.py  文件偏移量

注意： 1. open 打开文件会重置文件偏移量
      2. 读写操作使用的是一个偏移量值
      3. seek操作文件偏移量一般是以二进制打开
'''

f = open('text','wb+')

f.write(b'Hello world')
# f.close()
#
# f = open('test','r')

print('偏移量:',f.tell())  # 获取文件偏移量

f.seek(-5,2)  # 将文件偏移量定位到开头

data = f.read()
print(data)

f.close()

