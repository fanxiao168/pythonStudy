'''
squeue.py  队列的顺序存储

思路分析：
1. 基于列表完成数据的存储
2. 通过封装功能完成队列的基本行为
3. 无论哪边做队头/队尾  都会在操作中有内存移动
'''


# 自定义异常
class QueueError(Exception):
    pass


# 队列操作
class SQueue:
    def __init__(self):
        self._elems = []

    # 判断队列是否为空
    def is_empty(self):
        return self._elems == []

    # 入栈
    def enqueue(self, val):
        self._elems.append(val)

    # 出栈
    def dequeue(self):
        if not self._elems:
            raise QueueError('Queue is empty')
        return self._elems.pop(0)  # 弹出第一个数据


if __name__ == '__main__':
    sq = SQueue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while not sq.is_empty():
        print(sq.dequeue())
