"""
    lambda匿名函数
"""


def test(x, y, fn):
    return fn(x, y)


# def add(x, y):
#     return x + y


def sub(x, y):
    return x - y


print(test(2, 1, lambda x, y: x + y))
print(test(2, 1, sub))
