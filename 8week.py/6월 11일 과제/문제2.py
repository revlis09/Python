age, year = input().split()
born=2025-int(age)
age_1=int(year)-int(born)
if int(born)>int(year):
  print("아직 태어나지 않았습니다")
else:
  print(age_1)

