# 定义与员工管理器
# 管理所有的员工
# 计算所有员工的工资

class EmployeeManager:
    def __init__(self):
        self.__list_emp = []

    def add_emp(self, emp):
        self.__list_emp.append(emp)

    def calc_total_salary(self):
        tatal_salary = 0
        for item in self.__list_emp:
            tatal_salary += item.calc_salary()
        return tatal_salary


class Employee:
    def __init__(self, base_salary=0):
        self.base_salary = base_salary

    def calc_salary(self):
        pass


# 员工:
# 程序员  底薪 + 项目分红
# 销售    底薪 + 销售额*0.05
# .......
# 体会 封装  继承  多态
# 体会 开闭  单一  依赖倒置
class Programmer(Employee):
    def __init__(self, base_salary=0, bonus=0):
        super().__init__(base_salary)
        self.bonus = bonus

    def calc_salary(self):
        return self.base_salary + self.bonus


class Salesman(Employee):
    def __init__(self, base_salary=0, sale_value=0):
        super().__init__(base_salary)
        self.sale_value = sale_value

    def calc_salary(self):
        return self.base_salary + self.sale_value * 0.05


manager = EmployeeManager()
manager.add_emp(Programmer(20000, 500))
manager.add_emp(Salesman(6000, 10000))
print(manager.calc_total_salary())
