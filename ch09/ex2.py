# ex2.py

def plus(v1, v2):
  result = v1 + v2
  return result

hap = 0

hap = plus(100, 200)
print('100과 200 의 plus함수 결과는 %d', hap)

def calc(v1, v2, op):
  result = 0

  if op == '+':
    result = v1 + v2

  elif op == '-':
    result = v1 - v2

  elif op == '*':
    result = v1 * v2

  elif op == '/':
    result = v1 / v2

  return result
  
res = 0
var1, var2, oper = 0, 0,''
oper = input('계산을 입력하세요(+,=,* /)')
var1 = int(input('첫 번째 수를 입력하세요'))
var2 = int(input('두 번째 수를 입력하세요'))

res = calc(var1, var2, oper)
print('## 계산기 : $d %s %d = %d' % (var1, oper, var2, res))



  