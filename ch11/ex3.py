# ex3.py : 쓰기

outFp = None
outStr = ''

outFp = open('C:/temp/data2.txt', 'w')

while True:
  outStr = input('내용 입력 : ')
  if outStr != '':
    outFp.write(outStr + '\n')
  else:
    break

outFp.close()
print('--- 파일에 정상적으로 써졌음 ---')