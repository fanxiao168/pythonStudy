# 从包名.子包名.模块名  导入 函数
# from my_project.skill_system.skill_deployer import  skill_deployer

# 从目录名.包名  导入模块
from my_project.skill_system import *

# 模块名.函数名
skill_deployer.skill_deployer()
skill_manager.SkillManager().skill_manager()

class Main:
    @classmethod
    def my_main(cls):
        print('in Main')
