n=int(input())
for i in range(1, n+1):
  if '3'in str(i) or '6'in str(i) or '9'in str(i) :
    print("짝", end="")
  else:
    print(i, end=" ")