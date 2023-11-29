def fibonacci(num):
    x1 = 0
    x2 = 1
    for n in range (0, num):
        if n % 2 == 0:
            print(x1)
            x1 += x2
        else:
            print(x2)
            x2 += x1

fibonacci(12)            