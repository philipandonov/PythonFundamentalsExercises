n = int(input())
for i in range(n):
    for k in range (i):
        print("*",end='')
    print("*")
for m in range(n,1,-1):
    for p in range(m-2):
        print("*",end='')
    print("*")