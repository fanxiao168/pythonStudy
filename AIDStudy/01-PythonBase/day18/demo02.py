'''
    内置高阶函数
    练习：exercise02.py
'''

from common.list_helper import ListHelper


class Enemy:
    def __init__(self, name, hp, atk=None, defense=None):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense


enemy_list = [
    Enemy('玄冥二老', 86, 80, 120),
    Enemy('成昆', 0, 0, 150),
    Enemy('谢逊', 120, 50, 150),
    Enemy('灭霸', 0, 0, 999)
]

# 1. 在敌人列表中查找所有死人
for item in filter(lambda item: item.hp == 0, enemy_list):
    print(item.name)
for item in ListHelper.find_all(enemy_list, lambda item: item.hp == 0):
    print(item.name)

# 2. 在敌人列表中查找所有敌人的名称
for item in map(lambda item:item.name,enemy_list):
    print(item)
for item in ListHelper.select(enemy_list,lambda item:item.name):
    print(item)

# 3. 获取攻击力最大的敌人
re = max(enemy_list,key=lambda item:item.atk)
print(re.name)
re1 = ListHelper.get_max(enemy_list,lambda item:item.atk)
print(re1.name)

# 4.对敌人列表根据攻击力升序排列
# sorted 返回排好序的数据
for item in sorted(enemy_list,key=lambda item:item.atk):
    print(item.atk)

#  对敌人列表根据攻击力降序排列
# sorted 返回排好序的数据
for item in sorted(enemy_list,key=lambda item:item.atk,reverse= True):
    print(item.atk)

ListHelper.order_by(enemy_list,lambda item:item.atk)
for item in enemy_list:
    print(item.atk)

