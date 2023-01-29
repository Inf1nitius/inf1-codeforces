import itertools

n = int(input())
hl = []
al = []
for _ in range(n):
    h, a = map(int, input().split())
    hl.append(h)
    al.append(a)

x = sum(h == a for h, a in itertools.product(hl, al))
print(x)
