# 定义一个将序列所有元素打印到终端的功能
# 如 list01 = [1,2,3,4]
# 1 2 3 4
# str = 'abcd'
# 'a' 'b' 'c' 'd'

def print_target(target):
    for item in target:
        print(item, end=' ')


list01 = [1, 2, 3, 4]
print_target(list01)
str01 = 'abcd'
print_target(str01)

# print(print_target(str01))
