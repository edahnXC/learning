n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
even_sum=0
odd_sum=0
if n1>n2:
    while n2<=n1:
        if n2%2==0:
            even_sum=even_sum+n2
            n2+=1
        else:
            odd_sum=odd_sum+n2
            n2+=1
else:
    while n1<=n2:
        if n1%2==0:
            even_sum=even_sum+n1
            n1+=1
        else:
            odd_sum=odd_sum+n1
print("Sum of the even numbers two numbers:",even_sum)
print("sum of the odd numbers between the two numbers:",odd_sum)