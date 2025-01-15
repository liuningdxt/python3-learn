"""
    使用函数作为函数形参
"""


def test(x, y, fn):
    return fn(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


print(test(2, 1, add))
print(test(2, 1, sub))
