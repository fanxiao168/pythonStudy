# 在控制台获取一个整数
# 如果是偶数 为变量state赋值'偶数' 否则赋值'奇数'

num = int(input('请输入一个整数:'))
if num % 2 == 1:
    state = '奇数'
else:
    state = '偶数'
print(state)

if num % 2:
    state = '奇数'
else:
    state = '偶数'
print(state)

# 条件表达式
state = '奇数' if num % 2 else '偶数'
print(state)

# 在控制台输入一个年份
# 如果闰年 给变量day赋值29
# 否则给day赋值28
year = int(input('请输入年份:'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    day = 29
else:
    day = 28
print(day)

# if num % 2 == 1:
# if num % 2:

if not year % 4 and year % 100 or not year % 400:
    day = 29
else:
    day = 28
print(day)

day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
print(day)
