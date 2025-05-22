import random
com=random.randint(1, 100)
while True:
  player=int(input("1부터 100사이의 숫자야, 맞춰봐> "))
  if com==player:
    print("정답")
    break
  else:
    if com>player:
      print("up")
    else:
      print("down")
