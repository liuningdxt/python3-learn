"""
    列表的定义
"""

# 定义一个有多元素的列表
list1 = ["java", "python", "c"]
print(list1)

# 定义空列表
list2 = []
list3 = list()
print(list2)
print(list3)
list2 = list1
list3 = list1
print(list2)
print(list3)

# 列表里元素类型没有限制
list4 = ["python222", 222, 3.14, True]
print(list4)

# 列表里可以嵌套列表
list5 = [[1, 2, 3], [4, 5, 6]]
print(list5)
