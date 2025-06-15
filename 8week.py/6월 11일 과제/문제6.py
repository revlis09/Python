money=int(input())
day=int(input())
n=input().split()
for i in n:
  money_1=money*(1+0.01*float(i))
if money>money_1:
  print("망함")
elif money==money_1:
  print("본전")
else:
  print("인생역전")