# ex7.py : 쓰레드
import time
import threading

class RacingCar:

  carName = ''

  def __init__(self, name):
    self.carName = name

  def runCar(self):
    for _ in range(0, 3):
      carStr = self.carName + '~~ 달립니다.\n'
      print(carStr, end='')
      time.sleep(0.1) # 0.1초

car1 = RacingCar('@자동차1')
car2 = RacingCar('#자동차2')
car3 = RacingCar('$자동차3')

# 멀티 스레딩 안된 케이스 : 동시 실행이 안되고 콘솔창에 한줄씩 뜸
# car1.runCar()
# car2.runCar()
# car3.runCar()

# 멀티 스레딩 된 케이스 : 동시 실행 -> 콘솔창에 한번에 뜸
th1 = threading.Thread(target=car1.runCar)
th2 = threading.Thread(target=car2.runCar)
th3 = threading.Thread(target=car3.runCar)

th1.start()
th2.start()
th3.start()

