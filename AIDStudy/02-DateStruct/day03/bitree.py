'''
bitree.py  二叉树的实现

思路分析：
1.  使用链式存储，Node表达一个节点（值，左连接，右链接）
2.  分析遍历过程
'''


# 二叉树节点
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树遍历
class Bitree:
    # 传入树根
    def __init__(self, root):
        self.root = root

    # 先序遍历
    def preOrder(self, node):
        if node is None:
            return
        print(node.val, end=' ')
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.val, end=' ')
        self.inOrder(node.right)

    # 后序遍历
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val, end=' ')

    # 层次遍历
    def levelOrder(self, node):
        import day02.lqueue
        lq = day02.lqueue.LQueue()
        # 初始节点先入队，循环判断，队列不为空则出队
        # 出队元素的左右孩子分别入队
        lq.enqueue(node)
        while not lq.is_empty():
            # 出队，打印表示遍历
            node = lq.dequeue()
            print(node.val, end=' ')
            if node.left:
                lq.enqueue(node.left)
            if node.right:
                lq.enqueue(node.right)


if __name__ == '__main__':
    # B F G D H I E C A
    # 构建一个二叉数
    b = Node('B')
    f = Node('F')
    g = Node('G')
    d = Node('D', f, g)
    h = Node('H')
    i = Node('I')
    e = Node('E', h, i)
    c = Node('C', d, e)
    a = Node('A', b, c)  # 树根

    bt = Bitree(a)

    bt.preOrder(bt.root)
    print()
    bt.inOrder(bt.root)
    print()
    bt.levelOrder(bt.root)
