n=int(input("enter the number of terms: "))
i=1
r=0
sum=0
while i<=n:
  r=i**2
  sum=sum+r
  i+=1
print("Sum of the given sequence is: ",sum)
print()

a=1
while a<=n:
    print(a**2,end=',')
    a+=1