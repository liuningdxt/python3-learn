"""
    捕获指定的异常
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
    print(Person().sex)
    print(2 / 0)
except ZeroDivisionError as z:
    print("出现了除0异常", z)
except AttributeError as a:
    print("出现了属性异常", a)
print("后续代码")
