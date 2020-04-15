'''
    生成器表达式
    练习：exercise09.py
'''

list01 = [34, 4, 'a', 'b', 1.5, 1.8, True, False]


# 生成器函数：为其他人提供功能
def find01():
    for item in list01:
        if type(item) == str:
            yield item


re = find01()
for item in re:
    print(item)

# 生成器表达式：为自己提供功能
re = (item for item in list01 if type(item) == str)
for item in re:
    print(item)
