#q1 create a 2D array arr 
import array as Arr
Arr=[[1,2,3],[4,5,6],[7,8,9]]
print(Arr)
print()

#2- access entire first row 
print(Arr[0])
print()

#3-access the element at row 1 and column 2
print(Arr[0][1])
print()

#4-individually access each element of the Array arr
for i in Arr:
    for j in i:
        print(j,end=',')
print()

#5- traverse the entire array arr using loop
# for i in range(len(Arr)):
#     for j in range(len(Arr[0])):
#         j=Arr[i][j]
#         print(j,end=',')
i=0
while i<len(Arr):
    j=0
    while j<len(Arr[i]):
        element=(Arr[i][j])
        print(element)
        j+=1
    i+=1


#6-insert a row at index 2
new_row=[2,3,4]
Arr.insert=(2,new_row)
print(Arr)