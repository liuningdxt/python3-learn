"""
    字符串工具
"""
__all__ = ['isEmpty']


def isEmpty(s: str):
    """
        判断字符串是否空
    :param s: 传入的字符串参数
    :return: 如果是空，则返回True，否则返回False
    """
    if not s:
        return True
    elif len(s.strip()) == 0:
        return True
    else:
        return False


def isNotEmpty(s: str):
    """
        判断字符串是否不是空
    :param s:  传入字符串参数
    :return:  不空则返回True，否则返回False
    """
    if s:
        if len(s.strip()) > 0:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print("测试代码：", isEmpty(None))
