n=int(input("n: "))
i="2"
j=0
while j<n:
    print(i,end=',')
    i+="2"
    j+=1
print(type(i))