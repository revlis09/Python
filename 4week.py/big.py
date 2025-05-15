a=int(input("첫번째 수 입력>"))
b=int(input("두번째 수 입력>"))
c=int(input("세번째 수 입력>"))
if a>b:
    if a>c:
        print("가장 큰 수는",a)
    else:
        print("가장 큰 수는",c)
elif b>c:
    print("가장 큰 수는",b)
else:
    print("가장 큰 수는",c)