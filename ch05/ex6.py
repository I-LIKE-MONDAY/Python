# 문제
# 1. 입력한 수식 계산  2. 두 수 사이의 합계 : 1
#  *** 수식을 입력하세요 : 3+4
#  3+4 결과는   7.0입니다.
#
# 힌트 :  eval 함수 사용
#
# 1. 입력한 수식 계산  2. 두 수 사이의 합계 : 2
#  *** 첫 번째 숫자를 입력하세요 : 10
#  *** 두 번째 숫자를 입력하세요 : 20
# 10+...+20는 165입니다.

select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

## 메인 코드 부분 ##
# 힌트 : eval 함수 사용(수식을 문자도 출력 해주는 함수)
select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

if select == 1:
    answer = input("수식을 입력하세요 : ")
    print("%s 결과는 %5.1f 입니다." % (answer, eval(answer)))

elif select == 2:
    num1 = int(input("*** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("*** 두 번째 숫자를 입력하세요 : "))
    for i in range(num1, num2 + 1):
        answer = answer + i
    print("%d + ... + %d는 %d 입니다." % (num1, num2, answer))

else:
    print("1 또는 2만 입력해야합니다.")
