#program to display product of the digits of a number accepted from user
n=int(input("Enter the number: "))
j=str(n)
p=1
for i in j:
    p=p*int(i)
print("product of digits using for loop:",p)
print()


#using while loop
r=0
product=1
while n!=0:
    r=n%10
    product=product*r
    n=n//10
print("product of digits using while loop is:",product)
