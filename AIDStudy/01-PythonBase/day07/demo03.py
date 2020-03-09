'''
集合的运算
交集 并集 补集
'''

# 交集
s1 = {1, 2, 3}
s2 = {2, 3, 4}
# 求s1 和 s2的交集
# 交集: 两个集合中共同的元素
s3 = s1 & s2
print(s3)  # {2, 3}

# 并集 '|'
# 返回两个集合中所有不重复的元素
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)  # {1, 2, 3, 4}

# 补集 -
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 - s2  # 属于s1但不属于s2
print(s3)  # {1}

# 补集 ^
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 ^ s2  # 等同于（s1-s2 | s2-s1）
print(s3)  # {1, 4}

s1 = {1, 2, 3}
s2 = {1, 2}
# 子集
# < 判断一个集合所有元素是否完全在另一个集合中
# 如果s1中包含了s2的全部元素 我们就把s2称为s1的子集
print(s2 < s1)  # True

# 超集 (super)
# > 判断一个集合是否包含另一个集合的所有元素
# 如果s1 包含了s2的全部元素 我们就把s1称为s2的超集
print(s1 > s2)  # True

# 相同或不相同
# 判断集合中所有元素是否和另一个集合元素相同
# ==
s1 = {1, 2, 3}
s2 = {3, 2, 1}
print(s1 == s2)  # True
print(s1 != s2)  # False

# 集合推导式
# 将0～9的数字放入集合
set_result = set()
for i in range(10):
    set_result.add(i)
print(set_result)

set_result = {i for i in range(10)}
print(set_result)

set_result = set()
for i in range(10):
    if i % 2:
        set_result.add(i)
print(set_result)
set_result = {i for i in range(10) if i % 2}
print(set_result)

# 固定集合
# 主要作用：与其他容器对象转换
s1 = frozenset(['d', 'a', 'b'])
print(s1)

s2 = frozenset(['a', 'b', 'c'])

print(s1 < s2)
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)

# 固定集合不能添加、修改、删除
# 其余运算同set
