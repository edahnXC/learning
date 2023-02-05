#program to find the sum of the digits of a number accepted from user
#using for loop
n=int(input("Enter the number: "))
s=0
j=str(n)
for i in j:
    s=s+int(i)
print("sum of the digits of a number using for loop: ",s)
print()
#using while loop
sum=0
r=0
while n!=0:
     r=n%10
     sum=sum+r
     n=n//10
print("sum of the digits of number using while loop:",sum)