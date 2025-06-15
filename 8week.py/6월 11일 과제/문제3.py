import random
num = int(input())
a = random.randint(1, num)
b = random.randint(1, num)
expect = input()
sum = a + b
if sum % 2 == 0:
  result = "짝수"
else:
  result = "홀수"
if expect == result:
  print(a, b, "맞았습니다")
else:
  print(a, b, "틀렸습니다")