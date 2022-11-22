# ex2.py

# 500과 1000 사이에 있는 홀수의 합계
# 방법 1
sum = 0
for i in range(500, 1001):
    if (i % 2 != 0):
        sum = sum + i
print("sum은 %d" % sum)

# 방법 2
sum = 0
for i in range(501, 1001, 2):   # 홀수에서 시작해서 2씩 더하면 자동 홀수임
    sum = sum + i
print("sum은 %d" % sum)