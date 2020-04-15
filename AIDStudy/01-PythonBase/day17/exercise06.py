# 练习：定义函数，获取列表中大于10的数字。
#    要求：使用传统方式/生成器方式
#          通过调试体会惰性/延迟操作


list01 = [4, 54, 65, 6, 76, 87, 9]


# 传统方式
def get_even01():
    result = []
    for item in list01:
        if item > 10:
            result.append(item)
    return result


#  生成器方式
def get_even02():
    for item in list01:
        if item > 10:
            yield item


# re = get_even01()
re = get_even02()
for item in re:
    print(item)
