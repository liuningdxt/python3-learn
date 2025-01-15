"""
    变量的类型注解
"""
import random

# 基础数据-类型注解
name: str = "张三"
age: int = 10
b: bool = False


# 类对象-类型注解
class Person:
    pass


lisi: Person = Person()

# 基础容器-类型注解
my_list: list = [1, 2, 3, 4]
my_tuple: tuple = (1, "python222", False)
my_dict: dict = {"python222": 3.14, "java1234": 4.35}

# 容器类型元素-类型注解
my_list2: list[int] = [1, 2, 3, 4]
my_tuple2: tuple[int, str, bool] = (1, "python222", False)
my_dict2: dict[str, float] = {"python222": 3.14, "java1234": 4.35}

# 在注释中进行类型注解
r1 = random.randint(1, 10)  # type:int
