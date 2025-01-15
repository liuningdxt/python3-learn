"""
    函数的不定长参数
"""


# 不定长参数(位置传递)
def test(*args):
    print(args, type(args))


test(1, "2")
test(True, 1, "2", 3.134)
test()


# 不定长参数(关键字传递)
def test2(**kwargs):
    print(kwargs, type(kwargs))


test2(name="Jack", age=11)
test2()
