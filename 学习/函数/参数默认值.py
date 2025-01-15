"""
    参数默认值
"""


def say_hi(name="锋哥", msg="欢迎来python222学Python"):
    print(f"{name}说：{msg}")


# 全部使用默认参数
say_hi()

# msg使用默认参数
say_hi("小王")

# 两个参数都不使用默认值
say_hi("李四", "我去java1234学Java")

# name使用默认值，msg需要使用关键字参数
say_hi(msg="也喜欢Java")
