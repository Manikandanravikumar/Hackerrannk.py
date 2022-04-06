n = int(input())
d={}
for _ in range(n):
    l=input().split()
    d[l[0]]=sum(map(float,l[1:]))/3
print('%.2f' % d[input()])    
