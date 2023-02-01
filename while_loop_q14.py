n=int(input("Enter the number: "))
a=list(str(n))
b=len(a)
i=0
numb={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
while i<b:
    print(numb[int(a[i])],end=' ')
    i+=1