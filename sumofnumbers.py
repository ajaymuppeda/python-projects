number=int(input("Enter a natural number:"))
sum_digits=0
while number>0:
    digit=number%10
    sum_digits += digit
    number=number//10
print("The sum of the digits is:",sum_digits)
 