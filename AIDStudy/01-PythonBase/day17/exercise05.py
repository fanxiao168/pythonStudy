# 练习：定义函数，获取列表中所有偶数。
#   要求：使用传统方法（思想：将所有满足）
#        生成器方式(yield)
#        通过调试体会惰性/延迟操作

list01 = [4, 54, 65, 6, 76, 87, 9]

# 传统方式
def get_even01():
    result = []
    for item in list01:
        if item % 2 == 0:
            result.append(item)
    return result


#  生成器方式
def get_even02():
    for item in list01:
        if item % 2 == 0:
            yield item


# re = get_even01()
re = get_even02()
for item in re:
    print(item)
