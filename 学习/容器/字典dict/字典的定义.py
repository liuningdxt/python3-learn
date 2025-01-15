"""
    字典的定义
"""
# 字典赋值定义
dict1 = {"语文": 68, "数学": 98, "英语": 76}
print(f"dict1={dict1},type={type(dict1)}")

# 空字典定义
dict2 = {}
dict3 = dict()
print(f"dict2={dict2},type={type(dict2)}")
print(f"dict3={dict3},type={type(dict3)}")

# key不能重复，否则新的key:value会覆盖老的key:value
dict4 = {"语文": 68, "数学": 98, "英语": 76, "数学": 100}
print(f"dict4={dict4},type={type(dict4)}")

# 字典嵌套
dict5 = {
    "张三": {"语文": 68, "数学": 98, "英语": 76},
    "李四": {"语文": 48, "数学": 68, "英语": 86},
    "王五": {"语文": 58, "数学": 48, "英语": 26}
}
print(f"dict5={dict5},type={type(dict5)}")
