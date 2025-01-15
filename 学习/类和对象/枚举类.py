"""
    枚举类
"""
import enum

# 定义一个Season枚举类 Enum第一个参数是类名，第二个参数是元组，用于列出所有枚举值
# 每个成员都有name和value两个属性，name是枚举值变量名，value是枚举值的序号，从1开始
Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)

# 根据枚举变量名来访问枚举对象
print(Season['WINTER'])
print(Season['WINTER'].name)
print(Season['WINTER'].value)

# 根据枚举值访问枚举对象
print(Season(3))
print(Season(3).name)
print(Season(3).value)

# 提供__members__属性，该属性返回一个dict字典，包含了所有枚举实例；通过__members__属性，访问所有枚举值
for name, member in Season.__members__.items():
    print(name, "=>", member, ",", member.value)
