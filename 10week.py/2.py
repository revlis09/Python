n=input("주민등록번호 입력> ")
gander=n[7]
birth=n[:2]
if gander=="1" or gander=="3":
  gander_last="남자"
elif gander=="2" or gander=="4":
  gander_last="여자"

if gander=="1" or gander=="2":
  birth_last=1900+int(birth)
elif gander=="3" or gander=="4":
  birth_last=2000+int(birth)

print(f"{birth_last}년 태어난 {gander_last}")

