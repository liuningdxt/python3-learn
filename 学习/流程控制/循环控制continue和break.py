"""
    循环控制continue和break
    - continue 中断本次循环，直接进入下一次循环
    - break 直接结束循环
"""
for i in range(1, 11):
    print(i, end=' ')

print()

for i in range(1, 11):
    if i == 4:
        continue
    print(i, end=' ')

print()
for i in range(1, 11):
    if i == 4:
        break
    print(i, end=' ')
