"""
    函数方法的类型注解
        函数（方法）的类型注解
    形参注解
        def add(x:int, y:int):
            return x+y
    返回值注解：
        def 函数方法名（形参：类型,...形参：类型)-> 返回值类型:
            pass
"""


def add(x: int, y: int) -> int:
    return x + y


print(add(1, 2))
