# ex2.py : 읽기

import os

inFp = None
fName, inList, inStr = '', [], ''

fName = input('파일명을 입력하세요') # C:/temp/data1.txt

if os.path.exists(fName): # 있다면 실행
  inFp = open(fName, 'r', encoding='utf-8')
  inList = inFp.readlines()
  for inStr in inList:
    print(inStr, end='')
  inFp.close()
else:
  print('%s 파일이 없습니다.' % fName)


