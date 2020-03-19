# student_manager_system
# 第一步:
# 数据模型类：StudentModel
# 逻辑控制类: StudentManagerController
#   数据：学生列表  __stu_list
#   行为：获取列表  stu_list,
#        添加学生  add_student
#        添加id    整数   递增    类变量

class StudentModel:
    '''
    学生模型
    '''

    # id 不需要传值 放在最后一位
    def __init__(self, name='', age=0, score=0, id=0):
        '''
        创建学生对象
        :param name: 姓名 str
        :param age: 年龄  int
        :param score: 成绩  int
        :param id: 编号  该学生的唯一标示
        '''

        self.id = id
        self.name = name
        self.age = age
        self.score = score


class StudentManagerController:
    '''
    学生管理控制器 处理业务逻辑
    '''
    __stu_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        # 为学生设置id 递增
        # StudentManagerController.__stu_id +=1
        # stu.id = StudentManagerController.__stu_id
        stu.id = self.__generate_id()
        self.__stu_list.append(stu)

    # 生成id
    def __generate_id(self):
        StudentManagerController.__stu_id += 1
        return StudentManagerController.__stu_id

    # 删除学生 remove_student
    # 根据id删除学生
    # 删除后返回结果  成功True/失败False
    def remove_student(self, id):
        '''
        根据编号删除学生
        :param id: 编号
        :return: 删除的结果
        '''
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
        raise ValueError('删除失败：id错误')

    # 修改学生update_student
    # s01 = StudentModel('zs',18,50)
    # s01 = StudentModel('zs',19,40,1001)

    def update_student(self, stu):
        for item in self.__stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        raise ValueError('未找到对应的学员!')

    # 了解清楚学生管理系统的运行流程
    # 根据成绩排序
    # 考虑如何重构shopping.py(提高)


# 测试添加学员
# manager = StudentManagerController()
# s01 = StudentModel('zm',18,50)
# manager.add_student(s01)
# # manager.stu_list列表 保存学生对象
# print(manager.stu_list[0].name)

# 测试删除学员
# manager = StudentManagerController()
# s01 = StudentModel('zd',18,90)
# s02 = StudentModel('ls',19,80)
# manager.add_student(s01)
# manager.add_student(s02)
# for item in manager.stu_list:
#     print(item.id,item.name)
# # print(manager.remove_student(1005))
# print(manager.remove_student(1001))
# print({item.id:item.name for item in manager.stu_list})

# 测试修改学员
manager = StudentManagerController()
s01 = StudentModel('zs', 18, 50)
manager.add_student(s01)
manager.update_student(StudentModel('张三', 19, 40, 1001))
print({(item.id, item.name, item.age) for item in manager.stu_list})
