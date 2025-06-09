import random
alist=[]
for _ in range(1, 6):
  alist.append(random.randint(1, 100))

if 50 in alist:
  print("50이 존재합니다")
else:
  print("50이 존재하지 않습니다")
print("리스트 숫자:", alist)
