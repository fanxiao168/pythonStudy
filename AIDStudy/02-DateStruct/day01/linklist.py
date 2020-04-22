'''
linklist.py
功能：使用节点作为数据元素的生成器，对数据元素之间的关系进行构建和操作
重点代码
'''


# 创建节点类
class Node:
    '''
    包含一个简单的数字作为数据
    next 构建关系
    '''

    def __init__(self, val, next=None):
        self.val = val  # 有用的数据
        self.next = next  # 节点关系


'''
1.构建节点间关系
2.在节点中存储数据
3.对但链表进行节点操作
'''


# 但链表的类
class LinkList:
    '''
    思路：生成对象即表示一个单链表对象
         对象调用方法可以完成对单链表的各种操作
    '''

    def __init__(self):
        '''
        初始化时 创建一个无用的节点，让对象拥有该节点，以表达链表的开端
        '''
        self.head = Node(None)

    # 初始化
    def init_list(self, iter):
        p = self.head
        for i in iter:
            p.next = Node(i)
            p = p.next

    # 遍历打印
    def show(self):
        p = self.head.next  # 第一个有效节点
        while p is not None:
            print(p.val)
            p = p.next  # p 向后移动

    # 判断链表是否为空
    def is_empty(self):
        return self.head.next is None

    # 清空链表
    def clear(self):
        self.head.next = None

    # 尾部插入
    def append(self, val):
        p = self.head
        # p 移动到最后一个节点
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 头部插入
    def head_instert(self, val):
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    # 指定位置插入
    def insert(self, index, val):
        p = self.head
        # 将p移动到待插入位置的前一个
        for i in range(index):
            # 超出最大范围
            if p.next is None:
                break
            p = p.next

        node = Node(val)
        node.next = p.next
        p.next = node

    # 删除节点（删除第一个val值）
    def delete(self, val):
        p = self.head
        # 确定p的位置（停留在待删除节点的前一个）
        while p.next and p.next.val != val:
            p = p.next

        # 分情况讨论
        if p.next is None:
            raise ValueError("x is not link")
        else:
            p.next = p.next.next

    # 获取节点值
    def get_value(self, index):
        if index < 0:
            raise IndexError('link index out of range')
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError('link index out of range')
            p = p.next
        return p.val


if __name__ == '__main__':
    link = LinkList()
    link.init_list(range(5))
    link.show()
    # link.append(5)
    # link.show()
    # link.head_instert(9)
    # link.show()
    # link.insert(2,10)
    # link.show()
    # link.delete(8)
    # link.show()
    # print(link.get_value(5))

    # node1 = Node(1)
    # link.head.next = node1
    #
    # node2 = Node(2)
    # node1.next = node2
    #
    # node3 = Node(3)
    # node2.next = node3
    #
