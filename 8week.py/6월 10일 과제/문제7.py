num=input().split()
num=list(map(int, num))
count=0
for i in num:
  if i%2==0:
    count+=1
print(count)