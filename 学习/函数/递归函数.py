"""
    递归函数
"""


def cal(n):
    # 递归出口
    if n == 1:
        return 1
    return n + cal(n - 1)


print(cal(100))
