# 定义函数 在控制台接受用户输入的成绩
# 如果出现异常就继续输入直到正确为止
def get_score():
    while True:
        try:
            score = int(input('请输入成绩'))
            return score
        except:
            print('输入有误')


if __name__ == '__main__':
    print(get_score())
