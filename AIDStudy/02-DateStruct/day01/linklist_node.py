# 创建一个节点类用于存储数据和维护关系
class Node:
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        # ....
        self.next = None

    def fun(self):
        pass


node1 = Node(name='张三', age=18)
node1.hobby = 'baddkkdkd'

node2 = Node(name='李四', age=16)
node1.next = node2
