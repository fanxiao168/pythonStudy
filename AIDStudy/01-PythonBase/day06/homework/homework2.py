# 斐波那契数列
fibs = [0, 1]
# [0,1,1]
# [0,1,1,2]
# [0,1,1,2,3,5,8,11....]
first = fibs[0]
sencond = fibs[1]
for i in range(13):
    result = first + sencond
    fibs.append(result)
    first = sencond
    sencond = result
print(fibs)

fibs = [0, 1]
for i in range(13):
    fibs.append(fibs[-1] + fibs[-2])
print(fibs)
