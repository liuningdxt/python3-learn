"""
    使用函数作为返回值
"""


def test(bol):
    if bol:
        return add
    else:
        return sub


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


b1 = test(True)
print(b1, b1(1, 2))
b2 = test(False)
print(b2, b2(1, 2))
