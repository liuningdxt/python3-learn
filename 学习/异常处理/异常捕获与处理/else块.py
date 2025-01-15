"""
    else块
"""


# 定义人类
class Person:
    # 属性 姓名
    name = None
    # 属性 年龄
    age = None


# print(Person().sex)
# print(1 / 0)
try:
    print(2 / 0)
except:
    print("出现了异常")
else:
    print("没有出现异常，我们干点正事")
print("后续代码")
