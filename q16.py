from array import *
A=array('i',[])
i=10
while i<151:
    A.append(i)
    i+=10
print(A)
print()

A[4]=55    #to update the values 
print(A)

B=array('i',[1,2,3,4,5])
print(B)

a=B.index(B[-1])
while a>=0:
    print(B[a],end=',')
    a-=1
