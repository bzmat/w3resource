# write a Python program to get the Fibonacci series between 0 to 50.

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("żly numer")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(0, n):
            c = a + b
            a = b
            b = c
            print(a)


def  fibonacci2(n):
    x = 0
    y = 1
    while y < n:
        print(y)
        x,y = y, x+y


fibonacci2(9)


