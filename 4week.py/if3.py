money=int(input("돈 입력>"))
if money>5000:
    print("택시 타고 가라")
else:
    if money>2000:
        print("버스 타고 가라")
    else:
        print("걸어 가라")