n = int(input())
i = 0

for _ in range(n):
    p, v, t = input().split()
    p = int(p)
    v = int(v)
    t = int(t)

    if p + v + t > 1:
        i += 1

print(i)
