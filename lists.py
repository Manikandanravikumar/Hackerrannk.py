N = int(input())
L=[]
for i in range(0,N):
    c=input().split()
    if c[0]=="insert":
        L.insert(int(c[1]), int(c[2]))
    elif c[0]=="append":
        L.append(int(c[1]))
    elif c[0]=="pop":
        L.pop()    
    elif c[0]=="print":
        print(L)
    elif c[0]=="remove":
        L.remove(int(c[1]))
    elif c[0]=="sort":
        L.sort()
    else:
        L.reverse()                    
