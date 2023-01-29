k = int(input())
p = list(map(int, input().split()))
x = max(p) - 25 if max(p) > 25 else 0
print(x)
