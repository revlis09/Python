while 1:
  score=input("점수를 입력하세요: ")
  score=int(score)
  if 0<=score<=100:
      if score>=80:
        print("합격입니다")
        break
      elif score<80:
        print("불합격입니다")
        break
  else:
    print("오류입니다")

    
