n=int(input("Enter the number: "))
if n>-1 and n<2:
    print(n,"is neither prime nor composite")
else:
    j=2
    prime=0
    while j<n:
        if n%j==0:
            prime=1
            break
        j+=1
    if prime==0:
        print(n," is prime")
    else:
        print(n,"is a composite number")
