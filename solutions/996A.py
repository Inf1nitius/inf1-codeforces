n = int(input())

d = [100, 20, 10, 5, 1]
x = 0

for y in d:
    while y <= n:
        n -= y
        x += 1

print(x)
