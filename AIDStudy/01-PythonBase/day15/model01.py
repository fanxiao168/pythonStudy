'''
第一个模块
'''


# import demo02

def fun01():
    print('模块1的fun01')


class MyClass:
    def fun02(self):
        print('MyClass -- fun02')


# main + tab
# 判断是否在主模块运行
# __name__当程序在主模块（自己运行时）值为 "__main__"
# 当程序作为模块被调用时，值为模块名
if __name__ == '__main__':
    print('模块1')
    fun01()
    print(__name__)
    # 查看文档字符串
    print(__doc__)
    # 查看文件的路径
    print(__file__)
