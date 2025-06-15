n=int(input())
count=0
while count<10:
  a=int(input())
  if a%n==0:
    print(n,"의 배수입니다")
    count+=1
  else:
    print(n,"의 배수가 아닙니다")
    count+=1
print("배수 찾기를 종료합니다")