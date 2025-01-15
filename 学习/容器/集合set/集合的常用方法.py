"""
    集合的常用方法
"""

# add(元素),添加元素到集合，假如元素集合里存在，则忽略
# 赋值定义集合
set1 = {"php", "java", "python"}
set1.add("c")
set1.add("php")
print(set1)

# pop()，随机从集合中获取一个元素，并且返回
set2 = {"php", "java", "python"}
ele = set2.pop()
print(set2, ele)

# clear()，清空集合
set3 = {"php", "java", "python"}
set3.clear()
print(set3)

# 集合1.difference(集合2)  返回差集 （集合1有但是集合2没有的新集合）
set4 = {"a", "b", "c"}
set5 = {"a", "d", "e"}
print(set4.difference(set5))
print(set4)
print(set5)

# 集合1.difference_update(集合2) ,删除差集。集合1内，删除和集合2相同的元素
set6 = {"a", "b", "c"}
set7 = {"a", "d", "e"}
set6.difference_update(set7)
print(set6)
print(set7)

# 集合1.union(集合2)，返回合并集合1，集合2后的新集合
set8 = {"a", "b", "c"}
set9 = {"a", "d", "e"}
set10 = set8.union(set9)
print(set10)
print(set8)
print(set9)

# len(集合)统计元素个数
set11 = {"a", "b", "c"}
print(len(set11))

# 集合遍历
set12 = {"php", "java", "python"}
for ele in set12:
    print(ele)
