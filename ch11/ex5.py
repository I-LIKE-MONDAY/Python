# ex5 : 암호화/ 해제

i = 0
secu = 0

secuYN = input('1.암호화, 2.암호 해석 중 선택 : ')
inFname = input('입력 파일명을 입력하세요 : ')
outFname = input('출력 파일명을 입력하세요 : ')

if secuYN == '1':
  secu = 100
elif secuYN == '2':
  secu = -100

# C:/temp/normal.txt
inFp = open(inFname, 'r', encoding='utf-8')
outFp = open(outFname, 'w', encoding='utf-8')

while True:
  inStr = inFp.readline()  # 안녕하세요
  if not inStr:
    break

  outStr = '' # 변수 초기화
  for i in range(0, len(inStr)):  # 안녕하세요에서 한글자씩 가져옴
    ch = inStr[i]
    # ord : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
    chNum = ord(ch)
    chNum += secu
    ch2 = chr(chNum)
    outStr += ch2

  outFp.write(outStr)

outFp.close()
inFp.close()
print('%s --> %s 변환 완료' % (inFname, outFname))
