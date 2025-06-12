id = "admin"
pw = "1234"
id_user = input()
pw_user = input()
list = ['#', "'", '"', "/", "(", ")", "%", ":"]
value = id_user + pw_user
for i in list:
  x = value.count(i)
  if x > 0:
    print("잘못입력되었습니다.")
    break

if id == id_user and pw == pw_user:
  print("환영합니다")
elif id == id_user and pw != pw_user:
  print("비번이 다릅니다")
elif id != id_user and pw == pw_user:
  print("아이디가 다릅니다")

