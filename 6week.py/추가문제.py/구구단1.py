import random
print("구구단을 외자! 구구단을 외자!")
count=0
while count<10:
  n=random.randint(1, 9)  
  a=random.randint(1, 9)  
  print(n,"*",a, "?")
  correct=n*a
  num=input()
  num=int(num)
  if num!=n*a:
    print("땡! 정답은", correct)
  count+=1
