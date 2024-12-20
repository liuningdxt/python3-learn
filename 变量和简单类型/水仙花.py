for i in range(1, 10):
    for j in range(0, 10):
        for z in range(0, 10):
            a = i * 100 + j * 10 + z
            b = i ** 3 + j ** 3 + z ** 3
            if a == b:
                print(a, end=" ")
