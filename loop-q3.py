#program to check if a number is prime or not
#using for loop
n=int(input("enter the number: "))
if n<2 and n>-1:
    print(n,"is neither prime nor composite number")
for i in range(2,n):
    if n%i==0:
        print(n,"is a composite number")
        break
else:
    print(n,"is a prime number")
print()

#using while loop
i=2
# prime=0
while i<n:
    if n%i==0:
        print(n,"is not a prime number")   #prime=1
        break
    i+=1
# if prime==0:
#     print(n,"is a prime number")
else:
    print(n,"is a prime number")