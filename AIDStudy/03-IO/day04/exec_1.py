'''
从终端输入一个单词，从单词本中找到该单词，打印这一行内容，如果没有找到则打印'找不到'
'''

word = input('单词:')

# 打开文件
f = open('dict.txt')

for line in f:
    w = line.split(' ')[0]
    # 遍历的单词已经大于目标，说明找不到了
    if w > word:
        print('没有找到该单词')
        break
    elif w == word:
        print(line)
        break

else:
    print('没有找到该单词')

f.close()
