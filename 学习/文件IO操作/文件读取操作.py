"""
    文件读取操作
"""
# 打开文件 r 只读模式 要求文件必须存在
f = open("D:/测试.txt", "r", encoding="UTF-8")
print(type(f))
# 读取文件 read()
# print("读取15个字节", f.read(15))
# print("读取全部内容", f.read())

# 读取文件全部行 ，返回列表 readlines()
# lines = f.readlines()
# print(type(lines))
# print(lines)
# for line in lines:
#     print(line, end='')

# 逐行读取 readline()
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')

# line = f.readline()
# while line:
#     print(line, end='')
#     line = f.readline()

# 简化的for遍历
for line in f:
    print(line, end='')

# 关闭文件对象，结束IO流操作
f.close()
