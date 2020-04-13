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
        # StudentManagerController.__stu_id += 1
        stu.id = self.__generate_id()
        # 将学生添加到学生列表
        self.__stu_list.append(stu)

    def __generate_id(self):
        StudentManagerController.__stu_id += 1
        return StudentManagerController.__stu_id

    # 删除学生remove_student
    # 根据id删除学生
    # 删除后返回结果 成功True/失败False

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
        return False

    def update_student(self, stu):
        for item in self.__stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        return False

    # 了解清楚学生管理系统的运行流程
    # 根据成绩排序
    # 考虑如何重构shopping.py(提高)

    # 根据成绩排序order_by_score
    # 你是谁 你要找谁
    def order_by_score(self):
        for i in range(len(self.__stu_list) - 1):
            for c in range(i + 1, len(self.__stu_list)):
                if self.__stu_list[i].score > self.stu_list[c].score:
                    self.__stu_list[i], self.stu_list[c] = self.stu_list[c], self.__stu_list[i]
