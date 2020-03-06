# ['张三丰','翠山','无忌'] --> {'无忌':2,'翠山':2,'张三丰':3}
# list --> dict  key 是列表的元素 value是key的长度
list_name = ['张三丰', '翠山', '无忌']
dict_name = {}
for item in list_name:
    dict_name[item] = len(item)
print(dict_name)

dict_name = {item: len(item) for item in list_name}
print(dict_name)

# 姓名列表['无忌','赵敏','芷若']
# 房间列表[101,102,103]
# 把两个列表合并为一个字典 姓名作为key 房间号作为value
name_list = ['无忌', '赵敏', '芷若']
room_list = [101, 102, 103]
dict_name_room = {}
for i in range(len(name_list)):
    dict_name_room[name_list[i]] = room_list[i]
print(dict_name_room)

dict_name_room = {name_list[i]: room_list[i] for i in range(len(name_list))}
print(dict_name_room)
