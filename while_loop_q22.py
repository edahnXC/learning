#program to print the sequence 1+1/1!+1/2!.....+1/n!
n=int(input("n: "))
f=1
i=1
s=1
while i<=n:
    f=f*i
    s=s+1/f
    i+=1
print("sum of the sequence is: ",s)