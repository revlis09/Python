email=input()
for i in email:
  if i != "@":
    print(i, end="")
  else:
    break