# ex1.py

for i in range(0, 3):
    print("안녕하세요", i)

for i in range(0, 10, 2):   # range() 세번째 숫자 : 증가치
    print("반갑습니다", i)

# 1 ~ 10 까지의 합을 리턴
sum = 0
for i in range(1, 11, 1):
    sum = sum + i
print("sum : ", sum)

