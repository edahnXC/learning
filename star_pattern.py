for i in range(3):
    for j in range(i+1):
        print("*",end=' ')
    print()

for i in range(1,4):
    for j in range(4-i):
        print(' ',end='')
    for k in range(i):
        print('*',end=' ')
    print()
