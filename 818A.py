n, k = map(int, input().split())

w = n // 2
d = 0
c = 0

if k < n:
    d = w // (k + 1)
    c = k * d

print(f"{d} {c} {n-c-d}")
