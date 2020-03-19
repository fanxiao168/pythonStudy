# 复习
# 封装
# 数据角度
#       将多个变量包装成一个对象
#       学生（姓名，年龄，成绩）
#       dict01 = {'name':name,'age':age}
#       dict01['name']
#       stu01.name
#       优点：
#          代码书写/可读性比容器更好
#          更符合人的思想
# 行为角度
#       向类外提供必要的信息  屏蔽/隐藏实现细节
#       如：
#             str01 = '你好'
#       str 类 （）
#       私有成员: __开头
# 设计角度

## 老张开车去东北

# 为孩子买一个玩具LittlePony
# 玩具有尺寸（little middle large）
# 有颜色（white pink yellow）
# 玩具能唱歌（lalala)
# 玩具能说话（hello my name is LittlePony)

class LittlePony:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        # 组合
        self.vendor = Vendor()

    def sing(self):
        print('lalala')

    def speak(self):
        print('hello my name is LittlePony')


# 玩具还有生产厂家属性
# 生产厂家有邮箱 email
#          电话 phone
#          地址 address
# 这时需要将数据封装到类中
# 生产厂家还能查询真伪 call (打电话)
class Vendor:
    def __init__(self, email='littlepony@tedu.cn', phone='400-123-8989', address='北京天坛'):
        self.email = email
        self.phone = phone
        self.address = address

    def call(self):
        print('给%s打电话' % self.phone)


myLittlePony = LittlePony('middle', 'pink')
myLittlePony.speak()
myLittlePony.sing()
myLittlePony.vendor.call()
