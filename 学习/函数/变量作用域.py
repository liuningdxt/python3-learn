"""
    变量作用域
"""

# 定义全局变量name2
name2 = "Jack"


def test():
    # 定义局部变量name
    name = "jack"
    print(name)
    global name2
    name2 = "Marry"


test()
# print(name)
print(name2)
