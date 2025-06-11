n=int(input())
daylist=[]
for i in range(n):
  att=list(map(int, input().split()))
  daylist.append(att)

count=0

for j in daylist:
  for a in j:
    if a==1:
      count+=1
print(count)