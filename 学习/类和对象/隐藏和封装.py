"""
    隐藏和封装
"""


# 定义人类
class Person:
    # 属性 姓名
    name = None
    # 属性 年龄
    age = None
    # 私有属性 得分
    __score = None

    def __init__(self, name, age, score):
        print("调用有参构造方法")
        self.name = name
        self.age = age
        self.__score = score

    # 成员方法 say 打印输出当前对象的姓名和年龄
    def say(self):
        print(f"姓名：{self.name}，年龄：{self.age},成绩：{self.__score}")
        self.__check_score()

    # 定义私有方法，不及格，叫家长来下
    def __check_score(self):
        if self.__score < 60:
            print(f"叫{self.name}的家长来下学校")


zhangsan = Person("张三", 21, 67)
zhangsan.say()
# zhangsan.__check_score() # 访问私有方法，报错
# print(zhangsan.__score) # 访问私有属性，报错

lisi = Person("李四", 22, 19)
lisi.say()
