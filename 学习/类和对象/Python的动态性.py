"""
    Python的动态性
"""


class Dog:
    name = None

    def say(self):
        print(f"{self.name}:汪汪")


def action_func(self):
    print(f"{self.name}：还能跑，年龄：{self.age}")


dog = Dog()
dog.name = "Jack"
dog.say()
Dog.age = 11  # 给类动态添加age属性
Dog.action = action_func  # 给类动态添加方法action
dog.action()

dog2 = Dog()
dog2.name = "Marry"
dog2.age = 12
dog2.action()
