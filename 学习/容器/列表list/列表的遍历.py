"""
    列表的遍历
"""
# 定义一个有多元素的列表
list1 = ["java", "python", "c"]

for ele in list1:
    print(ele)

i = 0
while i < len(list1):
    ele = list1[i]
    print(ele)
    i += 1
