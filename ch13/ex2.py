# ex2.py : DB 연동 :

# pip install pymysql
import pymysql

con, cur = None, None
data1, data2, data3, data4 = '', '', '', ''
sql = ''
row = None  # 변수 추가


con = pymysql.connect(host='localhost', user='root', password='1234', db='mydb', charset='utf8')
cur = con.cursor()    # 커서를 통해서 실행

cur.execute('SELECT * FROM tblmember2') # 쿼리문 실행

print('사용자ID    사용자이름       이메일     출생년도')
print('----------------------------------------------')
while(True):
  row = cur.fetchone()  # 레코드 한 줄 읽어옴 (fatch : 가져오다)
  if row == None:
    break
  data1 = row[0]
  data2 = row[1]
  data3 = row[2]
  data4 = row[3]
  print('%6s   %10s   %10s   %5s' % (data1, data2, data3, data4))

con.close()