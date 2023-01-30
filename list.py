# # a=[1,2,3,4]
# # # a.pop()
# # print(sum(a))
# # n= int(input("Enter the number of command: "))
# # a=[]
# # for i in range(n):
# #     cmd=input().split()
# #     # a.append(i)
# #     if cmd[0]=="append":
# #         a.append(int(cmd[1]))
# #     elif cmd[0]=="insert":
# #         # index=int(input("Enter the index: "))
# #         a.insert(int(cmd[2]),int(cmd[1]))
# #     elif cmd[0]=="pop":
# #         a.pop()
# #     elif cmd[0]=="remove":
# #         a.remove(int(cmd[1]))
# #     elif cmd[0]=="sum":
# #         print(sum(a))
# #     else:
# #         print("error")
# # print(a)

# for i in range(10):
#     # print(i)
#     if i==5:        
#         continue
#     print(i)
# for i in range(5):
#     for j in range(i+1):
#         print(1,end=" ")
#     print()
# for i in range(6):
#     for j in range(i):
#         print(j,end=' ')
#     print()
i=1
while i<=100:
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
    i+=1