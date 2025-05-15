import random as r
a=r.randint(1,9)
b=r.randint(1,9)
answer=int(input(f'{a}*{b}는 무엇일까요?'))
if answer==a*b:
    print("정답입니다")
else:
    print("구구단 공부합시다")