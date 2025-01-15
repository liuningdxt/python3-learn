"""
    初识Python类和对象
"""


# 定义人类
class Person:
    # 属性 姓名
    name = None
    # 属性 年龄
    age = None


# 创建一个对象 zhangsan
zhangsan = Person()
zhangsan.name = "张三"
zhangsan.age = 21
print(f"姓名：{zhangsan.name}，年龄：{zhangsan.age}")

# 再创建一个对象 lisi
lisi = Person()
lisi.name = "李四"
lisi.age = 12
print(f"姓名：{lisi.name}，年龄：{lisi.age}")
