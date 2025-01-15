"""
    if语句的嵌套应用
"""

vip = True
amount = input("请输入充值金额：")
amount = int(amount)
if amount == 100:
    if vip:
        print("总共充值：", 100 + 30)
    else:
        print("总共充值：", 100 + 20)
elif amount == 200:
    if vip:
        print("总共充值：", 200 + 70)
    else:
        print("总共充值：", 200 + 50)
