# 随机加法考试
import random

# 随机生成两个数字
# 在控制台获取用户输入的两个数字相加的结果
# 3+2=？ 5
# 8+5=？ 3 x
# 如果用户输入正确，得分20分
# 共5道题
# 保存分数
score = 0
for i in range(5):
    random_number01 = random.randint(0, 100)
    random_number02 = random.randint(0, 100)
    # 提示字符串 3+2=？
    prompt = str(random_number01) + '+' + str(random_number02) + '=?'
    input_number = int(input(prompt))
    if input_number == random_number01 + random_number02:
        score += 20
# 最后打印得分
print('您最后的得分为' + str(score))
