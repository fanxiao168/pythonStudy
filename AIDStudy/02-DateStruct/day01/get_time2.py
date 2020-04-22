import time

from linklist import *

# 0     time: 1.2159347534179688e-05
# 10000 time: 0.0012907981872558594

link = LinkList()
link.init_list(range(1000000))

st = time.time()
link.insert(10000,'007')
print('time:',time.time() - st)
