a=int(input("직선1의 길이"))
b=int(input("직선2의 길이"))
c=int(input("직선3의 길이"))

if a+b>c and a+c>b and b+c>a:
    print("삼각형 가능.")
else: 
    print("삼각형 불가능.")