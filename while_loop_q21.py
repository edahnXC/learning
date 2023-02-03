n=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))
r=0
if n>m:
    while r!=0:
        r=n%m
        if r==0:
            hcf=m
        else:
            n=m
            m=r
else:
    while r!=0:
        r=m%n
        if r==0:
            hcf=n
        else:
            m=n
            n=r
print("Hcf of the two number is: ")