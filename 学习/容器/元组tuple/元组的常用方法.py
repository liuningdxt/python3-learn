"""
    元组的常用方法
"""

# 下标索引用法和列表一样，唯一区别就是不能修改元素
t1 = ("java", "python", "c")
print(t1[1])
print(t1[-1])
# t1[1] = "python222"

# 元组里可以嵌套元组
t6 = ((1, 2, 3), (4, 5, 6))
print(t6[1][1])

# index(元素)方法，查找元组中指定元素的下标，不存在就报错
t2 = ("java", "python", "c")
print(t2.index("python"))

# count(元素) 统计某元素在元组中的个数
t3 = ("java", "python", "c", "python", "c#")
print(t3.count("c"))

# len(元组)，统计元组内一共有多少元素
t4 = ("java", "python", "c", "python", "c#")
print(len(t4))

# 遍历元组
t5 = ("java", "python", "c", "python", "c#")

for ele in t5:
    print(ele)

i = 0
while i < len(t5):
    ele = t5[i]
    print(ele)
    i += 1
