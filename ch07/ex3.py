# ex3.py

# 1 ~ 100 사이의 값들 중, 짝수는 aa에, 홀수는 bb에 저장하시오.
aa = []
bb = []

for i in range(2, 101, 2):
    aa.append(i)
print(aa)

for i in range(1, 101, 2):
    bb.append(i)
print(bb)
