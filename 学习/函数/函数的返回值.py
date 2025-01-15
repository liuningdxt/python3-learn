"""
    函数的返回值
"""


# 定义一个加法函数
def add(x, y):
    result = x + y
    # 通过return关键字，把x+y的结果返回给函数的调用者
    return result


# 定义变量r，接收函数的返回值
r = add(1, 2)
print(f"调用add(1,2)的返回结果是{r}")

# 定义变量r2，接收函数的返回值
r2 = add(2, 3)
print(f"调用add(2,3)的返回结果是{r2}")
