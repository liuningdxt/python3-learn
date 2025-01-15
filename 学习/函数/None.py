"""
    None
"""


# 定义最基础函数 helloworld
def say_helloworld():
    print("Python大爷你好，学Python，上www.python222.com")


# result = say_helloworld()
# print(f"返回结果是{result},类型是{type(result)}")

def check_user(userName, password):
    if userName == 'python222' and password == '123456':
        return "success"
    else:
        return None


result = check_user('python222', '123456')
print(f"返回结果是{result}")

if not result:
    print("登录成功")

# 可以用于声明无初始化内容的变量
userName = None
