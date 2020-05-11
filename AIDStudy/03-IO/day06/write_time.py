'''
运行程序时,写一个日志文件,格式如下

 1. Fri Aug 30 17:57:45 2019
 2. Fri Aug 30 17:57:46 2019
 3. Fri Aug 30 17:57:47 2019
 4. Fri Aug 30 17:57:48 2019
 5. Fri Aug 30 17:57:58 2019

每隔一秒写依次,每个时间占一行
当程序终止运行,重写启动的时候,序列号能够衔接
'''

import time

f = open('log.txt','a+')

f.seek(0) # 将文件偏移量放到最开始

n = len(f.readlines())

while True:
    n += 1
    time.sleep(1)
    s = '%d. %s\n' % (n, time.ctime())
    f.write(s)
    f.flush()

