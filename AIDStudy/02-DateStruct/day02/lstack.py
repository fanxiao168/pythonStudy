'''
lstack.py 栈的链式结构
重点代码

思路：
1.源于节点存储数据，建立节点关联
2.封装方法 入栈  出栈  栈空  栈顶元素
3.链表的开头作为栈顶（不需要每次遍历）
'''


# 自定义异常
class StackError(Exception):
    pass


# 创建节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 节点关系


# 链式栈
class LStack:
    def __init__(self):
        # 标记顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self, val):
        self._top = Node(val, self._top)

    def pop(self):
        if self._top is None:
            raise StackError('Stack is empty')
        value = self._top.val
        self._top = self._top.next
        return value

    def top(self):
        if self._top is None:
            raise StackError('Stack is empty')
        return self._top.val


if __name__ == '__main__':
    ls = LStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    while not ls.is_empty():
        print(ls.pop())
