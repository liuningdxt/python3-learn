"""
    文件读取操作 with open
"""
with open("D:/测试.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line, end='')
