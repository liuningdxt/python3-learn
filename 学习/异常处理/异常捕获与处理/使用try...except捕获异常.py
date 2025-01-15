"""
    使用try...except捕获异常
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
    print(2 / 1)
except:
    print("出现了异常")
print("后续代码")
