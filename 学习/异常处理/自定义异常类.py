"""
    自定义异常类
"""


# 自定义异常类
class TooLongException(Exception):

    def __init__(self, length):
        self.lenght = length

    def __str__(self):
        return f"长度是{self.lenght}，超长了"


def name_test():
    try:
        name = input("请输入您的姓名：")
        if len(name) > 4:
            raise TooLongException(len(name))
        else:
            print(name)
    except TooLongException as tle:
        print("出现了异常：", tle)


name_test()
