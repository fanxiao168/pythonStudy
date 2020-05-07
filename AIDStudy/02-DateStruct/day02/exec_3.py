'''
队列内容反转
'''

from squeue import *
from lstack import *

sq = SQueue()
ls = LStack()  # 用于中转数据

for i in range(15):
    sq.enqueue(i)

# 出队入栈
while not sq.is_empty():
    ls.push(sq.dequeue())

# 出栈入队
while not ls.is_empty():
    sq.enqueue(ls.pop())

while not sq.is_empty():
    print(sq.dequeue())

