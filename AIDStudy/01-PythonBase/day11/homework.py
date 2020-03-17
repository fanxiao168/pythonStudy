# 定义敌人类
# 数据  姓名  血量  法力  基础攻击   防御力
# 行为  打印数据信息

class Enemy:
    def __init__(self, name, hp, mp=None, atk=None, defense=None):
        self.name = name
        # enemy['name']
        # Alt+Enter  Create P..
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.defense = defense

    def print_self_info(self):
        print(self.name, self.hp, self.mp, self.atk, self.defense)


# 创建敌人列表（至少4个元素） 画出内存图
enemy_list = [
    # name hp   mp  atk   defense
    Enemy('玄冥二老', 86, 80, 120, 5),
    Enemy('成昆', 0, 0, 150, 20),
    Enemy('谢逊', 120, 50, 150, 30),
    Enemy('灭霸', 0, 0, 999, 888),
]


# 查找叫'灭霸'的敌人 打印信息
def find01():
    for item in enemy_list:
        if item.name == '灭霸':
            return item
    return None


e01 = find01()
if e01:
    e01.print_self_info()


# 查找所有死亡的敌人
def find02():
    list_result = []
    for item in enemy_list:
        if item.hp == 0:
            list_result.append(item)
    return list_result


res = find02()
# res列表中保存的是对象的地址
for item in res:
    print(item.name)


# 计算所有敌人的平均攻击力
def calc():
    sum_atk = 0
    for item in enemy_list:
        sum_atk += item.atk
    return sum_atk / len(enemy_list)


print(calc())


# 删除防御力小于10的敌人
def delete():
    for i in range(len(enemy_list) - 1, -1, -1):
        if enemy_list[i].defense < 10:
            del enemy_list[i]


delete()

for item in enemy_list:
    print(item.name)


# 将所有敌人攻击力增加50
def set01():
    for item in enemy_list:
        item.atk += 50


set01()

for item in enemy_list:
    item.print_self_info()
