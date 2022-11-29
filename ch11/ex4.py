# ex4.py : 복사

inFp, outFp = None, None
inStr = ''

inFp = open('C:/temp/data1.txt', 'r')
outFp = open('C:/temp/data6.txt', 'w')

inList = inFp.readlines()
for inStr in inList:
  outFp.writelines(inStr)

inFp.close()
outFp.close()
print('---복사 완료---')
