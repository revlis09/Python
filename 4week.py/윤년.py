a=int(input("연도를 입력해 주세요"))
if a%400==0 and a%100!=0 or a%4==0:
    print(str(a)+"은 윤년입니다")
else:
    print(str(a)+"은 윤년이 아닙니다")