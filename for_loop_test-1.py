#program to print first 10 even number and 10 odd numbers 
for i in range(2,21,2):
    print(i,end=' ')        #first 10 even numbers
print("are the first 10 even numbers")
print()
for i in range(1,21,2):
    print(i,end=' ')              #first 10 odd numbers
print("are the first 10 odd numbers")
print()

#-2 program to print first 10 even numebers in reverse order
for i in range(20,0,-2):
    print(i,end=' ')
print("are the 10 even numbers in reverse order")

#-3 to check if a number is palindrome using while loop
n=int(input("Enter the number: "))
if n==0:
    print("the number should be greater than zero")
else:
    palindrome=n
    r=0
    p=0
    j=len(str(n))
    i=0
    while i<j:
        r=n%10
        p=p*10+r
        n=n//10
        i+=1
    if palindrome==p:
        print("The given number is palindrome")
    else:
        print("The given number is not Palindrome")