# ex3

def func1():
  a = 10
  print('func1()에서 a값 %d' % a)

def func2():
  print('func1()에서 a값 %d' % a)

a = 20 # 전역변수
func1()
func2()

def func3():
  global b  # 전역변수
  b = 20
  print('func3()에서 b값 %d' % b)

def func4():
  print('func3()에서 b값 %d' % b)

func3()
func4()
