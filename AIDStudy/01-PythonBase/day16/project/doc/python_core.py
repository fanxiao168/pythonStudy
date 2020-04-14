import sys

sys.path.append('/Users/shangyudianzi/Desktop/pythonStudy/AIDStudy/01-PythonBase/day16/project')
print(sys.path)

# 目录.包  导入模块
from game import game_2048

# 模块名.成员
game_2048.fun01()

# 目录.包.模块  导入 成员
from project.game.game_2048 import fun01

fun01()

import demo01
