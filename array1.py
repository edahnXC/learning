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
        print(element,end=',')
        j+=1
    i+=1
print()

#6-insert a row at index 2
Arr.insert(2, [8, 9, 10])
print(Arr)

#7-inserting an element into the array arr in the row and column 1
Arr[2][1]=1
print(Arr)

#8-update the array element at row no-2 and coloumn 0 with value 4
Arr[2][0]=4
print(Arr)

#9-update the row 1 with another row value
Arr[1]=[3,4,5]
print(Arr)

#10-delete the array element at position 0,0
del Arr[0][0]
print(Arr)

#11-delete the row 0 from entry
del Arr[0]
print(Arr)

#12-to insert,display and delete element
def insert_element(Arr, row, col, value):
    Arr[row][col] = value
    print("1.Insert Operation -",Arr)

def delete_element(Arr, row, col):
    del Arr[row][col]
    print("     2.Delete Operation -",Arr)

def display_array(Arr):
    print("     3.Display Operation -", end=" ")
    for i in range(len(Arr)):
        for j in range(len(Arr[0])):
            print(Arr[i][j], end = ",")

insert_element(Arr, 0, 1, 82)
delete_element(Arr, 0 , 1)
display_array(Arr)
print()
#13-matrices addition
# m1=[[1,2,3],
#     [4,5,6],
#     [6,7,8]]
# m2=[[2,2,2],
#     [2,2,2],
#     [2,2,2]]

# result=[[0,0,0],
#        [0,0,0],
#        [0,0,0]]
    
# i=0
# while i<len(m1):
#     j=0
#     while j<len(m1[0]):
#         result[i][j]=m1[i][j]+m2[i][j]
#         j+=1
#     i+=1
# print(result)
m1=[[1,2,3],
    [4,5,6],
    [6,7,8]]
m2=[[2,2,2],
    [2,2,2],
    [2,2,2]]
print("m1: ",m1)
print()
print("m2: ",m2)
result=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    
i=0
while i<len(m1):
    j=0
    while j<len(m1[0]):
        result[i][j]=m1[i][j]+m2[i][j]
        j+=1
    i+=1
print(result)

