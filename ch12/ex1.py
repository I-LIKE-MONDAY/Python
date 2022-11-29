# ex1.py

# 변수 타입이 없고 중괄호 대신 : (콜론) 사용. 들여쓰기가 중요.
class Car:
  color = ''
  speed = 0

  def upSpeed(self, value):
    self.speed += value

  def downSpeed(self, value):
    self.speed -= value
    if self.speed < 0:
      self.speed = 0

## 클래스 선언 끝


myCar1 = Car()  # new 키워드 없음. () 만 있으면 됨
myCar1.color = 'red'
myCar1.speed = 0

myCar2 = Car()
myCar2.color = 'blue'
myCar2.speed = 0
myCar2.upSpeed(30)

print('자동차1의 색상은 %s 이며, 현재 속도는 %dkm 입니다.' % (myCar1.color, myCar1.speed))
print('자동차1의 색상은 %s 이며, 현재 속도는 %dkm 입니다.' % (myCar2.color, myCar2.speed))