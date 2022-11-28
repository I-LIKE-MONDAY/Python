# 2차원 리스트 (다차원 리스트)
aa = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

for i in range(0, 3):
  for j in range(0, 3):
    print(aa[i][j], end=" ")
  print()

list1 = []
list2 = []
value = 1
for i in range(0, 3):
  for j in range(0, 4):
    list1.append(value)
    value += 1
  list2.append(list1)  # 1차 for문 : [[1, 2, 3, 4]]
  list1 = []
print(list2)  # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for i in range(0, 3):
  for j in range(0, 4):
    print("%3d" % list2[i][j], end=" ")
  print()

