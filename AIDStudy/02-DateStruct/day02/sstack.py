'''
sstack.py  栈模型的顺序存储
重点代码

思路：
1. 利用列表完成存储，但是列表功能多，不符合栈模型特点
2. 使用类将列表封装，提供符合栈特点的接口方法
'''


#  自定义异常
class StackError(Exception):
    pass


# 顺序栈模型
class SStack:
    def __init__(self):
        # 开辟一个顺序存储的模型空间
        # 列表的尾部表示栈顶
        self._elems = []

    # 判断栈是否为空
    def is_empty(self):
        return self._elems == []

    # 入栈
    def push(self, val):
        self._elems.append(val)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError('Stack is empty')
        # 弹出一个值并返回
        return self._elems.pop()

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError('Stack is empty')
        return self._elems[-1]


if __name__ == '__main__':
    st = SStack()
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
