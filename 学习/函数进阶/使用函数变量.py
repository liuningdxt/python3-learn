"""
    使用函数变量
"""


# 定义计算两个参数相加的函数
def add(x, y):
    return x + y


# 将add函数赋值给my_func，则my_func可以被当做add使用
my_func = add

print(my_func(1, 2))
print(add(1, 2))
