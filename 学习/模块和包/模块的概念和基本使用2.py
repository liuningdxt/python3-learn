"""
    模块的概念和基本使用
"""
# 示例一，from 模块 import 成员
# from random import randint
#
# print(randint(1, 10))

# 示例二，from 模块 import 成员 as 成员别名
# from random import randint as ri
#
# print(ri(1, 10))

# 示例三，from 模块 import 成员1,成员2
# from random import randint, random
#
# print(random())
# print(randint(1, 10))

# 示例四，from 模块 import 成员1 as 成员别名1,成员2 as 成员别名2
# from random import randint as ri, random as r
#
# print(r())
# print(ri(1, 10))

# 示例五，from 模块 import *
from random import *

print(randint(1, 10))
print(random())
