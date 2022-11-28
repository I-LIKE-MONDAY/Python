# ex5

def para_func(*para):  # (*인수) : 가변인수와 유사한 개념
  result = 0
  for num in para:
    result += num
  return result


hap = para_func(10, 20)
print('%d' % hap)
hap = para_func(10, 20, 30)
print('%d' % hap)
hap = para_func(10, 20, 30, 40)
print('%d' % hap)
