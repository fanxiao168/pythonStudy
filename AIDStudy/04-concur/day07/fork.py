'''
fork.py  fork进程演示1
'''

import os
from time import sleep

# 创建子进程

pid = os.fork()
if pid < 0:
    print('Create process failed')
elif pid == 0:
    # 子进程执行部分
    sleep(3)
    print('The new process')
else:
    # 父进程执行部分
    sleep(2)
    print('The old process')

print('Fork test over')  # 父子进程都执行