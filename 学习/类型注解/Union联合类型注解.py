"""
    Union联合类型注解
"""
from typing import Union

my_list2: list[int] = [1, 2, 3, 4]
my_dict2: dict[str, float] = {"python222": 3.14, "java1234": 4.35}
l1: list[Union[int, str, bool]] = [1, "python222", True]  # 如何注解多种元素类型
d1: dict[str, Union[str, int]] = {"k1": "python222", "k2": 2222}  # 如何注解多种元素类型
