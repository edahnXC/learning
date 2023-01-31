n=int(input("Enter the number:"))
i=0
j=2
while j<n:
    if n%j==0:
        i+=1
    j+=1
if i==0:
    print(n ,"is prime")
else:
    print(n," is not prime")