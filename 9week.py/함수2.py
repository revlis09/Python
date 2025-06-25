def avg(m, s, i):
  average=(m+s+i)/3
  return average
math=int(input("수학: "))
sice=int(input("과학: "))
info=int(input("정보: "))
result=avg(math, sice, info)
print(result)