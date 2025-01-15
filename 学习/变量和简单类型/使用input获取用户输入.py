"""
    使用input获取用户输入
"""

name = input("请输入您的姓名：")
print(name, type(name))

age = input("请输入您的年龄：")
age = int(age)
print(age, type(age))

height = input("请输入您的身高：")
height = float(height)
print(height, type(height))
