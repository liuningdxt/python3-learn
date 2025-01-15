"""
    if elif else语句语法格式
"""

score = input("请输入您的语文成绩：")
print(f"我的语文成绩是：{score}")
score = float(score)
if score >= 90:
    print("成绩优秀")
elif score >= 70:
    print("成绩良好")
elif score >= 60:
    print("成绩及格")
else:
    print("成绩不及格")
print("再接再励，加油")
