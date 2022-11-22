# ex4.py

i, dan = 0, 0

dan = int(input("단을 입력하세요 : "))

# % 와 d 사이의 숫자는 공백의 갯수를 뜻함
for i in range(1, 10, 1):
    print("%d X %d = %2d" % (dan, i, dan * i))


