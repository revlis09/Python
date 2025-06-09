friend=[]
count=0
while True:
  name=input("친구 이름 입력: ")
  count+=1
  friend.append(name)
  if count>=5:
    break
print(friend)