s=[]
for _ in range(int(input())):
  name = input()
  score = float(input())
  s.append([name,score])
hs = sorted(set([score for name, score in s]))[1]
print('\n'.join(sorted([name for name, score in s if score==hs])))
