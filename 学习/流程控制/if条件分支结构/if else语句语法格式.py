"""
    if else语句语法格式
    注意点：
    第一 else后面要加冒号：
    第二 else 执行内容前面也是四个空格
"""

age = input("请输入您的年龄：")
age = int(age)
print(f"我今年{age}岁了")
if age >= 18:
    print("已经成年了")
    print("我长大了")
else:
    print("还未成年")
    print("我要努力长大")
print("我要好好学习，天天向上")
