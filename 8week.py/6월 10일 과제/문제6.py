score=input().split()
total=0
score[0]=int(score[0])
score[1]=int(score[1])
score[2]=int(score[2])
count=0
for i in score:
  total+=i
  count+=1
print(f"{total/count:.2f}")