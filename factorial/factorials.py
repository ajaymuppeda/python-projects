n=int(input("Enter a number: "))
factorial=1
if n>=0:
    for i in range(1,n+1):
        factorial *=i
    print("Factorial of ",n,"is",factorial)
else:
    print("Factorial is not defined for negative number.")