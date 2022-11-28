# ex1.py
# coffee = int(input('어떤 커피를 드릴까요?(1.보통/ 2.설탕/ 3.블랙'))
coffee = 0

# 함수
def coffee_machine(button) :
  # coffee = int(input('A손님, 어떤 커피를 드릴까요?(1.보통/ 2.설탕/ 3.블랙'))
  print()
  print("# 1. 뜨거운 물을 준비한다.")
  print("# 2. 종이컵을 준비한다.")

  if coffee == 1:
    print('# 3.보통커피를 탄다.')

  elif coffee == 2:
    print('# 3. 설탕커피를 탄다.')
  elif coffee == 3:
    print('# 3. 블랙커피를 탄다.')
  else:
    print('# 3. 아무거나 탄다.')
  print("# 4. 물을 붓는다.")
  print("# 5. 스푼으로 젓는다.")
  print()


coffee = int(input('어떤 커피를 드릴까요? (1.보통/2.설탕/3.블랙)'))
coffee_machine(coffee)
print('A손님 여기 커피 있습니다.')
