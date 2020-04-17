# 3.创建敌人类（姓名，血量，攻击力，防御力）
#      创建敌人列表，存储若干敌人
#      ——-- （1）在敌人列表中查找所有死人
#      ---- （2）在敌人列表中查找血量最大的敌人
#      ---- （3）在敌人列表中查找所有敌人姓名与攻击力

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


# （1）在敌人列表中查找所有死人
def find01():
    for item in enemy_list:
        if item.hp == 0:
            yield item


# 优势：惰性/延迟（省内存）
# 缺点：获取元素时不灵活（索引/切片）
for item in find01():
    print(item.name)

# 解决：惰性操作 ---> 立即操作
result = tuple(find01())
print(result[0].name)


# （2）在敌人列表中查找血量最大的敌人
def get_max():
    max_value = enemy_list[0]
    for i in range(1, len(enemy_list)):
        if max_value.hp < enemy_list[i].hp:
            max_value = enemy_list[i]
    return max_value


print(get_max().name)


# （3）在敌人列表中查找所有敌人姓名与攻击力
def find02():
    for item in enemy_list:
        yield (item.name, item.atk)


re = find02()
for item in re:
    print(item[0], item[1])

for item in find02():
    print(item[0], item[1])

for item in find02():
    print(item[0], item[1])
