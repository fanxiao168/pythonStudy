import random

# 生成随机整数
r01 = random.randint(1, 100)
print(r01)

# 随机取数组中的一个
r02 = random.choice([1, 2, 3])
print(r02)

# 随机排序
r03 = [1, 2, 3]
random.shuffle(r03)
print(r03)
