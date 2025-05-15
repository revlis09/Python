num = int(input("정수를 입력하세요: "))

if num % 2 == 0 and num % 3 == 0:
    print(str(num) + "은 2와 3의 배수입니다.")
elif num % 2 == 0:
    print(str(num) + "은 2의 배수이고 3의 배수는 아닙니다.")
elif num % 3 == 0:
    print(str(num)+"은 3의 배수이고 2의 배수는 아닙니다.")
else:
    print(str(num)+"은 2와 3의 배수가 아닙니다.")