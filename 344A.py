n = int(input())
x = [input() for _ in range(n)]

g = 1 + sum(x[i] != x[i + 1] for i in range(n - 1))
print(g)
