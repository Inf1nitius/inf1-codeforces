n, t = map(int, input().split())
q = list(input())

for _ in range(t):
    x = [i for i in range(n - 1) if q[i] == "B" and q[i + 1] == "G"]
    for y in x:
        q[y], q[y + 1] = q[y + 1], q[y]

print("".join(q))
