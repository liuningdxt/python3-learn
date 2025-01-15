"""
    使用raise引发异常
"""
try:
    age = 19
    if age < 18:
        raise Exception
    else:
        print("放行")
except Exception as e:
    print(type(e))
