# ex6
import random

def getNumber():
  return random.randrange(1, 46)  # 1 ~ 45 범위

lotto = []
num = 0

print('*** 로또 추첨을 시작합니다. ***')

while True:
  num = getNumber()
  if lotto.count(num) == 0: # count가 0 : 리스트 내에 번호가 없다.
    lotto.append(num)
  elif len(lotto) >= 6:
    break

print('추첨된 로또 번호 ==> ', end="")
lotto.sort() # 간단하게 정렬
for i in range(0, 6):
  print('%d' % lotto[i], end=", ")