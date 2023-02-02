#to check if a number is a armstrong number or not
n=int(input("Enter the number: "))
a=list (str(n))
b=len(a)
p=0
i=0
while i<b:
    p=p+(int(a[i]))**3
    i+=1
if p==n:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")