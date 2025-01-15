"""
    字符串的常用方法
"""
str1 = "python222 是学习python的好地方"
print(f"str1={str1},类型是：{type(str1)}")
print(str1[1])
print(str1[-1])

# index(元素)方法，查找字符串中指定元素的下标，不存在就报错
str2 = "python222 是学习python的好地方"
print(str2.index("222"))

# replace(old字符串1，new字符串2)，把字符串内的所有字符串1,替换成字符串2，然后方法返回一个新字符串。(不是修改字符串操作)
str3 = "python222 是学习python的好地方，我要成为python老司机"
str3_1 = str3.replace("python", "java")
print(str3)
print(str3_1)
str3_2 = str3.replace("python", "java", 2)
print(str3_2)

# split(分隔符字符串)，根据指定的分隔符字符串，将字符串分割成多个字符串，并存入列表对象中，方法返回列表对象。(不是修改字符串操作)
str4 = "java php python"
str5 = "java,php,python"
l1 = str4.split(" ")
l2 = str5.split(",")
print(str4)
print(str5)
print(f"l1={l1},type={type(l1)}")
print(f"l2={l2},type={type(l2)}")

# strip()，去掉前后空格，返回新的字符串
str6 = "  java php python  "
print(str6.strip())
str7 = "@%java php python%@"
print(str7.strip("@%"))

# count(字符串)，统计字符串中出现指定字符串的个数
str8 = "java php python"
print(str8.count("ph"))

# len(字符串)，统计字符串的长度
str9 = "java php python"
print(len(str9))
