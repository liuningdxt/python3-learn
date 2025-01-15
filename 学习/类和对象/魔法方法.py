"""
    魔法方法
"""


# 定义人类
class Person:
    # 属性 姓名
    name = None
    # 属性 年龄
    age = None

    def __init__(self, name, age):
        print("调用有参构造方法")
        self.name = name
        self.age = age

    def __str__(self):
        print("调用str")
        return f"姓名：{self.name}，年龄：{self.age}"

    def __eq__(self, other):
        print("调用eq方法")
        return self.age == other.age


zhangsan = Person("张三", 21)
print(zhangsan)
print(str(zhangsan))
lisi = Person("李四", 21)
print(zhangsan == lisi)
