'''
就是一个数n的阶乘
'''


# def recursion(n):
#     resule = 1
#     for i in range(1, n + 1):
#         resule *= i
#     return resule


# 递归函数
def recursion(n):
    # 递归的终止条件
    if n <= 1:
        return 1
    return n * recursion(n - 1)


print(recursion(3))
