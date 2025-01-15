"""
    Python的动态性
"""


class Dog:
    name = None

    def say(self):
        print(f"{self.name}:汪汪")


def action_func():
    print("还能跑")


dog = Dog()
dog.name = "Jack"
dog.say()
dog.age = 11  # 给对象动态添加属性age
dog.action = action_func  # 给对象动态添加方法action
dog.action()
print(dog.age)

dog2 = Dog()
dog2.name = "Marry"
# print(dog2.age)  # 报错 dog2没有age属性
dog2.action()  # 报错 dog2没有action方法
