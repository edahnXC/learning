n=int(input("Enter the number: "))
i=0
j=0
while n!=0:
    i=n%10      
    j=j*10+i  
    n=n//10
print(j)