n=int(input("Enter the number:"))
a=0
b=1
c=0
if n==0:
    print("Series is:", a)
elif n==1:
    print("Series is:",a, b)
elif n<0:
    print("Input is invalid")

else:
    for i in range(1,n):
        a = b
        b = c
        c=a+b
        print(f"Term number:{i} is {b} ")
