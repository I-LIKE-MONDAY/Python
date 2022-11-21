# ex1.py
from builtins import int

a = 100
b = 50

# Ctrl + Shift + F10 : 실행 단축키
a = int(input("첫 번째 숫자를 입력하세요 : "))
b = int(input("두 번째 숫자를 입력하세요 : "))

result = a + b
print(a, "+", b, "=", result)
# 문자열은 계산 안됨 -> 정수로 변환 시켜 주어야 함 : int() 로 감싸 주기!
result = a - b
print(a, '-',  b, '=', result)
result = a * b
print(a, "*", b, "=", result)
result = a / b
print(a, "/", b, "=", result)


