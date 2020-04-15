'''
    要求：自行推理迭代器逻辑
    题目：迭代员工管理器
    class EmployeeManager:
        pass

    manager = EmployeeManager()
    manager.add_employee('无忌')
    manager.add_employee('翠山')
    manager.add_employee('三丰')

    for item in manager:
        print(item)
'''


class EmployeeIterator:
    '''
        迭代器
    '''

    def __init__(self, data):
        self.__target = data
        self.__index = -1

    def __next__(self):
        # 如果没有数据则抛出异常
        if self.__index >= len(self.__target) - 1:
            raise StopIteration
        # 返回数据
        self.__index += 1
        return self.__target[self.__index]


class EmployeeManager:
    '''
        员工管理器   可迭代对象
    '''

    def __init__(self):
        self.__employee = []

    def add_graphic(self, str_name):
        self.__employee.append(str_name)

    def __iter__(self):
        return EmployeeIterator(self.__employee)


manager = EmployeeManager()
manager.add_graphic('无忌')
manager.add_graphic('翠山')
manager.add_graphic('三丰')

for item in manager:
    print(item)
