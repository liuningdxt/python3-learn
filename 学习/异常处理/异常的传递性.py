"""
    异常的传递性
"""


def funC():
    print("funC()开始")
    a = 1 / 0
    print("funC()结束")


def funB():
    print("funB()开始")
    funC()
    print("funB()结束")


def funA():
    print("funA()开始")
    funB()
    print("funA()结束")


try:
    funA()
except Exception as e:
    print(e)
