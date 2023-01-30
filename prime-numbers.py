# def prime(a):
#     for i in a:
#         prime=0
#         for j in range(2,i):
#             if i%j==0:
#                 prime=1
#                 break
#         if prime==0:
#             print(i)
a=[]
i=56
# while i>=56:
# for j in range(2,i):
j=2
while j<i:
    if i%j==0:
        a.append(j)
    j+=1
print(a)
# prime(a)
# for i in a:
#     prime=0
#     for j in range(2,i):
#         if i%j==0:
#             prime=1
#             break
#     if prime==0:
#         print(i)
# i+=1    
i=0
while i<len(a):
    j=2
    prime=0
    while j<a[i]:
        # print(a[i])
        if a[i]%j==0:
            prime=1
            break
        j+=1
    if prime==0:
        print(a[i])
    i+=1

  


