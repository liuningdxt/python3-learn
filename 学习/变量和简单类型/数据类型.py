"""
    数据类型测试Demo
    用type()方法可以查看变量的类型
    Python是弱类型语言，变量的类型也是可以改变的。
"""

# 定义变量a 赋值222
a = 222
b = 3.14
c = "Python知识分享网"

# 打印变量类型
print("a=", a, type(a))
print("b=", b, type(b))
print("c=", c, type(c))

# 改变变量a的类型为字符串类型
a = "字符串类型ccc"
print("a=", a, type(a))
