"""
    for循环语句语法格式
"""

# 定义total变量，统计字符o的个数
total = 0

# 定义字符串website
website = "www.python222.com"

# 通过for循环遍历website字符串，拿到每个字符串字符
for w in website:
    if w == 'o':
        total += 1
    print(w)
print(f"'o'的总个数是{total}")
