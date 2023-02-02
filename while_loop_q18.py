#to print the sum of the series 1/1!+1/2!+1/3!+.....+1/n!
n=int(input("Enter the number: "))
i=1
f=1
sum=0
while i<=n:
    f=f*i
    sum=sum+1/f
    i+=1
print("The sum of the given series till the number",n,"is",round(sum,2))