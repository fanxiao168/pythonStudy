'''
wait.py 处理僵尸进程方法
'''

import os
from time import sleep

pid = os.fork()
if pid < 0:
    print('Error')
elif pid == 0:
    print('Child process', os.getpid())
    sleep(2)
    os._exit(3)  # 进程退出
else:
    pid, status = os.wait()  # 阻塞等待回收子进程
    print('pid:', pid)
    print('status:', os.WEXITSTATUS(status))
    while True:  # 让父进程不退出
        pass
