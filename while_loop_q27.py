a=[]
i=0
while i<10:
    n=int(input("enter the number: "))
    a.append(n)
    i+=1
a.sort()
print("The largest number is:",a[-1])
print("The smallest number is:",a[0])