"""
    for循环嵌套
    range(stop)
"""

# range(stop) 返回0到stop-1的数字序列
for i in range(10):
    print(i, end=' ')

print()
# range(start,stop) 返回start到stop-1的数字序列
for i in range(3, 10):
    print(i, end=' ')

print()
# range(start,stop,step) 返回start到stop-1的数字序列,步长step
for i in range(3, 10, 2):
    print(i, end=' ')

print()
for i in range(1, 6):
    print(f"第{i}行")
    for j in range(1, 11):
        print(f"第{j}列", end=' ')
    print()
