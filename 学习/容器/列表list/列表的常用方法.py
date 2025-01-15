"""
    列表的常用方法
"""
# 定义一个有多元素的列表
list1 = ["java", "python", "c"]

# 修改指定位置的元素值  语法：列表[下标索引]=值
list1[1] = "python222"
list1[-1] = "c222"
print(list1)

# index(元素)方法，查找列表中指定元素的下标，不存在就报错
list2 = ["java", "python", "c"]
index = list2.index("python")
print(index)

# insert(下标,元素)，在指定下标位置元素之前，插入元素
list3 = ["java", "python", "c"]
list3.insert(1, "php")
print(list3)

# append(元素)，将指定元素，追加到列表的尾部
list4 = ["java", "python", "c"]
list4.append("php")
print(list4)

# extend(容器)，追加容器数据到列表最后
list5 = ["java", "python", "c"]
list5.extend(["php", "c#"])
print(list5)

# del 列表[下标] 删除指定下标的元素
list6 = ["java", "python", "c"]
del list6[1]
print(list6)

# pop(元素下标) ，取出元素。从列表中删除这个元素，方法返回该元素。（下标越界就报错）
list7 = ["java", "python", "c"]
ele = list7.pop(1)
print(list7, ele)

# remove(元素)，删除指定元素在列表中的第一个匹配项
list8 = ["java", "python", "c", "python", "php"]
list8.remove("python")
print(list8)

# clear()清空列表
list9 = ["java", "python", "c"]
list9.clear()
print(list9)

# count(元素) 统计某元素在列表中的个数
list10 = ["java", "python", "c", "python", "php"]
count = list10.count("c")
print(count)

# len(列表)，统计列表内一共有多少元素
list11 = ["java", "python", "c"]
print(len(list11))
