# ex4.py

myList = [30, 10, 20]
print("현재 리스트 : %s" % myList)   # List 문자열 취급 가능
                                     # 현재 리스트 : [30, 10, 20]

myList.append(40)
print("현재 리스트 : %s" % myList)   # 현재 리스트 : [30, 10, 20, 40]

myList.reverse()
print("현재 리스트 : %s" % myList)   # 현재 리스트 : [40, 20, 10, 30]

print("20 값의 위치 : %d" % myList.index(20))   # 20 값의 위치 : 1

myList.insert(2, 222)
print("현재 리스트 : %s" % myList)   # 현재 리스트 : [40, 20, 222, 10, 30]

myList.remove(222)
print("현재 리스트 : %s" % myList)   # 현재 리스트 : [40, 20, 10, 30]

myList.extend([77, 88, 77])
print("현재 리스트 : %s" % myList)   # 현재 리스트 : [40, 20, 10, 30, 77, 88, 77]

print("77 값의 개수 : %d" % myList.count(77))   # 77 값의 개수 : 2
