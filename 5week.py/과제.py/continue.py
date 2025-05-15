sum =0
for i in range(1, 101):
  if i%3==0:
    continue
  sum= sum+i
print("1~100의 합(3의 배수제외): ", sum)