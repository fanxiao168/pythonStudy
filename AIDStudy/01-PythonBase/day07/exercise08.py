# 定义计算求4位整数每位相加的和的函数
# 1234 --——> 10

def unit_sum(number):
    '''
    计算整数每位相加的结果
    :param number: 4位整数
    :return: 每位相加的和
    '''
    result = number % 10
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000
    return result


print(unit_sum(1234))
