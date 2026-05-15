def fib(n):
    a = 0
    b = 1
    c = 0
    count = 1

    if n < 0:
        print("Input is invalid")
    elif n == 0:
        print("Series is", a)
    elif n == 1:
        print("Series is", a, b)
    else:
        while count < n:
            a = b
            b = c
            c = a + b
            print(f"Term {count} is {b}")
            count += 1

n=int(input("Enter a number:"))
fib(n)