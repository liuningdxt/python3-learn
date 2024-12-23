def SayHelloWorld():
    print("hello_world")


SayHelloWorld()
SayHelloWorld()


def add(x, y):
    print(f"add:{x}+{y}={x + y}")
    return x + y


add(1, 2)
add(3, 4)
add(5, 6)
add(x=1, y=2)
add(y=2, x=1)
add(1, y=2)


def SayHello(name="Hello", message="Hello message"):
    print(f"hello,{name}说{message}")


SayHello(name="Hello1", message="Hello message1")
SayHello()
SayHello(message="Hello message2")
SayHello("ZHANGSAN")
