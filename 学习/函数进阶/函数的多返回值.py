"""
    函数的多返回值
"""


def test():
    return 1, "python222", True


# 返回元组类型
result = test()
print(f"result={result},type={type(result)}")

# 通过多个变量接收
a, b, c = test()
print(a, b, c)
