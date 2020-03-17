# 创建技能类Skill
# 数据：名称    攻击比例（0.1 -5)
#              持续时间(0.1-10)
#              消耗法力(0-100)

class Skill:
    def __init__(self, name="", atk_ratio=0.1, duration=0.1, cost_mp=0):
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration
        self.cost_mp = cost_mp

    @property
    def atk_ratio(self):
        return self.__atk_ratio

    @atk_ratio.setter
    def atk_ratio(self, value):
        if 0.1 <= value <= 5:
            self.__atk_ratio = value
        else:
            raise ValueError('攻击力不在范围内')

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if 0.1 <= value <= 10:
            self.__duration = value
        else:
            raise ValueError('持续时间不在范围内')

    @property
    def cost_mp(self):
        return self.__cost_mp

    @cost_mp.setter
    def cost_mp(self, value):
        if 0 <= value <= 100:
            self.__cost_mp = value
        else:
            raise ValueError('法力值消耗超出范围')


# 定义一个至少包含四个技能的技能列表
skill_list = [
    Skill('降龙十八掌', 3, 2, 50),
    Skill('九阴白骨爪', 2, 4, 30),
    Skill('吸星大法', 0.5, 8, 0),
    Skill('旋风斩', 0.1, 9, 3)
]


# 定义函数  查找'降龙十八掌'的技能对象
def find01():
    for item in skill_list:
        if item.name == '降龙十八掌':
            return item
    return None


s01 = find01()


# if s01:
#     print(s01.name)


# 定义函数 查找所有不消耗法力的技能
def find02():
    result = []
    for item in skill_list:
        if item.cost_mp == 0:
            result.append(item)
    return result


res = find02()


# for item in res:
#     print(item.name)


# 定义函数 查找所有技能的名称及持续时间
def find03():
    # result = {}
    # for item in skill_list:
    #     result[item.name] = item.duration
    #     result.setdefault(item.name,item.duration)
    return {item.name: item.duration for item in skill_list}


res = find03()


# for k, v in res.items():
#     print(k, v)


# 定义函数 删除所有不消耗法力的技能
# （返回删除结果 个数/对象）
def delete():
    # 统计删除元素个数
    count = 0
    for i in range(len(skill_list) - 1, -1, -1):
        if skill_list[i].cost_mp == 0:
            del skill_list[i]
            count += 1
    return count


# res = delete()
# print(res)

# 定义函数 找出攻击比例最大的技能
def get_max():
    max_value = skill_list[0]
    for i in range(1, len(skill_list)):
        if max_value.atk_ratio < skill_list[i].atk_ratio:
            max_value = skill_list[i]
    return max_value


res = get_max()
print(res.name)


# 定义函数 对技能列表按照持续时间升序排列
def mysort():
    for r in range(len(skill_list) - 1):
        for c in range(r + 1, len(skill_list)):
            if skill_list[r].duration > skill_list[c].duration:
                skill_list[r], skill_list[c] = skill_list[c], skill_list[r]


mysort()
for item in skill_list:
    print(item.name)
