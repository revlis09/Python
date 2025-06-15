n=int(input())
count=0
list=[]
while count<n:
  num=int(input())
  list.append(num)
  count+=1
max=list[0]
for i in list:
  if max<i:
    max=i
print("가장 큰 수", max)
print("가장 큰 수의 위치", list.index(max)+1)


