i, dan = 0, 0

for i in range(2, 10, 1):
    print("#  %d단  #" % i, end=' ')

for i in range(1, 10, 1):
    print()
    for j in range(1, 10, 1):
        print("%d X %d = %2d" % (i, j, i * j), end=' ')



