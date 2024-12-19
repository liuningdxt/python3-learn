import random
num = random.randint(1,10)
print(num)
myNum = input("Number:")
myNum = int(myNum)
if myNum == num:
    print("Congratulations! You got it.")
elif myNum>num:
    print("Too big! Try again.")
else:
    print("Too small! Try again.")
