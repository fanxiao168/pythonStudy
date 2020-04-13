from project.student_system.bill import StudentManagerController

from project.student_system.model import StudentModel


class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print('+---------------------+')
        print('| 1)添加学生信息        |')
        print('| 2)显示学生信息        |')
        print('| 3)删除学生信息        |')
        print('| 4)修改学生信息        |')
        print('| 5)按照成绩升序排序     |')
        print('+---------------------+')

    def __select_menu(self):
        option = input('请输入:')
        if option == '1':
            self.__input_students()
        elif option == '2':
            self.__output_students(self.__manager.stu_list)
        elif option == '3':
            self.__delete_student()
        elif option == '4':
            self.__modify_student()
        elif option == '5':
            self.__output_student_by_score()

    def main(self):
        '''
        界面入口
        :return:
        '''

        while True:
            self.__display_menu()
            self.__select_menu()

    # 输入学生 __input_students
    def __input_students(self):
        # 收集学生信息
        # 要求输入 姓名 年龄  成绩
        # 创建学生对象（姓名 年龄  成绩）
        # 去控制器找add_student方法
        name = input('请输入学生姓名:')
        age = int(input('请输入学生年龄:'))
        score = int(input('请输入学生成绩:'))
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    # 输出学生__output_students
    def __output_students(self, list):
        for item in list:
            print(item.name, item.age, item.score, item.id)

    # 删除学生__delete_student
    def __delete_student(self):
        # 需要用户输入学生id
        # 调用管理器对象的删除学生方法
        # 如果结果为True 显示删除成功
        # 否则显示删除失败
        id = int(input('请输入要删除学生的编号:'))
        if self.__manager.remove_student(id):
            print('删除成功')
        else:
            print('删除失败')

    # 修改学生信息 __modify_student
    def __modify_student(self):
        # 收集用户输入的信息保存到对象
        # 调用管理器的修改学生的方法
        id = int(input('请输入要修改学生的编号:'))
        name = input('请输入新的学生姓名:')
        age = int(input('请输入新的学生年龄:'))
        score = int(input('请输入新的学生成绩:'))
        stu = StudentModel(name, age, score, id)
        if self.__manager.update_student(stu):
            print('修改成功')
        else:
            print('修改失败')

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)
