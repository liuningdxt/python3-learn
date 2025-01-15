"""
    while循环嵌套
    1 2 3
    4 5 6
"""

# 定义行
i = 1

# 外层嵌套 打印5行
while i <= 5:
    print(f"打印第{i}行")

    # 定义列
    j = 1
    while j <= 8:
        print(f"打印第{j}列", end=" ")
        j += 1
    print()
    i += 1
print("哇哇，打印完了")
