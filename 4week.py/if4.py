a=int(input("연소득 입력>"))
b=int(input("재직기간 입력>"))
if a>=40000000 and b>=2:
    print("대출 자격 있음")
else:
    if 40000000>a:
        print("연봉 4000만원 이상 필요")
    else:
        print("재직기간 2년 이상 필요")