# 2. 计算一个字符串的字符以及字符出现的次数
# 输入 this is a test string
# t:4 h:1 i:3 s:4 a:1 e:1 r:1 n:1 g:1
# 思路
# 判断字符出现的次数
# 如果统计过 次数加1 如果没有统计过则等于1
# setdefult()

str_target = 'this is a test string'
dic_result = {}

for ch in str_target:
    # # 判断字符是否为字典中的键
    # if ch not in dic_result:
    #     # 如果不是 在字典中添加键值对
    #     dic_result[ch] = 1
    # else:
    #     dic_result[ch] = dic_result[ch] + 1

    # 判断字符是否为字典中的键 如果不是添加键值对
    # 如果是 将值加1
    dic_result.setdefault(ch, 0)
    dic_result[ch] += 1
print(dic_result)
