"""
    while循环语句语法格式
    1+2+3+...+10 求和
"""

# 定义变量sum，用来保存运行过程中的累计和
sum = 0

# 定义变量i，循环过程每次被加的值
i = 1

while i <= 10:
    print(f"while循环执行第{i}次")
    # 进行累加
    sum += i
    # i每次执行加1
    i += 1
print("1+2+3+...+10=", sum)
