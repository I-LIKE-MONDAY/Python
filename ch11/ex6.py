# ex6 : 명화

inFp, outFp = None, None
inStr = ''

inFp = open('C:/temp/aaa.jpg', 'rb')
outFp = open('C:/temp/ccc.jpg', 'wb')

while True:
  inStr = inFp.read(1)  # 문자가 아니기때문에 realine 불가능
  if not inStr:
    break
  outFp.write(inStr)

inFp.close()
outFp.close()
print('---이전 파일이 정상적으로 복사되었음---')