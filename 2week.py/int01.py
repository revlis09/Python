#int 01
string_a=input("입력 A> ")
int_a=int(string_a)

string_b=input("입력 B> ")
int_b=int(string_b)

print("문자열 자료:", string_a+string_b)
print("숫자 자료:", int_a+int_b)

#int 02
input_a=float(input("첫 번째 숫자> "))
input_b=float(input("두 번째 숫자> "))

print("덧셈결과:", input_a+input_b)
print("뺄셈결과:", input_a-input_b)
print("곱셈결과:", input_a*input_b)
print("나눗셈결과:", input_a/input_b)

#int 03
print("안녕하세요? 이름을 입력해 주세요")
name=input()
print(name, "님 안녕하세요?")
age=input("나이를 입력해 주세요")
print(20-int(age), "년 후면 20살이시네요")