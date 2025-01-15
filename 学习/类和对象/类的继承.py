"""
    类的继承
"""


# 定义一个水果类，作为父类
class Fruit:
    # 父类属性 口感
    taste = None

    def say_taste(self):
        print(f"口感：{self.taste}")


class Food:
    # 父类属性 价格
    price = 1

    # 父类方法 打印价格
    def say_price(self):
        print(f"价格：{self.price}")


# 定义香蕉子类，继承父类Food
class Banana(Fruit, Food):
    # 子类属性 颜色
    color = None

    # 重写父类属性
    price = 9

    def say_color(self):
        print(f"香蕉颜色：{self.color}")

    def __str__(self):
        return f"口感：{self.taste}，价格：{self.price}，颜色：{self.color}"

    # 重写父类方法 打印价格
    def say_price(self):
        print(f"父类属性打印：{Food.price},{super().price}")
        # 调用父类方法
        Food.say_price(self)
        super().say_price()
        print(f"香蕉价格：{self.price}")


b1 = Banana()
b1.taste = "果肉芳香"
b1.say_taste()
b1.color = "黄色"
b1.say_color()
print(b1.price)
b1.price = 10.1
b1.say_price()
print(b1)
