"""
    文件追加操作
"""
# 打开文件 a 写入，文件如果不存在，会自动创建
f = open("D:/测试3.txt", "a", encoding="UTF-8")

# write方法写入，内容是写入内存缓存区
f.write("\npython222.com也真好")

# flush刷新，写入到磁盘
f.flush()

# close关闭文件IO
f.close()
