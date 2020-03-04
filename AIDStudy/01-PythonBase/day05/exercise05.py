# 在控制台获取所有学生的成绩（循环 一个一个录入）
# 如果录入空字符串 停止
# 输出最高分 最低分 和平均分

scores_list = []
while True:
    str_score = input('请输入成绩:')
    if str_score == '':
        break
    score = int(str_score)
    scores_list.append(score)
print(max(scores_list))
print(min(scores_list))
print(sum(scores_list)/len(scores_list))
