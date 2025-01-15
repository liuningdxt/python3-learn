"""
    容器序列切片
"""
# 对列表进行切片
list1 = [0, 1, 2, 3, 4, 5, 6, 7]
print(list1[1:4])
print(list1[1:4:1])
print(list1)

# 对元组进行切片
tuple1 = (0, 1, 2, 3, 4, 5, 6, 7)
print(tuple1[:])
print(tuple1[::2])

# 对字符串进行切片
str1 = "01234567"
print(str1[::-1])
print(str1[::-2])
print(str1[6:3:-1])
print(str1[6:3:-2])
