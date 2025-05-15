import random as r
print("동전 던지기 게임을 시작합니다")
coin=r.randint(0,1)
a=int(input("앞면/뒷면을 입력해주세요>"))
if coin==0:
    print("앞면입니다")
else:
    print("뒷면입니다")
print("게임이 종료되었습니다")