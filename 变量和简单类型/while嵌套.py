i = 1
while i <= 5:
    print(f"打印第{i}行")
    j = 1
    while j <= 5:
        print(f"第{i}行第{j}列", end=" ")
        j += 1
    print("")
    i += 1
print("打印完成")
