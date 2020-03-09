# 经理: 曹操 刘备 孙权
# 技术: 曹操 刘备 关羽 张飞
# 是经理也是技术的有谁?
# 是经理不是技术的有谁?
# 不是经理 是技术的有谁?
# 张飞是经理吗?
# 总共有多少人?
# 身兼一职的有多少人?

# 字典 内嵌集合
# {
#     '经理':{xxx...}
# }

dict_persons = {
    '经理': {'曹操', '刘备', '孙权'},
    '技术': {'曹操', '刘备', '关羽', '张飞'}
}

# 是经理也是技术的有谁?
print(dict_persons['经理'] & dict_persons['技术'])
# 是经理不是技术的有谁?
print(dict_persons['经理'] - dict_persons['技术'])
# 不是经理 是技术的有谁?
print(dict_persons['技术'] - dict_persons['经理'])
# 张飞是经理吗?
print('张飞' in dict_persons['经理'])
# 总共有多少人?
print(dict_persons['经理'] | dict_persons['技术'])
print(len(dict_persons['经理'] | dict_persons['技术']))
# 身兼一职的有多少人?
print(dict_persons['经理'] ^ dict_persons['技术'])
print(len(dict_persons['经理'] ^ dict_persons['技术']))
