'''
buffer.py
缓冲区演示
'''

# f = open('test','w',1) # 行缓冲
f = open('test', 'w')

while True:
    data = input('>>')
    if not data:
        break
    f.write(data + '\n')
    f.flush()  # 主动刷新缓冲

f.close()
