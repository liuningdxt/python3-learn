"""
    模块的概念和基本使用
"""
# 示例一，import 模块名
import random  # 导入Python内置的random模块

print(random.randint(1, 10))
print(random.random())

# 示例二，import 模块名 as 别名
# import random as r
#
# print(r.randint(1, 10))

# 示例三，import 模块1,模块2
# import random, time
#
# print("开始，过5秒执行")
# time.sleep(5)
# print(random.randint(1, 10))
# print("结束")

# 示例四，import 模块1 as 别名1,模块2 as 别名2
# import random as r, time as t
#
# print("开始，过5秒执行")
# t.sleep(5)
# print(r.randint(1, 10))
# print("结束")
