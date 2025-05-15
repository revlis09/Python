import random as r
a=str(r.randint(0,99))
b=input("복권번호를 입력하세요(0~99)")

print("당첨번호는",a,"입니다")
if a[0]==b[0] or a[1]==b[1]:
    print("상금 50만")
elif a==b:
    print("상금 100만원")
else:
    print("상금이 없습니다")