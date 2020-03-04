list01 = ['三丰', '翠山', '无忌']
# 把list01中存储的地址赋值给list02
list02 = list01
list01[0] = '张三丰'
print(list02[0])  # 张三丰

list01 = [800, 900, 1000]
list02 = list01
list03 = list01
list01[0] = '八百'
print(list02[0])  # 八百
list03 = '九百'
print(list02[0])  # 八百

list01 = [800, 900, 1000]
list02 = list01[:]
list01[0] = '八百'
print(list02[0])  # 800

list01 = [800, 900, 1000]
list02 = list01
list01[1:2] = ['a', 'b']
print(list02)  # ?[800,'a','b',1000] 为什么1000后移

list01 = [100, [200, 300]]
list02 = list01
# list01[1] = [200,300]
# [200,300][0] = 200
list01[1][0] = 500
print(list02)  # [100, [500, 300]]

list01 = [100, [200, 300]]
list02 = list01.copy()  # 浅拷贝
list01[1][0] = 500
print(list02[1][0])  # 500

list01 = [1000, 2000, 3000]
list02 = [1000, 2000, 3000]
print(list01 == list02)  # 比较的是值是否相等
print(list01 is list02)  # 比较的是地址id(list01)==id(list02)

import copy

# 深拷贝 划清界限 拷贝前的对象和拷贝后的对象互不影响
# 注意：深拷贝可能回占用大量内存
list01 = [100, [200, 300]]
list02 = copy.deepcopy(list01)
list01[1][0] = 500
print(list01)
print(list02)
