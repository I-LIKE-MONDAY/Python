# ex2.py

# ord : 유니코드 값으로 변환해주는 내장 함수
a = ord('a')    # 97
print(a)
a = ord('A')    # 65
print(a)

mask = 0x0F
print(mask)     # 15
# print(mark) %X = 16진수, %o 8진수
print("%x & %x = %x" % (a, mask, a & mask))
print("%X | %X = %X" % (a, mask, a | mask))
# 0100 0001
# 0000 1111

mask = ord('a') - ord('A')
print(mask)   # 32

b = a ^ mask  # %c : 글자
print("%c ^ %d = %c" % (a, mask, b))  # A ^ 32 = a

a = b ^ mask
print("%c ^ %d = %c" % (b, mask, a))  # a ^ 32 = A
