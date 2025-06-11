daylist=[[0,1,0,0,1],[0,0,1,0,0],[0,1,0,1,0],[0,0,0,1,0],[0,0,0,0,0]]
count=0
for i in daylist:
  for j in i:
    if j==1:
      count+=1
print(count)