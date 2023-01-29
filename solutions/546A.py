k, n, w = map(int, input().split())
cost = sum(k * i for i in range(w + 1))

if cost > n:
    print(cost - n)
else:
    print(0)
