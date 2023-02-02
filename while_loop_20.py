sum_n=0
sum_p=0
n=1
while n!=0:
    n=int(input("Enter the number: "))
    if n<0:
        sum_n+=n
    else:
        sum_p+=n
print("Sum of the negative numbers is: ",sum_n)
print("Sum of the positive numbers is: ",sum_p )