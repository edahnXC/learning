a=int(input("Enter the number a: "))
b=int(input("Enter the number b: "))
if a<b:
    while a<b:
        if a%2==0:
            print(a,end=' ')
        a+=1
else:
    while b<a:
        if b%2==0:
            print(b,end=' ')
        b+=1
