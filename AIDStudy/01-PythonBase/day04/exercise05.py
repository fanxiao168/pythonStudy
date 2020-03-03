# 累加10～50之间的个位不是3 6 9的数字
# 10+11+12+14+15+17+18+20

# 获取所有10～50的数字
# 获取数字的个位 如果是3 6 9 跳过
# 如果不是 累加
# 输出结果

sum_number = 0
for i in range(10, 51):
    unit = i % 10
    # 如果是3 6 9 跳过
    if unit == 3 or unit == 6 or unit == 9:
        continue
    sum_number += i
print(sum_number)

n = 10
sum_number = 0
while n < 51:
    unit = n % 10
    # 如果是3 6 9
    if unit == 3 or unit == 6 or unit == 9:
        n += 1
        continue
    sum_number += n
    n += 1

print(sum_number)

# 次数未知           while循环
# 次数已知/有确切数据  for循环
