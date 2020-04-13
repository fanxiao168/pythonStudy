# 技能系统
# 用到 封装  继承  多态
# 开闭  单一  依赖倒置


# 影响效果
class SkillImpactEffect:
    '''
    技能影响的效果
    '''

    def impact(self):
        pass


# 伤害效果
class DamageEffect(SkillImpactEffect):
    def __init__(self, value):
        self.value = value

    def impact(self):
        print('扣你%d血' % self.value)


# 消耗法力
class CostSPEffect(SkillImpactEffect):
    def __init__(self, value):
        self.value = value

    def impact(self):
        print('消耗%d法力' % self.value)


# 降低防御力
class LowerDeffenseEffect(SkillImpactEffect):
    def __init__(self, ratio, time):
        self.ratio = ratio
        self.time = time

    def impact(self):
        print('降低防御%.1防御力，持续%.1f秒' % (self.ratio, self.time))


# 技能释放器
class SkillDeployer:
    '''
    技能释放器
    '''

    def __init__(self, name):
        self.name = name
        # 保存配置文件内容
        self.__dict_skill_config = self.__loacd_config_file()
        # 保存创建好的效果对象
        self.__list_effect_object = self.__create_effect_object()

    # 读配置文件
    def __loacd_config_file(self):
        return {
            '韦陀杵': ["LowerDeffenseEffect(0.3,2.5)", "CostSPEffect(20)", "DamageEffect(200)"],
            '亢龙有悔': ["DamageEffect(500)", "CostSPEffect(100)"]
        }

    # 创建对象
    def __create_effect_object(self):
        # 在字典中 根据技能名找到影响效果 实现
        # '亢龙有悔': ["DamageEffect(500)", "CostSPEffect(100)"
        list_effect_name = self.__dict_skill_config[self.name]
        # 列表 字符串
        # "DamageEffect(500)", "CostSPEffect(100)"
        # eval("DamageEffect(500)")
        # list_effect_object = []
        # for item in list_effect_name:
        #     list_effect_object.append(eval(item))
        # return list_effect_object
        return [eval(item) for item in list_effect_name]

    # 调用方法
    def genernate_skill(self):
        print('看招', self.name)
        for item in self.__list_effect_object:
            item.impact()


skill01 = SkillDeployer('亢龙有悔')
skill01.genernate_skill()
