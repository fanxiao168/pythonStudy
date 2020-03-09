# 1. 存储各个城市的美食与景区(不用输入)在控制台显示
# 北京：
#    美食：烤鸭 豆汁 卤煮 炸酱面
#    景区：故宫 天安门 天坛
# 四川：
#    美食：火锅 串串 毛血旺
#    景区：峨眉山 九寨沟 春熙路

dict_info = {
    "北京": {
        "美食": ['烤鸭', '豆汁', '卤煮', '炸酱面'],
        '景区': ['故宫', '天安门', '天坛']
    },
    "四川": {
        "美食": ['火锅', '串串', '毛血旺'],
        '景区': ['峨眉山', '九寨沟', '春熙路']
    }
}

# 查询所有北京的美食
for item in dict_info['北京']['美食']:
    print(item)
# 查询所有四川的景区
for item in dict_info['四川']['景区']:
    print(item)
