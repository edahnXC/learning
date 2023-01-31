n=int(input("Enter the number: "))
i=0
product=1
while n!=0:
    i=n%10
    product*=i
    n=n//10
print(product)