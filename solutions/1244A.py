from math import ceil

n = int(input())

for _ in range(n):
    a, b, c, d, k = map(int, input().split())
    pn = ceil(a / c)
    pc = ceil(b / d)
    if pn + pc > k:
        print(-1)
    else:
        print(f"{str(pn)} {str(pc)}")
