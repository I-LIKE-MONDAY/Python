"""
  파일명 : ex2.py
  개발자 : Gwak
"""

ss = input('입력 문자열 ==> ')
print('출력 문자열 ==> ', end="")

if ss.startswith('(') == False:
  print('(', end="" ) # 첫 글자가 ( 로 시작하지 않으면 False가 아니므로 if문 false -> ( 추가

print(ss, end="")

if ss.endswith(')') == False:
  print(')', end="" ) # 끝 글자가 ) 로 끝나지 않으면 False가 아니므로 if문 false -> ) 추가


inStr = '    한글 Python 프로그래밍    '
# inStr에 공백문자를 제거하고 리턴
outStr = ""
#
# i = 0
#
# for i in range(0, len(inStr)):
#   if inStr[i] == " ":
#     continue
#   elif inStr[i] != " ":
#     outStr += inStr[i]
#
# print("원래 문자열 ==> " + '[' + inStr + ']')
# print("공백 삭제 문자열 ==> " + '[' + outStr + ']')

############################################################################

for i in range(0, len(inStr)):
  if inStr[i] != ' ':
    outStr += inStr[i]

print("원래 문자열 ==> " + '[' + inStr + ']')
print("공백 삭제 문자열 ==> " + '[' + outStr + ']')

inStr = 'Live as if you will die today'

print(inStr.replace('i', '$'))