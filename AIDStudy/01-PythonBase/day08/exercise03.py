# 定义一个函数myprint 统计该函数调用的次数
count = 0
def myprint():
    # 如果在函数内部直接修改全局变量 程序会认为创建新的局部变量
    # 需要先声明再赋值
    global count # 将count声明为全局变量
    count += 1
    print(count)

myprint()
myprint()
myprint()
myprint()