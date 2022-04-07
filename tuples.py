n = int(raw_input())
l = map(int, raw_input().split())
t=()
for x in l:
    t+=(x,)
print(hash(t))
