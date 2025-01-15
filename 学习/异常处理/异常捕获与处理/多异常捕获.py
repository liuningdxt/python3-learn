"""
    多异常捕获
"""


# 定义人类
class Person:
    # 属性 姓名
    name = None
    # 属性 年龄
    age = None


# print(Person().sex) # AttributeError
# print(1 / 0)  # ZeroDivisionError
try:
    # print(Person().sex)
    # print(2 / 0)
    pass
except (ZeroDivisionError, AttributeError):
    print("出现了异常", )
print("后续代码")
