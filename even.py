# i=100
# while i<=2000:
#     if i%2==0:
#        print(i)
#     i+=1
i=1
while i<=4:
    j=1
    while j<=i:
        print("*",end='')
        j+=1
    print()
    i+=1
a=[1,2,3,4,5,6]
i=0
while i<=len(a)-1:
    print(a[i])
    i+=1

b="hello"
i=0
while i<=len(b)-1:
    print(b[i])
    i+=1
# a=[[1,2,3],[4,5,6]]
# for i in range(len(a)):
#     for j in range (len(a[i])):
#         print(a[i][j],end=',')
#     print()
a=[[1,2,3],[4,5,6]]
i=0
while i<=len(a)-1:
    j=0
    while j<=len(a[i])-1:
        print(a[i][j], end=',')
        j+=1
    print()
    i+=1

