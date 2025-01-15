"""
    字符串拼接
    在Python中，使用加号 ( + )作为字符串的拼接运算符；
    有时候，我们需要将字符串与数值进行拼接，而 Python不允许直接拼接数值和字符串，程序必须先将数值转换成字符串。
为了将数值转换成字符串，可以使用str()或 repr()函数，例如如下代码。
"""

name = "小锋"
site = "Python知识分享网 www.python222.com"
tel = 66666666
print("姓名：" + name + ",个人网站：" + site + ",联系电话：" + str(tel))
print("姓名：" + name + ",个人网站：" + site + ",联系电话：" + repr(tel))
