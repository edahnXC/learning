#TO PRINT THE SEQUENCE OF 2,22,222,2222......N TERMS
# n=int(input("n: "))
# i="2"
# j=0
# while j<n:
#     print(i,end=',')
#     i+="2"
#     j+=1
# print(type(i))

#to print the elements inside a stack in a reverse order
s=['R','A','U','N','E','E','T']   
i=s.index(s[-1])
while i>=0:
    print(s[i],end=',')
    i-=1

