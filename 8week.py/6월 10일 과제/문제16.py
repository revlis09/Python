daylist=[[0,1,0,0,1],[0,0,1,0,0],[0,1,0,1,0],[0,0,0,1,0],[0,0,0,0,0]]
count=0
for i in daylist:
    if i[1]==1:
      count+=1
print(count)