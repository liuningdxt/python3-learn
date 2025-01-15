"""
    字典的常用方法
"""
# 字典赋值定义
dict1 = {"语文": 68, "数学": 98, "英语": 76}
print(dict1["语文"])
print(dict1['数学'])
print(dict1["英语"])
print(dict1.get("数学2"))

dict5 = {
    "张三": {"语文": 68, "数学": 98, "英语": 76},
    "李四": {"语文": 48, "数学": 68, "英语": 86},
    "王五": {"语文": 58, "数学": 48, "英语": 26}
}
print(dict5["张三"]["数学"])
print(dict5["王五"]["英语"])
print(dict5.get("张三").get("英语"))

# 新增或者修改元素 语法 字典["Key"]=Value 如果key不存在，就是新增，如果key存在，就是修改。
dict2 = {"语文": 68, "数学": 98, "英语": 76}
# key不存在，新增元素
dict2["体育"] = 77
print(dict2)
# key存在，修改元素
dict2["语文"] = 99
print(dict2)
dict2.update({"数学": 88})
print(dict2)
dict2.update({"计算机": 100})
print(dict2)
dict2.update({"语文": 10, "素质": 99})
print(dict2)

# 删除元素。语法 字典.pop("Key")  字典中删除该key:value元素，然后方法返回该key的Value
dict4 = {"语文": 68, "数学": 98, "英语": 76}
print(dict4.pop("数学"))
print(dict4)

# 清空元素。语法：clear()
dict6 = {"语文": 68, "数学": 98, "英语": 76}
dict6.clear()
print(dict6)

# 获取所有key。语法 字典.keys()。返回值类型的是 dict_keys 类对象
dict7 = {"语文": 68, "数学": 98, "英语": 76}
print(f"keys={dict7.keys()},type={type(dict7.keys())}")

# 遍历字典 先获取字典的keys，然后遍历keys，通过key获取字典值
dict8 = {"语文": 68, "数学": 98, "英语": 76}
keys = dict8.keys()
for key in keys:
    value = dict8[key]
    print(key, value)

# 遍历方式2  遍历字典，每次拿到的也是key 以后我们就用这种简单方式，不用获取keys
for key in dict8:
    value = dict8[key]
    print(key, value)

# 统计字典元素的总数量，len(字典)
dict9 = {"语文": 68, "数学": 98, "英语": 76}
print(len(dict9))
