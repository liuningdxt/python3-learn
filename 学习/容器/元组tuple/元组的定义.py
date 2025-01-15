"""
    元组的定义
"""

# 赋值定义
t1 = ("java", "python", "c")
print(f"t1={t1},类型={type(t1)}")

t2 = ("java",)
print(f"t2={t2},类型={type(t2)}")

# 空元组定义
t3 = ()
t4 = tuple()
print(f"t3={t3},类型={type(t3)}")
print(f"t4={t4},类型={type(t4)}")

# 元组里元素类型没有限制
t5 = ("python", 222, 3.14, True)
print(f"t4={t5},类型={type(t5)}")

# 元组里可以嵌套元组
t6 = ((1, 2, 3), (4, 5, 6))
print(f"t6={t6},类型={type(t6)}")
