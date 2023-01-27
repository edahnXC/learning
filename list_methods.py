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
if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        cmd=input().split()
        if cmd[0]=="append":
                list.append(int(cmd[1]))
        elif cmd[0]=="insert":
                list.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0]=="remove":
                list.remove(int(cmd[1]))
        elif cmd[0]=="sort":
                list.sort()
        elif cmd[0]=="pop":
                list.pop()
        elif cmd[0]=="reverse":
                list.reverse()
        else:
                print("Enter the currect command")
print(list)