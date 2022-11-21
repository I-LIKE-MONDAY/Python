## 함수 선언 부분 ##
def myFunc():
    print("함수를 호출함.")

# 전역 변수 : 들여쓰기 밖에서 선언
gVar = 100

if __name__ == '__main__':
    print("메인 함수 부분이 실행 됩니다.")
    myFunc()
    print("전역 변수 값 : ", gVar)
