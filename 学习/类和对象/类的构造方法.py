"""
    类的构造方法
"""


# 定义人类
class Person:
    # 属性 姓名
    name = None
    # 属性 年龄
    age = None

    # def __init__(self):
    #     print("构造方法")

    def __init__(self, name, age):
        print("调用有参构造方法")
        self.name = name
        self.age = age

    # 成员方法 say 打印输出当前对象的姓名和年龄
    def say(self):
        print(f"姓名：{self.name}，年龄：{self.age}")

    def say2(self, msg):
        print(f"姓名：{self.name}，年龄：{self.age},备注：{msg}")


# 创建一个对象 zhangsan
zhangsan = Person("张三", 21)
# zhangsan.name = "张三"
# zhangsan.age = 21
zhangsan.say()
zhangsan.say2("成年人")

# 再创建一个对象 lisi
lisi = Person("李四", 12)
# lisi.name = "李四"
# lisi.age = 12
lisi.say()
lisi.say2("未成年")
