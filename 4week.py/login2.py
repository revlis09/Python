id = "ilovepython"
pw = "123456"

user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")

if user_id == id and user_pw == pw:
    print("환영합니다")
elif user_id == id:
    print("아이디와 비밀번호가 일치하지 않습니다")
elif user_pw == pw:
    print("아이디를 찾을 수 없습니다")
else: 
    print("로그인 실패")                                      