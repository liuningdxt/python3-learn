"""
    枚举类
"""
import enum


class Week(enum.Enum):
    MON = '星期一'
    TUE = '星期二'
    WED = '星期三'
    THU = '星期四'
    FRI = '星期五'
    SAT = '星期六'
    SUN = '星期日'

    def info(self):
        print(f"这个是代表星期的一个数值：{self.value}")


print(Week.MON)
print(Week.MON.name)
print(Week.MON.value)
# 通过枚举变量名来访问
print(Week['SAT'])
print(Week['SAT'].name)
print(Week['SAT'].value)
# 通过枚举值来访问
print(Week('星期日'))
print(Week('星期日').name)
print(Week('星期日').value)
# 调用枚举方法info
Week.FRI.info()
# 通过__members__访问所有枚举值
for name, member in Week.__members__.items():
    print(name, "=>", member, ",", member.value)
