# 从包中导入模块 包名.模块名
# from 包名  import 模块名
# from 包名.模块 import 成员

# 特别注意：运行时，在day15文件夹下打开
from project.student_system.usl import StudentManagerView

view = StudentManagerView()
view.main()