n=int(input("Enter the number:"))
if n<2:
    print(n,"is neither prime nor composite")
else:
    j=2
    while j<n:
        prime=0
        if n%j==0:
            prime=1
        j+=1
    if prime==0:
        print(n ,"is prime")
    else:
        print(n," is not prime")