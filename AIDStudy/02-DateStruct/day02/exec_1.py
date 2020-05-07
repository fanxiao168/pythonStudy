from day01.linklist import *

l1 = LinkList()
l2 = LinkList()

l1.init_list([1, 5, 7, 8, 10, 12, 13, 19])
l2.init_list([0, 3, 4, 8, 9])


# 将l2合并到l1当中
def merge(l1, l2):
    p = l1.head
    q = l2.head.next
    while p.next is not None and q is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            p = p.next
            q = tmp
    if p.next is None:
        p.next = q  # 将最后剩余的连接上


merge(l1, l2)
l1.show()
