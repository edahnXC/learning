# a=[]
# n=int(input("enter the number of commands: "))
# for i in range(n):
#     cmd=(input().split())
#     if cmd[0]=="append":
#         a.append(int(cmd[1]))
#     elif cmd[0]=="insert":
#         a.insert(1,int(cmd[1]))
#     elif cmd[0]=="pop":
#         a.pop()
#     elif cmd[0]=="remove":
#         a.remove(int(cmd[1]))
#     elif cmd[0]=="sum":
#         print(f"sum is:{sum(a)}")
#     else:
#         print("Error,the command given is wrong")
# print(a)
n = int(input())
a=[]
for i in range(n):
    cmd=input().split()
    if cmd[0]=="append":
        a.append(int(cmd[1]))
    elif cmd[0]=="insert":
        a.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=="remove":
        a.remove(int(cmd[1]))
    elif cmd[0]=="sort":
        a.sort()
    elif cmd[0]=="pop":
        a.pop()
    elif cmd[0]=="reverse":
        a.reverse()
    else:
        print("Enter the correct command")
print(a)