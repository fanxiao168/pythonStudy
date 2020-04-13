class StudentModel:
    '''
    学生模型
    '''

    def __init__(self, name='', age=0, score=0, id=0):
        '''
        创建学生对象
        :param name: 姓名 str
        :param age: 年龄 int
        :param score: 成绩 int
        :param id: 编号 该学生的唯一标示
        '''
        self.id = id
        self.name = name
        self.age = age
        self.score = score
