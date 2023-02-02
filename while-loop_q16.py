#factorial of number using while loop
n=int(input("Enter the number: "))
a=list(str(n))
b=len(a)
f=1
i=1
while i<=n:
    f=f*i
    i+=1
print("factorial of number ",n," is ",f)