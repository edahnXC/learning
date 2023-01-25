'''
#a,b,c=map(float,input("enter the number a,b and c: ").split())
print(a+b+c)
a,b=map(float,input("enter the number a,b: ").split())
print(a//b)

#x,y,z=map(int,input("Enter the value of x,y and z: ").split())
print(f"Equation:- ({x}+{y})*{z}")
print((x+y)*z)

#a=input("enter: ")
print(f"{a} {type(a)}") 

#a=input("enter: ")
# print(a[4:-3:-1])
for i in range(len(a)-3,3,-1):
    print(a[i],end='')
a=input("enter: ")
for i in range(len(a)-4,3,-1):
    print(a[i],end='')
'''
a="hello"
# print(a.replace("l","a",1))
# a1= a[:3]+'a'+a[4:]
# print(a1)
l_ind = a.index('l')
a1=''
for i in range(len(a)):
    if a[i] == 'l' and i != l_ind:
        a1+='a'
    else: 
        a1+=a[i]
