# ex4.py

# list(리스트)

import random

numbers = []
for num in range(1, 11): # 0 ~ 9
    numbers.append(random.randrange(0,11))

for num in range(1, 11): # 0 ~ 9
    if num not in numbers: # numbers 안에 num이 없으면 실행되는 if문
        print("숫자 %d는 리스트에 없네요" % num)

print("생성된 리스트", numbers)