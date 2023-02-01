#fibonaci series 
n=int(input("n: "))
if n==0:
    print("0")
elif n==1:
    print("1")
elif n==2:
    print("1,1")
else:
    first_numb=0
    second_numb=1
    print(first_numb,second_numb,end=' ')
    i=2
    while i<n:
        numb=first_numb+second_numb
        print(numb,end=' ')
        first_numb=second_numb
        second_numb=numb
        i+=1

