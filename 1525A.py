t = int(input())

for _ in range(t):
    k = int(input())
    y = 100
    if k in {100, 0}:
        print(1)
    else:
        while y:
            k, y = y, k % y
        print(100 // k)
