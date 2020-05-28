'''
fork1.py  fork进程演示示例
'''

import os
from time import sleep

print('=================')
a = 1

pid = os.fork()
print('pid:', pid)
if pid < 0:
    print('Error')
elif pid == 0:
    print('Child process')
    print('a = ', a)  # 从父进程空间获取的a
    a = 10000  # 修改自己空间的a
else:
    sleep(1)
    print('Parent process')
    print('a:', a)

print('all a =', a)  # 父子进程都执行
