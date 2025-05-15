age=int(input("나이를 입력해주세요?"))
if age>=20:
    print("성인")
elif 20>age>=17:
    print("고등학생")
elif 17>age>=14:
    print("중학생")
elif 14>age>=8:
    print("초등학생")
else:
    print("미취학")