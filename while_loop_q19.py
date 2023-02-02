# n=int(input("Enter the number of time user input is needed: "))
# i=1
# sum=0
# while i<=n:
#     a=int(input("Enter the number: "))
#     sum+=a
#     i+=1
# print("Sum of the user input provided is:",int(sum))
a='yes'
sum=0
while a=='yes':
    num=int(input("Enter the number: "))
    sum+=num
    a=input("enter 'yes' to add another number: ")
print(int(sum),"is the sum of the given numbers")
