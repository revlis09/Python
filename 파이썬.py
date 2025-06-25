n= int(input("학생수 입력:"))
scores=list(map(int, input("점수를 입력하시오:").split()))
averge=sum(scores)/n
print(f"평균: {averge:.2f}")
count=0
a=[]
for i in scores:
  if i<=60:
    count+=1
  else:
    a.append(i)

print("통과 한 사람 점수: ", end="")
for j in a:
  print(j, end=" ")


print("\n통과 하지 못한 사람의 수", count)