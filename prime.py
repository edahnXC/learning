# n=int(input("Enter the number: "))
# if n>-1 and n<2:
#     print(n,"is neither prime nor composite")
# else:
#     j=2
#     prime=0
#     while j<n:
#         if n%j==0:
#             prime=1
#             break
#         j+=1
#     if prime==0:
#         print(n," is prime")
#     else:
#         print(n,"is a composite number")

a=[]
b=[]
n=int(input("Enter the number: "))
j=2
prime=0
while j<n:
    if n%j==0:
        a.append(j)
    j+=1
print(a)

i=0
while i<len(a):
    j=2
    while j<a[i]:
        if a[i]%j==0:
            prime=1
            break
        j+=1
    if prime==0:
        b.append(a[i])
    i=i+1
print(b)