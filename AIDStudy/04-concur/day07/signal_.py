# signal 信号方法处理僵尸进程

import os
import signal

# 信号处理僵尸
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 处理子进程
pid = os.fork()
if pid < 0:
    print('Create process failed')
elif pid == 0:
    # 子进程执行部分
    print('Child process:', os.getpid())
else:
    # 父进程执行部分
    print('Process process')
    while True:
        pass
